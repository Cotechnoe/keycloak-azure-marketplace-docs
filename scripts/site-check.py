#!/usr/bin/env python3
"""Validate the configured Jekyll site using only the Python standard library."""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_source(path):
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", raw, re.S)
    require(match is not None, f"{path.name}: missing front matter")
    metadata, body = match.groups()
    return metadata, body


def field(metadata, name, default=None):
    match = re.search(rf"^{name}: (.+)$", metadata, re.M)
    return match.group(1).strip('"') if match else default


def markdown_links(body):
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", body)


class RenderedPage(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.ids = []
        self.links = []
        self.content_links = []
        self.assets = []
        self.text = []
        self.tags = {}
        self.checkboxes = 0
        self.main_count = 0
        self.in_main = False
        self.noindex = False
        self.scripts = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "html":
            self.lang = attrs.get("lang")
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "script":
            self.scripts += 1
        if tag == "main":
            self.main_count += 1
            self.in_main = True
        if tag == "meta" and attrs.get("name") == "robots":
            self.noindex = attrs.get("content") == "noindex, nofollow"
        if tag == "a":
            self.links.append(attrs.get("href", ""))
            if self.in_main:
                self.content_links.append(attrs.get("href", ""))
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.assets.append(attrs.get("href", ""))
        if self.in_main:
            self.tags[tag] = self.tags.get(tag, 0) + 1
            if tag == "input" and attrs.get("type") == "checkbox":
                self.checkboxes += 1
                require("checked" not in attrs, "Completion checkbox unexpectedly checked")

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False

    def handle_data(self, data):
        if self.in_main:
            self.text.append(data)


def validate():
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    baseurl = field(config, "baseurl", "")
    require(baseurl.startswith("/") and not baseurl.endswith("/"), "Invalid project baseurl")
    names = ("README", "QUICKSTART", "SUPPORT", "PRIVACY")
    sources = [ROOT / f"{name}{suffix}.md" for name in names for suffix in ("", "-fr")]
    sources += sorted((ROOT / "docs").glob("*.md"))
    require(len(sources) == 22, "Expected eleven EN/FR page pairs")
    routes = {}
    bodies = {}
    for source in sources:
        metadata, body = read_source(source)
        lang = "fr" if source.stem.endswith("-fr") else "en"
        require(field(metadata, "lang", "en") == lang, f"{source.name}: source language")
        heading = re.search(r"^# (.+)$", body, re.M)
        require(heading and field(metadata, "title") == heading.group(1),
                f"{source.name}: title must match h1")
        relative = source.relative_to(ROOT).with_suffix(".html")
        route = field(metadata, "permalink", "/" + relative.as_posix())
        require(route.startswith("/"), f"{source.name}: absolute site route required")
        routes[source] = route
        bodies[source] = body

    def output_path(route):
        relative = unquote(route).lstrip("/")
        if route.endswith("/"):
            relative += "index.html"
        target = (SITE / relative).resolve()
        require(target.is_relative_to(SITE), f"Output escapes site: {route}")
        return target

    expected_files = {output_path(route) for route in routes.values()}
    require(set(SITE.rglob("*.html")) == expected_files, "Missing or unexpected HTML pages")
    require(set(path for path in SITE.rglob("*") if path.is_file())
            == expected_files | {SITE / "assets/site.css"},
            "Unexpected files exposed by site build")
    pages = {}
    for source, route in routes.items():
        path = output_path(route)
        page = RenderedPage()
        page.feed(path.read_text(encoding="utf-8"))
        require(page.lang == ("fr" if source.stem.endswith("-fr") else "en"), f"{path}: lang")
        require(page.main_count == 1 and page.tags.get("h1") == 1, f"{path}: landmark/h1")
        require(len(page.ids) == len(set(page.ids)), f"{path}: duplicate ids")
        require(page.noindex and not page.scripts, f"{path}: noindex or script policy")
        for warning in re.findall(r"^.*⚠.*$", bodies[source], re.M):
            warning_text = re.sub(r"\*\*|`", "", warning)
            warning_text = re.sub(r"^[-*] ", "", warning_text)
            warning_text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", warning_text)
            require(" ".join(warning_text.split()) in " ".join("".join(page.text).split()),
                    f"{path}: missing technical warning")
        require(page.assets == [baseurl + "/assets/site.css"], f"{path}: local stylesheet")
        body = bodies[source]
        for level in (1, 2, 3):
            require(page.tags.get(f"h{level}", 0)
                    == len(re.findall(rf"^{'#' * level} ", body, re.M)), f"{path}: headings")
        require(page.tags.get("table", 0) == len(re.findall(r"^\|[-| ]+\|$", body, re.M)),
                f"{path}: tables")
        require(page.checkboxes == body.count("- [ ]"), f"{path}: checkboxes")
        expected_links = []
        for link in markdown_links(body):
            url = urlsplit(link)
            if url.scheme:
                require(url.scheme in ("https", "mailto"), f"Unexpected protocol: {link}")
                expected_links.append(link)
            else:
                target = (source.parent / unquote(url.path)).resolve()
                require(target in routes and not url.fragment, f"Bad source link: {link}")
                expected_links.append(baseurl + routes[target])
        require(page.content_links == expected_links, f"{path}: rendered link destinations")
        pages[source] = page

    count = 0
    for source, page in pages.items():
        for link in page.links + page.assets:
            url = urlsplit(link)
            if url.scheme:
                continue
            if not url.path:
                target = output_path(routes[source])
            else:
                require(url.path.startswith(baseurl + "/"), f"Link escapes baseurl: {link}")
                target = output_path(url.path[len(baseurl):])
            require(target.is_file(), f"Broken rendered link: {source.name}: {link}")
            if url.fragment:
                target_page = RenderedPage()
                target_page.feed(target.read_text(encoding="utf-8"))
                require(unquote(url.fragment) in target_page.ids, f"Missing fragment: {link}")
            count += 1

    for en, page in pages.items():
        if en.stem.endswith("-fr"):
            continue
        fr = en.with_name(en.stem + "-fr.md")
        require(fr in pages, f"{en.name}: missing French page")
        require(page.content_links[0] == baseurl + routes[fr], f"{en.name}: FR selector")
        require(pages[fr].content_links[0] == baseurl + routes[en], f"{fr.name}: EN selector")
        for origin in (en, fr):
            expected_nav = (("/", "/QUICKSTART.html", "/SUPPORT.html", "/PRIVACY.html")
                            if origin == en else
                            ("/fr/", "/QUICKSTART-fr.html", "/SUPPORT-fr.html", "/PRIVACY-fr.html"))
            require(pages[origin].links[:5] == ["#main"] + [baseurl + url for url in expected_nav],
                    f"{origin.name}: main navigation language")
        require(page.tags == pages[fr].tags, f"{en.name}: EN/FR HTML structure parity")
        for pattern in (r"^```[^\n]*\n.*?^```", r"^\d+\. "):
            require(re.findall(pattern, bodies[en], re.M | re.S)
                    == re.findall(pattern, bodies[fr], re.M | re.S), f"{en.name}: step/code parity")
        expected = []
        for link in markdown_links(bodies[en])[1:]:
            if urlsplit(link).scheme:
                expected.append(link)
            else:
                target = Path(link)
                expected.append(str(target.with_name(target.stem + "-fr.md")))
        require(markdown_links(bodies[fr])[1:] == expected, f"{en.name}: source link parity")

    print(f"PASS: {len(pages)} pages, 11 language pairs; {count} local HTML/CSS/fragment links.")
    print(f"PASS: {sum(p.tags.get('table', 0) for p in pages.values())} tables; "
          f"{sum(p.checkboxes for p in pages.values())} unchecked checkboxes.")
    print("PASS: titles, landmarks, languages, reciprocal navigation, EN/FR parity, technical warnings.")
    print("PASS: no internal notes, build files, dependencies or scripts exposed.")
    print("Not validated: external HTTP, visual accessibility, public deployment or VM procedures.")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)

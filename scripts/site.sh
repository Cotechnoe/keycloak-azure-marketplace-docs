#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUBY_IMAGE="ruby:3.3.13-bookworm@sha256:ae098d019fd2995e6cb82e16a87529348ba26a7c83ad6189937decc2846b0730"

fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

command -v docker >/dev/null 2>&1 || fail "Docker is required."
docker info >/dev/null 2>&1 || fail "Docker must be running."

run_bundle() {
  docker run --rm \
    --user "$(id -u):$(id -g)" \
    --volume "${ROOT}:/site" --workdir /site \
    --env HOME=/tmp --env BUNDLE_PATH=/site/vendor/bundle \
    --env BUNDLE_APP_CONFIG=/tmp/bundle-config \
    "${RUBY_IMAGE}" bundle "$@"
}

case "${1:-}" in
  setup)
    run_bundle install
    ;;
  build|check)
    [[ -f "${ROOT}/Gemfile.lock" ]] || fail "Run make setup first."
    run_bundle check
    run_bundle exec jekyll build --strict_front_matter --trace
    if [[ "$1" == "check" ]]; then
      command -v python3 >/dev/null 2>&1 || fail "Python 3 is required for validation."
      python3 "${ROOT}/scripts/site-check.py"
      python3 "${ROOT}/scripts/site-check-tests.py"
    fi
    ;;
  serve)
    [[ -f "${ROOT}/Gemfile.lock" ]] || fail "Run make setup first."
    run_bundle check
    docker run --rm \
      --user "$(id -u):$(id -g)" \
      --volume "${ROOT}:/site" --workdir /site \
      --env HOME=/tmp --env BUNDLE_PATH=/site/vendor/bundle \
      --env BUNDLE_APP_CONFIG=/tmp/bundle-config \
      --publish 127.0.0.1:4000:4000 \
      "${RUBY_IMAGE}" bundle exec jekyll serve --host 0.0.0.0 --port 4000
    ;;
  *)
    fail "Usage: $0 {setup|build|check|serve}"
    ;;
esac

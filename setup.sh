#!/usr/bin/env sh
set -eu

mkdir -p "$HOME/.pi/agent"
cp settings.json "$HOME/.pi/agent/settings.json"
pi install "$(pwd)"

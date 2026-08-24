# Pi Agent Config

Personal Pi package for sharing Pi extensions and skills across machines.

## Install

```sh
pi install git:github.com/Yikai-Liao/pi-agent-config
```

## What is tracked

- `skills/`
- Pi package metadata
- npm dependencies for these Pi packages:
  - `pi-web-access`
  - `@juicesharp/rpiv-ask-user-question`
  - `@juicesharp/rpiv-todo`
  - `@dietrichgebert/ponytail`
  - `@plannotator/pi-extension`
  - `@ff-labs/pi-fff`
  - `@narumitw/pi-btw`
  - `@narumitw/pi-goal`
  - `@narumitw/pi-usage`
  - `pi-subagents`
  - `pi-agent-browser-native`
  - `pi-observational-memory`
  - `open-zk-kb`

## open-zk-kb prerequisite

The integrated knowledge tools require [Bun](https://bun.sh) >= 1.0 on `PATH` for the local SQLite server. Restart Pi after installing this package, then run `knowledge-health` to verify the integration.

## What stays local

- `~/.pi/agent/auth.json`
- `~/.pi/agent/trust.json`
- `~/.pi/agent/settings.json`
- sessions, package caches, runtime model state

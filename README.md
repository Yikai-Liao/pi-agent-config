# Pi Agent Config

Personal Pi package for sharing Pi extensions and skills across machines.

## Install

```sh
pi install git:github.com/Yikai-Liao/pi-agent-config
```

Update Pi and the installed plugins with `pi update --all`.
The pnpm configuration uses a hoisted dependency layout for Pi's TypeScript
extension loader and explicitly allows required dependency build scripts.

## What is tracked

- `skills/`
- Pi package metadata
- npm dependencies for these Pi packages:
  - `@howaboua/pi-codex-conversion`
  - `pi-web-access`
  - `@juicesharp/rpiv-ask-user-question`
  - `@plannotator/pi-extension`
  - `@ff-labs/pi-fff`
  - `@narumitw/pi-btw`
  - `@narumitw/pi-goal`
  - `@narumitw/pi-usage`
  - `pi-subagents`
  - `pi-draft-history`

The local pnpm registry must be the public npm registry rather than the
npmmirror mirror. This is important for `pi-zentui`: the public registry
provides the `0.24.0` tarball, while the mirror returned
`ERR_PNPM_FETCH_404` for it.

## What stays local

- `~/.pi/agent/auth.json`
- `~/.pi/agent/trust.json`
- `~/.pi/agent/settings.json`
- sessions, package caches, runtime model state

# Pi Agent Config

Personal Pi package for sharing reusable skills and settings across machines.

## Install

```sh
git clone git@github.com:Yikai-Liao/pi-agent-config.git ~/pi-agent-config
cd ~/pi-agent-config
./setup.sh
```

## What is tracked

- `skills/`
- `settings.json`
- Pi package metadata
- npm dependencies for these Pi packages:
  - `@vigolium/piolium`
  - `pi-web-access`
  - `@juicesharp/rpiv-ask-user-question`
  - `@juicesharp/rpiv-todo`
  - `@dietrichgebert/ponytail`
  - `@plannotator/pi-extension`
  - `pi-simplify`
  - `@ff-labs/pi-fff`
  - `@quintinshaw/pi-dynamic-workflows`
  - `@narumitw/pi-goal`
  - `pi-fabric`

## What stays local

- `~/.pi/agent/auth.json`
- `~/.pi/agent/trust.json`
- sessions, package caches, runtime model state

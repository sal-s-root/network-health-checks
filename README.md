# Network health checks

## Purpose

Build on shell inspection with Python, DNS, TCP sockets, JSON, and failure handling.

## Run locally

```sh
python3 -m unittest -v
python3 check.py localhost 8080 --timeout 2
```

## Scope and limitations

Python standard library only. The example expects a local service on port 8080. DNS resolution has no total deadline; TCP checks do not verify HTTP behavior.

## Engineering notes

See [LEARNING.md](LEARNING.md) for the design decisions, verification evidence,
and next steps. Never commit credentials, private hostnames, or real incident data.

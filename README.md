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

## Batch checks

Start a local service and run `python3 batch.py examples/targets.json`. The batch is sequential, capped at 100 targets, and validates the whole manifest before probing. Exit 1 means at least one check failed; exit 2 indicates invalid input. DNS can exceed the configured per-connection timeout.

# Engineering notes: Networking and diagnostic tools

## Objective

Build on resource inspection by distinguishing connectivity from service behavior.

## Design decisions

- Emit JSON so downstream tools can consume results without parsing prose.
- Use the standard socket connection helper to support IPv4 and IPv6 destinations.
- Exercise a local listener and a refused connection rather than depend on an external website.

## Verification performed

| Check | Observed result |
|---|---|
| `python3 -m unittest -v` | Passed; exit 0 as expected |

## What the evidence establishes

A TCP handshake does not confirm a healthy application. OS DNS lookup and multiple address attempts mean the timeout is not an overall deadline.

## Next exercise

Add HTTP checks and distinguish resolver, connection, TLS, and application failures in a structured result.

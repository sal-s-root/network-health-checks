#!/usr/bin/env python3
"""DNS and TCP checks with structured output and bounded timeouts."""
import argparse
import json
import socket
import sys
import time

def check(host, port, timeout=3):
    start = time.monotonic()
    result = {"host": host, "port": port, "ok": False}
    try:
        # create_connection handles IPv4 and IPv6; its timeout covers connection attempts.
        with socket.create_connection((host, port), timeout=timeout) as connection:
            result.update(ok=True, peer=connection.getpeername()[0])
    except OSError as error:
        result["error"] = str(error)
    result["elapsed_ms"] = round((time.monotonic() - start) * 1000, 2)
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host")
    parser.add_argument("port", type=int)
    parser.add_argument("--timeout", type=float, default=3)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535 or not args.timeout > 0:
        parser.error("port must be 1-65535 and timeout must be positive")
    result = check(args.host, args.port, args.timeout)
    print(json.dumps(result))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    sys.exit(main())

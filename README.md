# Network diagnostics

Python TCP probes and a validated sequential target manifest for authorized hosts.
Results are JSON, including elapsed connection time and explicit failure details.

```sh
python3 -m unittest -v
python3 check.py localhost 8080 --timeout 2
python3 batch.py examples/targets.json
```

Exit 0 indicates successful checks, 1 a failed connection, and 2 invalid input.
The batch validates all targets before probing and limits a run to 100 targets.
The connection timeout is not an overall DNS or multi-address deadline.

## Troubleshoot by layer

1. Confirm the intended hostname, port, client network, and expected route.
2. Inspect resolution with `getent hosts` or your platform's DNS tooling.
3. Inspect local listeners with `ss -lnt` where available.
4. Run the TCP probe from the affected network.
5. Check HTTP readiness and application behavior separately.

A TCP handshake does not prove TLS trust, authentication, correct HTTP responses,
or service health. This tool does not scan address ranges or change firewall rules.
See [runbook](RUNBOOK.md) and [checks](VALIDATION.md).

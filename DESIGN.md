# Design decisions

TCP connectivity, DNS resolution, and application correctness are separate observations. The batch validates its complete target list before sending probes, runs sequentially, and caps target count. OS DNS resolution is not bounded by the per-connection timeout.

See README.md for operation and VALIDATION.md for the checks actually performed.

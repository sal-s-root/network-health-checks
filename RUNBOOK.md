# Connectivity triage

Check DNS resolution, destination port, route, and firewall rules separately.
A successful TCP connection does not prove the application is healthy.
Compare results from the client network and the server network before changing rules.

DNS resolution uses the OS resolver and may exceed the connection timeout.
Each address attempted can consume a separate timeout; this is not a total deadline.
Only probe hosts you own or are authorized to test.

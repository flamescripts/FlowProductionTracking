# Flow Production Tracking
Script library to assist with Flow Production Tracking (formerly Shotgun/Shotgrid) troubleshooting.

### Flow Production Tracking FQDN Checker
This Python 3 script checks if a list of Fully Qualified Domain Names (FQDNs) can connect to port 443. It uses the FQDNs from the FPT Ecosystem help page and tries to establish a socket connection for each one. The script then shows which FQDNs successfully connected to port 443 and which did not.

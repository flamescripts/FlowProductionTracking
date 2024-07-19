# Flow Production Tracking
Script library to assist with Flow Production Tracking (formerly Shotgun/Shotgrid) troubleshooting.

### Flow Production Combined URL Checker
This Python 3 script checks if a list of Fully Qualified Domain Names (FQDNs), Autodesk Subscription URLs and Autodesk Identity URLs can connect to a port of your selection. It uses the data from the FPT Ecosystem help page, "Which URLs/Protocols need to be allowed for Autodesk Subscription Licensing" page and the "Which URLs/Protocols need to be allowed for Autodesk Identity Manager" help page.  The script attempts to establish a socket connection for each one. The script then shows which URLs successfully connected to the selected port and which did not.  Curl is used for the sitename check.

### Flow Production Tracking FQDN Checker
This Python 3 script checks if a list of Fully Qualified Domain Names (FQDNs) can connect to port 443. It uses the FQDNs from the FPT Ecosystem help page and tries to establish a socket connection for each one. The script then shows which FQDNs successfully connected to port 443 and which did not.

# Flow Production Tracking
Script library to assist with Flow Production Tracking (formerly Shotgun/Shotgrid) troubleshooting.

### Flow Production Combined URL Checker *
This Python 3 script checks if a list of Fully Qualified Domain Names (FQDNs), Autodesk Subscription URLs and Autodesk Identity URLs can connect to a port of your selection. It uses the data from the FPT Ecosystem help page, "Which URLs/Protocols need to be allowed for Autodesk Subscription Licensing" page and the "Which URLs/Protocols need to be allowed for Autodesk Identity Manager" help page.  The script attempts to establish a socket connection for each one. The script then shows which URLs successfully connected to the selected port and which did not.  Curl is used for the sitename check.

### Flow Production Tracking FQDN Checker
This Python 3 script checks if a list of Fully Qualified Domain Names (FQDNs) can connect to port 443. It uses the FQDNs from the FPT Ecosystem help page and tries to establish a socket connection for each one. The script then shows which FQDNs successfully connected to port 443 and which did not.  It does not have the option to check Identity and Subscriptipn URLs.

### Flow Production Tracking API Create User
Creating user accounts with a Python script in the Flow Production Tracking API:
- Replace <XXX> in the below script with your site url and user credentials.
- The auth_token lines can be commented (#) out for Flow sites with 2FA turned off.
	- If removing the auth_token line, also remove the preceeding comma.
- Modify the sg.create string to fit the intended workflow.

# Flow Production Tracking FQDN Checker
Flow Production Tracking "FPT" (formerly known as Shotgrid/Shotgun)

This Python 3 script is designed to validate whether a list of Fully Qualified Domain Names (FQDNs)
can connect to port 443 or not. The script is based on the list of FQDNs referenced in the FPT Ecosystem
help page. Iterating over each FQDN, attempting to establish a socket connection using the Python socket
library. The script displays a list of FQDNs that were able to connect to port 443, as
well as the sites that couldn't.

**Note**: An alternate to using Python to create a socket connection would be to itterate using 

```openssl s_client -connect url:443 -tls1_2```


## Disclaimer

This is not an official Autodesk certified script. Neither the author nor Autodesk are responsible for any
use, misuse, unintended results, or data loss that may occur from using this script. This script has not
been thoroughly tested and is a work in progress. It was created on personal time to address a specific
customer request and may not be applicable to your workflow.

**Use at your own risk.**
This script is intended for providing guidance only. There is no support provided. Caution is strongly
advised as this has not been thoroughly tested.


## Test Environment

- Operating System: macOS 13.6.7, Rocky 9.3, Windows 11


## Installation:
- The script itself should dowloaded or cloned to a path that is accessible to Python3.


## Usage

This script can be ran with or without an argument.  If no argument is provided, the script will prompt for
the Flow site name to replace flow_sitename value in the FQDN list.   


- Example usage without an flow_sitename argument:


   ```python3 flow_fqdn_checker.py```

- Example usage with a flow_sitename argument:

   **Note**: replace flow_sitename with your FPT site name (hostname).


   ```python3 flow_fqdn_checker.py flow_sitename```

## Requirements

- Run as the normal OS user.
- Python 3
- An active Flow Production tracking site.


## Helpful Links

- [Flow Production Tracking: Ecosystem: FQDNs](https://help.autodesk.com/view/SGSUB/ENU/?guid=SG_Administrator_ar_general_security_ar_ecosystem_html)
- [Which URLs/Protocols need to be allowed for Autodesk Subscription Licensing](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/What-URLs-protocols-should-be-accessible-for-Desktop-Subscription-to-work-html.html)
- [Which URLs/Protocols need to be allowed for Autodesk Identity Manager](https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/2GO1P1KDIaLATbYJwgByp6.html)

## Always Current Version

- [FlameScripts on GitHub](https://github.com/flamescripts)

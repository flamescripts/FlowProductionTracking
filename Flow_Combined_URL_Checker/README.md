# Flow Production Tracking Combined URL Checker
Flow Production Tracking "FPT" (formerly known as Shotgrid/Shotgun)

This Python 3 script is designed to validate whether a list of Fully Qualified Domain Names (FQDNs),
Autodesk Subscription URLs and Autodesk Identity URLs can be reached over port 443. The script is
based on the list of FQDNs referenced in the FPT Ecosystem help page, "Which URLs/Protocols need to
be allowed for Autodesk Subscription Licensing" page and the "Which URLs/Protocols need to be allowed
for Autodesk Identity Manager" help page. Iterating over each URL, attempting to establish a socket
connection using the Python socket library. Curl is used for a sitename check.  The script displays
a list of URLs that were able to connect to a selected port, as well as the sites that couldn't.

**Note**: An alternate to using Python to create a socket connection would be to itterate using openssl. 

```openssl s_client -connect url:443 -tls1_2```


## Disclaimer

This script has not been thoroughly tested and is a work in progress.  This script is intended for
providing guidance only. There is no support provided.


## Test Environment

- Operating System: macOS 13.6.7, Rocky 9.3, Windows 11


## Installation:
- The script and dictionary should dowloaded or cloned to a path that is accessible to Python3.
- The URL data comes from the dictionary file ```url_dict.py```.
- The values for ```timeout``` and ```port``` can be modified.


## Usage

This script can be ran with or without an argument.  If no argument is provided AND if running
an FQDN check, the script will prompt for the Flow site name to replace flow_sitename value in the FQDN list.   


- Example usage without an flow_sitename argument:


   ```python3 flow_combined_checker.py```

- Example usage with a flow_sitename argument:


   ```python3 flow_combined_checker.py flow_sitename```
  
   **Note**: Please replace "flow_sitename" with the FPT site name (hostname). Utilizing a sitename argument
  will automatically proceed to the FQDN check, bypassing the subsequent Subscription Licensings and Identity
  Manager URL options.


After launch, validate the URLs/Protocols by selected the corresponding key, "F", "S", or "I".
- 'F' for Flow Production Tracking FQDN
- 'S' for Autodesk Subscription Licensings
- 'I' for Autodesk Identity Manager

## Requirements

- Run as the normal OS user.
- Python 3
- An active Flow Production tracking site.
- ```url_dict.py``` in the same path as ```flow_combined_checker.py```.


## Helpful Links

- [Flow Production Tracking: Ecosystem: FQDNs](https://help.autodesk.com/view/SGSUB/ENU/?guid=SG_Administrator_ar_general_security_ar_ecosystem_html)
- [Which URLs/Protocols need to be allowed for Autodesk Subscription Licensing](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/What-URLs-protocols-should-be-accessible-for-Desktop-Subscription-to-work-html.html)
- [Which URLs/Protocols need to be allowed for Autodesk Identity Manager](https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/2GO1P1KDIaLATbYJwgByp6.html)

## Always Current Version

- [FlameScripts on GitHub](https://github.com/flamescripts)

#!/usr/bin/env python3
#
# 07/19/24
#
# Name: Flow Production Tracking Combined URL Checker
#
# USAGE (FQDN): python3 flow_combined_checker.py flow_sitename
#   Note: replace flow_sitename with your FPT site name.
#
# USAGE (Sub or Identity): python3 flow_combined_checker.py
#
# REQUIRED: 
#   - Run as the normal OS user.
#   - Python 3
#   - An active Flow Production tracking site.
#   - url_dict.py
#
# See README.md for description, disclaimer, other OS usage, testing environments,
# installation notes and caveats.
#
# Always Current Version: https://github.com/flamescripts

import socket
import sys
import os
import subprocess
from url_dict import fqdns, subscription, identity

# Customizable variables
timeout = 5
port = 443

# Check for argument (sitename) , prompt for one if not provided
def validate_sitename():
    if len(sys.argv) > 1:
        flow_sitename = sys.argv[1]
    else:
        flow_sitename = input("\nPlease enter the shotgrid sitename(hostname) and press enter:\n")

    # If FPT sitename is a fqdn, strip out everything but the hostname/subdomain
    if '.' in flow_sitename:
        print(f"\nRenaming sitename from {flow_sitename} to {flow_sitename.split('.')[0]}")
        flow_sitename = flow_sitename.split('.')[0]

    return flow_sitename

# Check if site exists
def check_sites_exist(flow_sitename, fqdns):
    shotgrid_url = "https://" + fqdns['Flow Production Tracking'][0]
    shotgunstudio_url = "https://" + fqdns['Flow Production Tracking'][1]

    sitename_exists = False

    for url in shotgrid_url, shotgunstudio_url:
        try:
            # Run curl to check sitename existence
            command = f"curl -Is {url}"
            output = subprocess.check_output(command, shell=True).decode()

            # Split output into lines and grab the status code on first line, after the first space
            lines = output.split('\n')
            status_line = lines[0]
            status_code = int(status_line.split(' ')[1])

            if status_code in (200, 301, 302):
                sitename_exists = True
        except (subprocess.CalledProcessError, IndexError, ValueError):
            print(f"Error: Could not connect to {url}.")

    if sitename_exists:
        print(f"* sitename {flow_sitename} found.")
    else:
        print(f"Error: The sitename {flow_sitename} does not exist or is accessible.")
        sys.exit()

# Print connection status of url
def print_connection_status(url, socket_result):
    if socket_result:
        print(f"   - {url} (\033[1mCONNECTED\033[0m)")
    else:
        print(f"   - {url} (\033[1m*UNABLE TO CONNECT*\033[0m)")

# Checks if a socket connection can be established with the url/port.
def test_socket_connection(url):
    print(f"  Testing connection for {url} port {port}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((url, port))
        if result == 0:
            print(f"   - Connection successful.")
            return True
        else:
            print(f"   - Connection attempt failed.")
            return False
    except socket.gaierror:
        print(f"* {url} is an invalid Flow sitename/hostname.")
        return False
    finally:
        sock.close()

# Add URL to successful_urls list if connection successsful, if connection fails add to failed_urls list.
def check_urls(url_dict):
    # Init the lists
    successful_urls = []
    failed_urls = []

    for key, urls in url_dict.items():
        print(f"\n+Checking {key} list:\n")
        for url in urls:
            socket_result = test_socket_connection(url)
            print_connection_status(url, socket_result)
            (successful_urls if socket_result else failed_urls).append(url)

    return successful_urls, failed_urls

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Flow Production Tracking URL Checker")

    if len(sys.argv) > 1:
        check_type = 'F'
    else:
        # Ask the user what type of check they would like to perform
        check_type = input("\nPlease select from the following options to to validate the URLs/Protocols nedded:\n 'F' for Flow Production tracking FQDN\n 'S' for Autodesk Subscription Licensings\n 'I' for Autodesk Identity Manager URLs/Protocols:\n").upper()

    if check_type == 'F':
        # FQDN check
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Flow Production Tracking FQDN Checker")
        flow_sitename = validate_sitename()

        # Add dynamic URLs to the fqdns dictionary
        fqdns['Flow Production Tracking'] = [
            f"{flow_sitename}.shotgrid.autodesk.com",
            f"{flow_sitename}.shotgunstudio.com",
        ] + fqdns['Flow Production Tracking']

        print(f"\nChecking if sitename {flow_sitename} exists")
        check_sites_exist(flow_sitename, fqdns)
        successful_urls, failed_urls = check_urls(fqdns)

    elif check_type == 'S':
        # Subscription check
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Flow Production Tracking Subscription URL Checker")
        successful_urls, failed_urls = check_urls(subscription)

    elif check_type == 'I':
        # Identity check
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Flow Production Tracking Identity manager Checker")
        successful_urls, failed_urls = check_urls(identity)

    else:
        print("Invalid selection. Please enter either 'F', 'S', or 'I'.")
        return

    print(f"\n\n\033[1mThe following URLs can connect to port {port} \033[0m")
    for url in successful_urls:
        print(url)

    if failed_urls:
        print(f"\n\n\033[1mThe following URLs were unable to connect to port {port} \033[0m")
        for url in failed_urls:
            print(url)

    print("\nScript Complete. Please upload these results to your Autodesk support case.\n")

if __name__ == "__main__":
    main()

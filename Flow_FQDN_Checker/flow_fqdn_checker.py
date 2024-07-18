#!/usr/bin/env python3
#
# 07/18/24
#
# Name: Flow Production Tracking FQDN Checker
#
# USAGE: python3 flow_fqdn_checker.py flow_sitename
#   Note: replace flow_sitename with your FPT site name.
#
# REQUIRED: 
#   - Run as the normal OS user.
#   - Python 3
#   - An active Flow Production tracking site.
#
# See README.md for description, disclaimer, other OS usage, testing environments,
# installation notes and caveats.
#
# Always Current Version: https://github.com/flamescripts

import socket
import sys
import os
import subprocess

# Customizable variables
timeout = 10
port = 443

# Check if any arguments were passed from command line, if not capture that input
def validate_sitename():
    
    if len(sys.argv) > 1:
        flow_sitename = sys.argv[1]
    else:
        flow_sitename = input("\nNo argument provided.  Please enter the shotgrid sitename(hostname) and press enter:\n")

    # If FPT sitename is a fqdn, strip out everything but the hostname/subdomain
    if '.' in flow_sitename:
        print(f"\nRenaming sitename from {flow_sitename} to {flow_sitename.split('.')[0]}")
        flow_sitename = flow_sitename.split('.')[0]

    return flow_sitename


# Check if site exists, if not exit
def check_sites_exist(flow_sitename, fqdns):
    shotgrid_url = "https://" + fqdns['Flow Production Tracking'][0]
    shotgunstudio_url = "https://" + fqdns['Flow Production Tracking'][1]

    sitename_exists = False

    for url in shotgrid_url, shotgunstudio_url:
        try:
            # Run curl command and get output
            command = f"curl -Is {url}"
            output = subprocess.check_output(command, shell=True).decode()

            # Split output into lines
            lines = output.split('\n')

            # The status code is in the first line, after the first space
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

# Output connection status of url
def print_connection_status(url, socket_result):
    if socket_result:
        print(f"   - {url} (\033[1mCONNECTED\033[0m)")
    else:
        print(f"   - {url} (\033[1m*UNABLE TO CONNECT*\033[0m)")

# Checks if a socket connection can be established.
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

def main():
    # Start fresh
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Flow Production Tracking FQDN Checker")
    
    flow_sitename = validate_sitename()
    
    fqdns = {
        'Flow Production Tracking': [
            f"{flow_sitename}.shotgrid.autodesk.com",
            f"{flow_sitename}.shotgunstudio.com",
            "launchdarkly.shotgrid.autodesk.com"
        ],
        'Flow Production Tracking Create': [
            "sg-software.ems.autodesk.com",
            "sg-sec.s3-accelerate.amazonaws.com"
        ],
        'Flow Production Tracking RV': [
            "sg-software.ems.autodesk.com"
        ],
        'AWS S3': [
            "sg-media-usor-01.s3.amazonaws.com",
            "sg-media-tokyo.s3.amazonaws.com",
            "sg-media-ireland.s3.amazonaws.com",
            "sg-media-saopaulo.s3.amazonaws.com",
            "sg-media-mumbai.s3.amazonaws.com",
            "sg-media-sydney.s3.amazonaws.com"
        ],
        'AWS S3 accelerated': [
            "sg-media-usor-01.s3-accelerate.amazonaws.com",
            "sg-media-tokyo.s3-accelerate.amazonaws.com",
            "sg-media-ireland.s3-accelerate.amazonaws.com",
            "sg-media-saopaulo.s3-accelerate.amazonaws.com",
            "sg-media-mumbai.s3-accelerate.amazonaws.com",
            "sg-media-sydney.s3-accelerate.amazonaws.com"
        ],
        'Toolkit App Store': [
            "tank.shotgunstudio.com",
            "s3-proxy.shotgrid.autodesk.com",
            "s3-proxy.shotgunstudio.com"
        ],
        'Analytics': [
            "api.amplitude.com"
        ]
    }

    successful_urls = []
    failed_urls = []

    print(f"\nChecking if sitename {flow_sitename} exists")
    check_sites_exist(flow_sitename,fqdns)

    for fqdn, urls in fqdns.items():
        print(f"\nChecking {fqdn} FQDN list:\n")
        for url in urls:
            socket_result = test_socket_connection(url)
            print_connection_status(url, socket_result)
            (successful_urls if socket_result else failed_urls).append(url)

    print(f"\n\n\033[1mThe following URLs can connect to port {port} \033[0m")
    for url in successful_urls:
        print(url)

    if failed_urls:
        print(f"\n\n\033[1mThe following URLs were unable to connect to port {port} \033[0m")
        for url in failed_urls:
            print(url)

    print("\nScript Complete.  Please upload these results to your Autodesk support case/\n")
	
if __name__ == "__main__":
    main()

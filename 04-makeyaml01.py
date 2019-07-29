#!/usr/bin/python3

import yaml

def main():
    
    # Create a list of dictionaries
    vcp = [{"service": "compute", "app": "nova"}, {"service": "network", "app": "neutron"}, {"service": "block", "app": "cinder"}]

    print(vcp)
    
    # creates a file to write out to called vcp.yaml
    with open("vcp.yaml", "w") as vcpyaml:
        # yaml has not DUMPS just dump
        yaml.dump(vcp, vcpyaml)

main()
   

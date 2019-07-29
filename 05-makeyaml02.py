#!/usr/bin/python3

import yaml
import json

def main():
    with open("vcp.yaml", "r") as vcp:
        pyyammy = yaml.load(vcp)

    pyyammy.append({"service": "identity", "app": "keystone"})

    print(pyyammy)

    with open("vcp.json", "w") as vcpjson:
        json.dump(pyyammy, vcpjson)
        



main()

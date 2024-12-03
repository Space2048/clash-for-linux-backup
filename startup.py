#!/usr/bin/python3

#config
subaddr = "https://sub.xfltd.bond/api/v1/client/subscribe?token=7995e48c713c9671928b27ba96f86b73"
extendNode = []
extendNode.extend(
    {
        
    }
)


import subprocess
import requests
import os
import base64

def download_subfile(addr, file_dir):
    headers = {
            'User-Agent': 'curl/7.64.1'
    }
    
    response = requests.get(addr, headers=headers)
    if response.status_code == 200:
        content = response.text
        with open(file_dir, "w") as f:
            f.write(base64.b64decode(content).decode("utf-8"))
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

def convert_subfile(file_dir):
    convertProgram = "./tools/subconverter/subconverter"
    stdin, stderr = subprocess.run([convertProgram, "-f", "clash", "-g", "-s", file_dir, "-o", file_dir])
    print(stdin, stderr)
    pass

if __name__ == "__main__":
    #download_subfile(subaddr, "test.yaml")
    convert_subfile("/data/Code/github_project/clash-for-linux-backup/test.yaml")


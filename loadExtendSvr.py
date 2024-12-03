import yaml
import sys
import os

servers= [
    {'name': 'CN_2', 'server': '45.87.103.89', 'port': 6498, 'type': 'vmess', 'password': '2e4a49ef-9780-4f99-aeb8-03171532ce69', 'uuid': '1bac81e1-6051-42d9-8e31-5e7c1680eb33', 'alterId': 0, 'network': 'tcp'}
]

if len(sys.argv) < 2:
    print("lack config file name")
file=sys.argv[1]
if not os.path.exists(file):
    print("Not Found Config File!")
    exit()

with open(file, "r+") as f:
    data = yaml.safe_load(f.read())
    for newNode in servers:
        for node in data['proxies']:
            if newNode['name'] == node['name']:
                continue
        data['proxies'].append(newNode)
    updated_yaml_content = yaml.dump(data, default_flow_style=False)
    f.write(updated_yaml_content)

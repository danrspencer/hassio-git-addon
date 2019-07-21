#!/usr/bin/env python3

import json
import os
import yaml

config_path = "/config"
options_path = "/data/options.json"
secrets_path = "/config/secrets.yaml"

ssh_key_path = "/root/.ssh/id_rsa"

os.chdir(config_path)

with open(options_path, 'r') as stream:
    options_json = stream.read()
    options = json.loads(options_json)

with open(secrets_path, 'r') as stream:
    try:
        secrets = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

with open(ssh_key_path, 'w') as stream:
    stream.write(secrets["git_ssh"])
    os.chmod(ssh_key_path, 0o600)

print(secrets)


# git_status = os.popen("git status --porcelain").read()

# if len(git_status) > 0:
#     os.system("git commit -m 'Auto commit from hassio-git...'; git push")

#!/usr/bin/env python3

import json
import os
import sys
import time
import yaml

import subprocess
from subprocess import call, check_output

config_path = "/config"
options_path = "/data/options.json"
secrets_path = "/config/secrets.yaml"


def load_options():
    with open(options_path, 'r') as stream:
        options_json = stream.read()
        options = json.loads(options_json)

    return options


def setup_ssh():
    ssh_key_path = "/root/.ssh/id_rsa"
    known_hosts_path = "/root/.ssh/known_hosts"

    with open(secrets_path, 'r') as stream:
        try:
            secrets = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    with open(ssh_key_path, 'w', encoding='utf-8') as stream:
        stream.write(secrets["git_ssh"])

    os.chmod(ssh_key_path, 0o600)

    known_hosts = check_output(
        ["ssh-keyscan", "github.com"]).decode(sys.stdout.encoding)

    with open(known_hosts_path, 'w', encoding='utf-8') as stream:
        stream.write(known_hosts)


def clone_remote(repository):
    os.chdir(config_path)

    try:
        remotes = check_output(["git", "remote", "-v"]
                               ).decode(sys.stdout.encoding)
    except:
        remotes = ""

    if repository not in remotes:
        print("Checking out {}".format(repository))
        call(["git", "init"])
        call(["git", "remote", "add", "origin", repository])
        call(["git", "fetch"])
        call(["git", "reset", "--hard", "origin/master"])
        call(["git", "branch", "--set-upstream-to", "origin/master"])
        call(["git", "submodule", "update", "--init", "--recursive"])
    else:
        print("Repository already checked out.")


def setup_git():
    call(["git", "config", "--global", "user.email", "git-hassio@git-hassio"])
    call(["git", "config", "--global", "user.name", "git-hassio"])


def check_remote():
    call(["git", "fetch"])


def check_local():
    if check_output(["git", "status", "--porcelain"]):
        call(["git", "add", "-A"])
        call(["git", "commit", "-m", "Auto commit from hassio-git"])
    else:
        print("No local changes.")

    if "branch is ahead" in check_output(["git", "status", "--ahead-behind"]).decode(sys.stdout.encoding):
        call(["git", "push"])


def update_from_remote():
    call(["git", "submodule", "update", "--init", "--recursive"])
    # hass -c . --script check_config


options = load_options()
setup_ssh()
setup_git()

clone_remote(options['repository'])

while True:
    check_local()
    time.sleep(10)

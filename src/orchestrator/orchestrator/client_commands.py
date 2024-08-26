# Copyright 2023 Reply S.p.A. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
This module is used as client for the server_commands.
"""

# sys modules
import requests

# external modules
#  -

# local modules
# -

# local vars
HOST = '127.0.0.1'
BASE_URL = 'http://'+HOST+':1992/api/'
API_USER_COMMANDS = BASE_URL + 'userCommands'


class ClientCommands:

    def retrieve_user_command(self):
        result = requests.get(API_USER_COMMANDS, timeout=5)
        user_command = result.json()['user_command']
        return user_command

    def publish_user_command(self, user_command):
        payload = {'user_command': user_command}
        requests.post(API_USER_COMMANDS, json=payload, timeout=5)


if __name__ == "__main__":
    client_commands = ClientCommands()
    user_command = client_commands.retrieve_user_command()
    print(user_command)

# Copyright 2024 Reply S.p.A. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
This module is used as exchange to let agents talks with external agents.
Here two APIs are exposed:
- POST publish_user_command
- GET retrieve_user_command
"""

# sys modules
import logging

# external modules
from flask import Flask, request, jsonify, abort

# local modules
# -

# local vars
SERVER_NAME = "server_commands"
app = Flask(SERVER_NAME)
list_user_commands = []


@app.route('/api/userCommands', methods=['GET'])
def retrieve_user_command():
    """
    This API is used by internal agents to read user commands
    """
    global list_user_commands

    # Prepare the response with the next user command if available
    user_command = list_user_commands.pop(0) if list_user_commands else None

    return jsonify({"user_command": user_command})


@app.route('/api/userCommands', methods=['POST'])
def publish_user_command():
    """
    This API is used by external services to publish user commands.
    """
    global list_user_commands

    if 'user_command' in request.json:
        user_command = request.json['user_command']
        list_user_commands.append(user_command)
        return "Command Published!"
    else:
        return jsonify({"error": "user_command parameter is missing"}), 400


def run_server():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='0.0.0.0', port=1992)
    exit(1)


if __name__ == "__main__":
    run_server()

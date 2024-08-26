# Copyright 2024 Reply S.p.A. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
This agent is used to emulate the Alarm Service
"""

# sys modules
# -

# external modules
# -

# local modules
from orchestrator.client_commands import ClientCommands

# local vars
AGENT_NAME = "agent_alarm"


def play():

    client_commands = ClientCommands()
    user_command = "Go to door1 on seconds floor, give me the images"
    client_commands.publish_user_command(user_command=user_command)
    print(user_command)


if __name__ == "__main__":
    print(f'START {AGENT_NAME}')
    play()

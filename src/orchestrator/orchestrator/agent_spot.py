# Copyright 2024 Reply S.p.A. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
This agent is used to control actions on SPOT.
"""

# sys modules
import time
import traceback

# external modules
# -

# local modules
from orchestrator.client_commands import ClientCommands

# local vars
AGENT_NAME = "agent_spot"


def play():

    client_commands = ClientCommands()

    try:
        while True:

            # READ commands
            user_command = client_commands.retrieve_user_command()

            # IF command execute it els print no command
            if user_command:
                print(f'AGENT:{AGENT_NAME} EXECUTE command: {user_command}')
            else:
                print(f'AGENT:{AGENT_NAME} No command to execute')

            time.sleep(5)

    except Exception as x1:
        print(x1)
        # Print the stack trace of the exception
        traceback.print_exc()
        print('exception captured!')
        time.sleep(3)


if __name__ == "__main__":
    print(f'START {AGENT_NAME}')
    play()

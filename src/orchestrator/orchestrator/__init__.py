# Copyright 2024 Reply S.p.A. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
The orchestrator package structure consists of:
- agent_x.py: this family of modules are agents that read commands from server_y and execute them. They can also write messages to server_y that will be read by other agents inside the package or external agents on another network.
- server_y.py: these modules are REST servers that expose APIs that will be used by agents inside the package or external agents to communicate;
- client_y.py: these modules are used as client that have the API REST calls to the respective server_y.
"""

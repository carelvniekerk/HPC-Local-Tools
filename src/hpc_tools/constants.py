# --------------------------------------------------------------------------------
# Project: HPC Local Tools
# Author: Carel van Niekerk, Benjamin Ruppik
# Year: 2025
# Group: Dialogue Systems and Machine Learning Group
# Institution: Heinrich Heine University Düsseldorf
# --------------------------------------------------------------------------------
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License."

import os
import random
import re
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from enum import StrEnum, auto


class HPCSystem(StrEnum):
    """HPC systems available for the user."""

    HILBERT = "HILBERT"
    NOCTUA2 = "NOCTUA2"
    LAMARR = "LAMARR"


class NodeType(StrEnum):
    """Node types available for the user."""

    LOGIN = auto()
    STORAGE = auto()


def get_node(
    hpc_system: HPCSystem = HPCSystem.HILBERT,
    node_type: NodeType = NodeType.LOGIN,
) -> str:
    """Get the login node for the given HPC system."""
    regex_pattern: str = r"^(.*)\[(\d+)-(\d+)\]$"
    login_node: str = os.environ.get(f"{hpc_system}_{node_type}_NODE".upper(), "")
    match: re.Match[str] | None = re.search(regex_pattern, login_node)
    if match:
        prefix, start, end = match.groups()
        node_id: int = random.choice(range(int(start), int(end) + 1))  # noqa: S311
        login_node = f"{prefix}{node_id}"
    return login_node


def get_username(hpc_system: HPCSystem = HPCSystem.HILBERT) -> tuple[str, str]:
    """Get the username for the given HPC system."""
    username: str = os.environ.get(f"{hpc_system}_USERNAME".upper(), "")
    if not username:
        msg = f"{hpc_system.value.upper()}_USERNAME environment variable not set."
        raise ValueError(msg)
    remote_base_path: str = os.environ.get(
        f"{hpc_system}_REMOTE_BASE".upper(),
        f"/gpfs/project/{username}/src",
    )

    return username, remote_base_path


if __name__ == "__main__":
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--hpc_name",
        type=HPCSystem,
        default=HPCSystem.HILBERT,
        help="HPC system to use.",
    )
    hpc_system: HPCSystem = parser.parse_args().hpc_name

    login_node: str = get_node(hpc_system=hpc_system, node_type=NodeType.LOGIN)
    storage_node: str = get_node(hpc_system=hpc_system, node_type=NodeType.STORAGE)
    username, remote_base_path = get_username(hpc_system=hpc_system)

    print(f'export HPC_TOOLS_LOGIN_NODE="{login_node}"')
    print(f'export HPC_TOOLS_STORAGE_NODE="{storage_node}"')
    print(f'export HPC_TOOLS_USERNAME="{username}"')
    print(f'export HPC_TOOLS_REMOTE_BASE="{remote_base_path}"')

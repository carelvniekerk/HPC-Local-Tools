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


def get_node(hpc_system: str = "HILBERT", node_type: str = "LOGIN") -> str:
    """Get the login node for the given HPC system."""
    regex_pattern: str = r"^(.*)\[(\d+)-(\d+)\]$"
    login_node: str = os.environ.get(f"{hpc_system}_{node_type}_NODE", "")
    match: re.Match[str] | None = re.search(regex_pattern, login_node)
    if match:
        prefix, start, end = match.groups()
        print(prefix, start, end)
        node_id: int = random.choice(range(int(start), int(end) + 1))  # noqa: S311
        login_node = f"{prefix}{node_id}"
    return login_node


LOGIN_NODE = get_node("HILBERT", "LOGIN")
STORAGE_NODE = get_node("HILBERT", "STORAGE")

ZIM_USERNAME = os.environ.get(
    "HILBERT_USERNAME",
    "",
)
if not ZIM_USERNAME:
    msg = "HILBERT_USERNAME environment variable not set."
    raise ValueError(msg)

REMOTE_BASE = os.environ.get(
    "HILBERT_REMOTE_BASE",
    f"/gpfs/project/{ZIM_USERNAME}/src",
)

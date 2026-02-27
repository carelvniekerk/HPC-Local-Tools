# coding=utf-8
# --------------------------------------------------------------------------------
# Project: HPC Local Tools
# Author: Carel van Niekerk
# Year: 2024
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

import subprocess
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from pathlib import Path

from hpc_tools.constants import HPCSystem, NodeType, get_node, get_username


def sync_results() -> None:
    """Sync the project with the remote storage node."""
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--hpc_name",
        help="HPC System",
        default=HPCSystem.HILBERT,
        type=HPCSystem,
    )
    hpc_system: HPCSystem = parser.parse_args().hpc_name
    storage_node: str = get_node(hpc_system, NodeType.STORAGE)
    _, remote_base = get_username(hpc_system)
    local_dir = Path.cwd()

    # Results sync directories
    results_list = local_dir / ".rsync-results"

    # Sync local directory with remote directory, excluding .venv
    print("Synchronizing results...")
    sync_dirs: list[str] = []
    if results_list.exists():
        with results_list.open() as f:
            sync_dirs += [
                line.strip() for line in f if line.strip() and "#" not in line
            ]

    rsync_commands: list[list[str]] = [
        [
            "rsync",
            "-avz",
            f"{storage_node}:{remote_base}/{local_dir.name}/{dir_name}",
            f"{Path(dir_name).parent}/",
        ]
        for dir_name in sync_dirs
    ]

    for cmd in rsync_commands:
        try:
            subprocess.run(cmd, check=True)  # noqa: S603
        except subprocess.CalledProcessError as err:
            msg = f"Error during rsync: {err}"
            raise RuntimeError(msg) from err


if __name__ == "__main__":
    sync_results()

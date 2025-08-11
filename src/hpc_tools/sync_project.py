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


def sync_project() -> None:
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

    local_dir: Path = Path.cwd()

    # Check if there is a exclude file in the local directory
    exclude_file = local_dir / ".rsync-exclude"

    exclude_args = [
        "--exclude",
        ".venv",
        "--exclude",
        "poetry.lock",
    ]
    if exclude_file.exists():
        exclude_args += ["--exclude-from", str(exclude_file)]

    # Sync local directory with remote directory, excluding .venv
    rsync_command = [
        "rsync",
        "-avz",
        "--delete",
        *exclude_args,
        str(local_dir),
        f"{storage_node}:{remote_base}/",
    ]

    try:
        print("Synchronizing files...")
        subprocess.run(rsync_command, check=True)  # noqa: S603
    except subprocess.CalledProcessError as err:
        msg = f"Error during rsync: {err}"
        raise RuntimeError(msg) from err


if __name__ == "__main__":
    sync_project()

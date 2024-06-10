# coding=utf-8
# --------------------------------------------------------------------------------
# Project: Training Project
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

import os
import subprocess
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

USER_NAME = "niekerk"
STORAGE_NODE = "Hilbert-Storage"
REMOTE_BASE = f"/gpfs/project/{USER_NAME}/src"


def sync_project():
    local_dir = os.getcwd()

    # Sync local directory with remote directory, excluding .venv
    print("Synchronizing files...")
    rsync_command = [
        "rsync",
        "-avz",
        "--progress",
        "--exclude",
        ".venv",
        "--exclude",
        "poetry.lock",
        local_dir,
        f"{STORAGE_NODE}:{REMOTE_BASE}/",
    ]
    try:
        subprocess.run(rsync_command, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error during rsync: {e}")


if __name__ == "__main__":
    sync_project()

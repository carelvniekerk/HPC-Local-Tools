# --------------------------------------------------------------------------------
# Project: HPC Local Tools
# Author: Carel van Niekerk, Benjamin Ruppik
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

LOGIN_NODE = "Hilbert"
STORAGE_NODE = "Hilbert-Storage"

ZIM_USERNAME = os.environ.get(
    "ZIM_USERNAME",
    "",
)
if not ZIM_USERNAME:
    msg = "ZIM_USERNAME environment variable not set."
    raise ValueError(msg)

REMOTE_BASE = os.environ.get(
    "ZIM_REMOTE_BASE",
    f"/gpfs/project/{ZIM_USERNAME}/src",
)

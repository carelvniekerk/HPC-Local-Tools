# coding=utf-8
# --------------------------------------------------------------------------------
# Project: HPC Local Tools
# Author: Benjamin Matthias Ruppik
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
# limitations under the License.

"""Extract job IDs from the output of the `qs` command."""

import re

qs_output = """
11625522.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625523.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625524.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625525.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625526.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625527.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625529.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625530.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625531.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625532.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625533.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625534.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625535.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625536.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625537.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625538.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625539.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625540.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625541.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --                                                                                                                                                                
11625542.hpc-batch   ruppik   DSML     compute_p*    --    1   4   32gb 36:00 Q   --
"""


def extract_job_ids(
    qs_output: str,
) -> str:
    # Use regular expression to find all job numbers
    job_numbers = re.findall(
        r"^\d+",
        qs_output,
        re.MULTILINE,
    )

    # Join the numbers with a space
    result = " ".join(job_numbers)

    return result


def main() -> None:
    result = extract_job_ids(qs_output)

    print(result)


if __name__ == "__main__":
    main()

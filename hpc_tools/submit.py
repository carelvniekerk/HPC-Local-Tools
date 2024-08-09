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
# limitations under the License.

"""Submit a job to the cluster."""

import pathlib
import subprocess
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from pathlib import Path

from constants import LOGIN_NODE, REMOTE_BASE


def get_submission_command() -> str:
    """Get the command to submit the job to the cluster."""
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--job_name", help="Job Name", default="", type=str)
    parser.add_argument(
        "-s",
        "--job_script",
        help="Path to job script",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-a",
        "--job_script_args",
        help="Arguments for the job script",
        default="",
        type=str,
    )

    parser.add_argument("--template", help="Job Queue", default="")
    parser.add_argument("--queue", help="Job Queue", default="DSML")
    parser.add_argument("--ncpus", help="Number of CPUs", default=2, type=int)
    parser.add_argument("--memory", help="Amount of memory in GB", default=32, type=int)
    parser.add_argument("--ngpus", help="Number of GPUs", default=1, type=int)
    parser.add_argument("--accelerator_model", help="GPU model", default=None)
    parser.add_argument(
        "--walltime",
        help="Walltime in format hh:mm:ss, eg 08:00:00",
        default="36:00:00",
        type=str,
    )
    args = parser.parse_args()

    job_script_path = pathlib.Path(
        REMOTE_BASE,
        Path.cwd().name,
        args.job_script,
    )

    command = [
        "submit_job",
        "-n",
        args.job_name,
        "-s",
        str(job_script_path),
        "--ncpus",
        str(args.ncpus),
        "--memory",
        str(args.memory),
        "--ngpus",
        str(args.ngpus),
        "--walltime",
        args.walltime,
    ]

    if args.job_script_args:
        command.extend(["-a", f'"{args.job_script_args}"'])
    if args.template:
        command.extend(["--template", args.template])
    if args.queue:
        command.extend(["--queue", args.queue])
    if args.accelerator_model:
        command.extend(["--accelerator_model", args.accelerator_model])

    command = " ".join(command)
    return f"bash -ci 'base && home && {command}'"


def submit() -> None:
    """Submit the job via SSH."""
    print("Submitting job...")
    command = get_submission_command()
    print(command)
    ssh_command = ["ssh", "-t", LOGIN_NODE, command]
    try:
        subprocess.run(ssh_command, check=True)  # noqa: S603
    except subprocess.CalledProcessError as err:
        msg = f"Error during submission: {err}"
        raise RuntimeError(msg) from err

    print("Job submitted successfully.")


if __name__ == "__main__":
    submit()

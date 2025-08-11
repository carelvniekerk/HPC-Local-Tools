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

from hpc_server_tools.vm_templates import JOB_DEFAULTS, templates
from hpc_server_tools.vm_templates.types import (
    AcceleratorModel,
    HPCQueue,
)

from hpc_tools.constants import HPCSystem, NodeType, get_node, get_username


def get_submission_command() -> tuple[str, str]:
    """Get the command to submit the job to the cluster."""
    template_list: list[str] = list(templates.__all__)
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

    parser.add_argument(
        "--template",
        help=f"Machine Template. Options: {' '.join(template_list)}",
        default="",
    )
    parser.add_argument(
        "--queue",
        help="Job Queue",
        default=JOB_DEFAULTS.queue,
        type=HPCQueue,
    )
    parser.add_argument(
        "--ncpus",
        help="Number of CPUs",
        default=JOB_DEFAULTS.num_cpus,
        type=int,
    )
    parser.add_argument(
        "--memory",
        help="Amount of memory in GB",
        default=JOB_DEFAULTS.memory,
        type=int,
    )
    parser.add_argument(
        "--ngpus",
        help="Number of GPUs",
        default=JOB_DEFAULTS.num_gpus,
        type=int,
    )
    parser.add_argument(
        "--accelerator_model",
        help="GPU model",
        default=JOB_DEFAULTS.accelerator_model,
        type=AcceleratorModel,
    )
    parser.add_argument(
        "--walltime",
        help="Walltime in format hh:mm:ss, eg 08:00:00",
        default=JOB_DEFAULTS.walltime,
        type=str,
    )
    parser.add_argument(
        "--hpc_name",
        help="HPC System",
        default=HPCSystem.HILBERT,
        type=HPCSystem,
    )
    args = parser.parse_args()

    hpc_system: HPCSystem = args.hpc_name
    login_node: str = get_node(hpc_system, NodeType.LOGIN)
    _, remote_base = get_username(hpc_system)

    job_script_path = pathlib.Path(
        remote_base,
        Path.cwd().name,
        args.job_script,
    )

    if args.walltime.startswith('"') and args.walltime.endswith('"'):
        args.walltime = args.walltime[1:-1]

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
        f"--walltime={args.walltime}",
        # f'\\"{args.walltime}\\"',
    ]

    if args.job_script_args:
        args.job_script_args = args.job_script_args.replace('"', '\\"')
        command.extend(["-a", f'"{args.job_script_args}"'])
    if args.template:
        command.extend(["--template", args.template])
    if args.queue:
        command.extend(["--queue", args.queue])
    if args.accelerator_model:
        command.extend(["--accelerator_model", args.accelerator_model])

    command_str: str = " ".join(command)
    return f"bash -ci 'base && home && {command_str}'", login_node


def submit() -> None:
    """Submit the job via SSH."""
    print("Submitting job...")
    command, login_node = get_submission_command()
    print(command)
    ssh_command = ["ssh", "-t", login_node, command]
    try:
        subprocess.run(ssh_command, check=True)  # noqa: S603
    except subprocess.CalledProcessError as err:
        msg = f"Error during submission: {err}"
        raise RuntimeError(msg) from err

    print("Job submitted successfully.")


if __name__ == "__main__":
    submit()

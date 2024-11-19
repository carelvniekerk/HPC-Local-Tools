# HPC Local Tools

This repository contains a collection of tools that are useful for HPC users.
The tools are written in Python and Bash.
The tools are designed to be used on a local machine, not on the HPC cluster itself.
The tools are designed to help users manage their data and jobs on the HPC cluster.

## Installation

The user is required to first install the cluster tools on the HPC cluster.

The local tools can be installed using oh-my-zsh by simply cloning the repository into the `~/.hpc_tools` directory and creating a symbolic link plugin in the `~/.oh-my-zsh/plugins` directory.

```sh
# Clone the repository
git clone git@gitlab.cs.uni-duesseldorf.de:dsml/hpc-local-tools.git ~/.hpc_tools
ln -s ~/.hpc_tools/plugin ~/.oh-my-zsh/plugins/hpc
```

Or by adding the following to the `.zshrc` file:

```sh
# Configure HPC Tools
export HPC_TOOLS_DIR="${HOME}/.hpc_tools"
export PATH="${HPC_TOOLS_DIR}:${PATH}"
```

Then activate the plugin in the `.zshrc` file by adding `hpc` to the `plugins` array:

```sh
# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git hpc)
```

To create a python virtual environment for the local tools, run the following commands:

```sh
poetry install
```

## Additional setup

### ssh config

The python scripts use the variables `LOGIN_NODE = "Hilbert"` and `STORAGE_NODE = "Hilbert-Storage"` to determine the login and storage nodes of the HPC cluster.
For this to work, you need to add the following to your `~/.ssh/config` file.
Replace `ZIM_USERNAME` with your username on the HPC cluster and also see the instructions for setting the environment variables below.

```sh
Host *
    UseKeychain yes

Host Hilbert*
    User ZIM_USERNAME
    Port 22

Host Hilbert
    HostName hpc.rz.uni-duesseldorf.de

Host Hilbert-Storage
    HostName storage.hpc.rz.uni-duesseldorf.de
```

### Environment variables

Set the environment variable `ZIM_USERNAME` to your username on the HPC cluster, for example by adding the following to the `.zshrc` file:

```sh
export ZIM_USERNAME="your_zim_username" # e.g. "niekerk" or "ruppik"
```

Optionally, if you use a custom folder structure on the HPC cluster, you can set the remote base directory to which the sync_project command will sync the project files.
For example, if you have your project code in a folder `/gpfs/project/your_zim_username/git-source` on the HPC cluster, you can set the following environment variable:

```sh
export ZIM_REMOTE_BASE="/gpfs/project/$ZIM_USERNAME/git-source"
```

See the python script `hpc_tools/constants.py` for the default values which will be used if the environment variables are not set.

For syncing the HPC log files to the local machine, you need to set the following environment variables on the local machine:

```bash
JOB_LOGS_LOCAL_DIR
JOB_LOGS_BACKUP_LOCAL_DIR
```

## Contributors

- [Carel van Niekerk](https://gitlab.cs.uni-duesseldorf.de/niekerk), <niekerk@hhu.de>
- [Benjamin Ruppik](https://gitlab.cs.uni-duesseldorf.de/ruppik), <mail@ruppik.net>

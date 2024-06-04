# HPC Local Tools

This repository contains a collection of tools that are useful for HPC users. The tools are written in Python and Bash. The tools are designed to be used on a local machine, not on the HPC cluster itself. The tools are designed to help users manage their data and jobs on the HPC cluster.

## Installation
The user is required to first install the cluster tools on the HPC cluster.

The local tools can be installed using oh-my-zsh by simply cloning the repository into the `~/.hpc_tools` directory and creating a symbolic link plugin in the `~/.oh-my-zsh/plugins` directory.

```sh
# Clone the repository
git clone TODO ~/.hpc_tools
ln -s ~/.hpc_tools/plugin ~/.oh-my-zsh/plugins/hpc
```

Or by adding the following to the `.zshrc` file:

```sh
# Configure HPC Tools
export HPC_TOOLS_DIR="${HOME}/.hpc_tools"
export PATH="${HPC_TOOLS_DIR}:${PATH}"
```

fpath=($HOME/.oh-my-zsh/plugins/hpc_tools $fpath)

# Configure HPC Tools
export HPC_TOOLS_DIR="${HOME}/.hpc_tools"
export PATH="${HPC_TOOLS_DIR}:${PATH}"

# Shorthand Aliases
alias hrun="hpc run"
alias hs="hpc status"
alias hqi="hpc qi"
alias hcl="hpc log"
alias hshf="hpc sync_hf"
alias hslogs="hpc sync_job_logs"
alias hlgn="hpc ssh"
alias hcmd="hpc cmd"
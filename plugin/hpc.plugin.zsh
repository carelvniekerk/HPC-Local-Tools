fpath=($HOME/.oh-my-zsh/plugins/hpc_tools $fpath)

# Configure HPC Tools
export HPC_TOOLS_DIR="${HOME}/.hpc_tools"
export PATH="${HPC_TOOLS_DIR}:${PATH}"

JOB_LOGS_LOCAL_DIR="${JOB_LOGS_LOCAL_DIR:-${HOME}/Projects/hpc_job_logs}"
JOB_LOGS_BACKUP_LOCAL_DIR="${JOB_LOGS_BACKUP_LOCAL_DIR:-${HOME}/Projects/hpc_job_logs_backup}"

# Shorthand Aliases
alias hrun="hpc run"
alias hs="hpc status"
alias hqi="hpc qi"
alias hcl="hpc log"
alias hshf="hpc sync_hf"
alias hslogs="hpc sync_job_logs"
alias hlgn="hpc ssh"
alias hcmd="hpc cmd"
alias hlogs="vsc ${JOB_LOGS_LOCAL_DIR}"
alias hdel="hpc delete_job"
PYTHON_INTERPRETER=/Users/carel17/Projects/hpc-tools/.venv/bin/python3
TOOLS_DIR=/Users/carel17/Projects/hpc-tools

alias hpc_submit="${PYTHON_INTERPRETER} ${TOOLS_DIR}/submit.py"
alias hpc_status="ssh Hilbert -t \"bash -ci 'base && home && qs'\""
alias hpc_interactive_setup="ssh Hilbert -t \"bash -ci 'base && home && qi-setup'\""
alias hpc_int="ssh Hilbert -t \"bash -ci 'base && home && qi'\""
alias hpc_job_log="ssh Hilbert -t \"bash -ci 'base && home && job_log'\""

# Alias for syncing local huggingface models with HPC
alias sync_hf="rsync -avz --delete --progress /Users/carel17/.cache/huggingface Hilbert-Storage:/gpfs/project/niekerk/models/"

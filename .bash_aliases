alias ..='cd ..;l'
alias python='/usr/bin/python3'
alias l='ls -CF'
alias ll='ls -l'
alias lll='ls -lah'
alias lR='ls -lahR'

alias bashrc='vim ~/.bashrc'
alias bashal='vim ~/.bash_aliases'
alias bashpf='vim ~/.bash_profile'
alias lb='source ~/.bash_profile'

# Aliases for WSL2
alias winhome='/mnt/c/Users/dylan'

# Search command line history
alias h="history | grep "


# Search running processes
alias p="ps aux | grep "
alias topcpu="/bin/ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10"

# Show current network connections to the server
alias ipview="netstat -anpl | grep :80 | awk {'print \$5'} | cut -d\":\" -f1 | sort | uniq -c | sort -n | sed -e 's/^ *//' -e 's/ *\$//'"

# Show open ports
alias ports='netstat -nape --inet'

# Space of files in directory
alias fspace='du -d 1 -h | sort -rh | more'

# Disk space of all files/folders
alias diskspace="du -Sh | sort -rh |more"

alias ccat="pygmentize -g -O style=lightbulb,linenos=1"

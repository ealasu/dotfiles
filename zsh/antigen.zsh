export ZPLUG_HOME=$ZSH/zsh/zplug
source $ZPLUG_HOME/init.zsh

zplug mafredri/zsh-async, from:github
zplug sindresorhus/pure, use:pure.zsh, from:github, as:theme
zplug zsh-users/zsh-history-substring-search
zplug zsh-users/zsh-syntax-highlighting

zplug load

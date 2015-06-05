alias reload!='. ~/.zshrc'

# enable color support of ls and also add handy aliases
if type dircolors > /dev/null && [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias p='pwd'

# vi
if [[ "$(uname)" == 'Darwin' ]]; then
  alias vi='mvim -v'
else
  alias vi=nvim
fi

# git
alias gca='git commit -a -m'
alias gp='git push'
gcp () {
    git commit -a -m "$1" && git push
}
alias gs='git status'
alias gd='git diff'

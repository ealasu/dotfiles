dotdir=~/.dotfiles

export PATH="$PATH:$dotdir/bin"
export PATH="$PATH:$HOME/bin"
export PATH="$PATH:$HOME/.linuxbrew/bin"
export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
export PATH="$PATH:$HOME/.gem/ruby/2.2.0/bin"
export PATH="/usr/local/heroku/bin:$PATH"

### Other env vars
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib"

[[ -s "$HOME/.gvm/scripts/gvm" ]] && source "$HOME/.gvm/scripts/gvm"

export NVM_DIR="$HOME/.nvm"
source $(brew --prefix nvm)/nvm.sh

# added by Anaconda3 2.4.1 installer
export PATH="$HOME/anaconda3/bin:$PATH"

# Make sure we're in a tmux session, except on OS X
if [ -z $TMUX ] && [[ "$(uname)" -ne 'Darwin' ]]; then
  if tmux ls; then
    exec tmux attach
  else
    exec tmux
  fi
fi

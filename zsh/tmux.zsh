# For SSH connections, make sure we're in a tmux session
if [ -z $TMUX ] && [ -n "$SSH_CLIENT" ]; then
  if tmux ls; then
    exec tmux attach
  else
    exec tmux
  fi
fi

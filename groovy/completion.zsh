export GRADLE_OPTS='-Xms512m -Xmx4G -XX:MaxPermSize=256m -Djava.net.preferIPv4Stack -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp'

function init_gvm {
  #source ~/.gvm/bin/gvm-init.sh
  export SDKMAN_DIR="/Users/ealasu/.sdkman" && source ~/.sdkman/bin/sdkman-init.sh
}

if [[ -e ~/.sdkman/bin/sdkman-init.sh ]]; then
  init_gvm
fi

if [[ -e ~/.gvm/bin/gvm-init.sh ]]; then
  source ~/.gvm/bin/gvm-init.sh
fi

export GRADLE_OPTS='-Xms512m -Xmx4G -XX:MaxPermSize=256m -Djava.net.preferIPv4Stack -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp'

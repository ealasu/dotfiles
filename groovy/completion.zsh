export GRADLE_OPTS='-Xms512m -Xmx4G -XX:MaxPermSize=256m -Djava.net.preferIPv4Stack -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp'

function init_gvm {
  source ~/.gvm/bin/gvm-init.sh
}
init_gvm


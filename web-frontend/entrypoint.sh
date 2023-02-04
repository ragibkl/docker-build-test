#!/bin/bash

run_gunicorn() {
	gunicorn -w 4 -b 0.0.0.0 'app:app'
}

run_nginx() {
	nginx -g 'daemon off;'
}

PID_LIST=""

run_gunicorn &
PID_LIST="$PID_LIST $!"

run_nginx &
PID_LIST="$PID_LIST $!"

trap "kill $PID_LIST" SIGINT SIGKILL EXIT
wait -n
exit $?

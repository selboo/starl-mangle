#!/bin/bash


pid=`ps x | grep -E 'nginx|uwsgi|ajaxterm2' | grep -v grep | awk '{print $1}'`


for i in $pid;do
	kill -9 $i
done

/usr/sbin/uwsgi -x /usr/local/tengine-1.4.6/conf/uwsgi/mangle.starl.com.cn.xml
/usr/local/tengine-1.4.6/sbin/nginx
/root/starl/ajaxterm2/ajaxterm2 &>/dev/null &

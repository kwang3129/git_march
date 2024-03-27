#!/bin/bash

current_time=`date +"%H:%M-%d/%m/%Y"`
cd /usr/local/etc/suricata/opnsense.rules/
git add .
git commit -m "auto commit $current_time "
git push origin main

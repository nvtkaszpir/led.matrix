#!/bin/bash

# add to cron something like this, adjust paths
## m h  dom mon dow   command
#  * *  *   *   *     /home/pi/led.matrix/set_time.sh > /home/pi/led.matrix/cron.log 2>&1


INSTALL_DIR=/home/pi/led.matrix/

cd ${INSTALL_DIR}
source env/bin/activate
python time.py
deactivate

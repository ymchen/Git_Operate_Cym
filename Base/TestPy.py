# -*- coding: utf-8 -*-
# @Author: ChenYiMin
# @Date:   2021-07-09 14:28:08
# @Last Modified by:   ChenYiMin
# @Last Modified time: 2021-07-09 14:33:19
import psutil
import datetime
print(psutil.cpu_times())
print(psutil.users())
print(datetime.datetime.fromtimestamp(psutil.boot_time ()).strftime("%Y-%m-%d %H: %M: %S") )

print(psutil.pids())
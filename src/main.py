import time
import htScript
import Setting
import ylScript


type = Setting.type

if type == 0:
    times = Setting.htTimes
    while times > 0:
        # time_start = time.time()
        htScript.start()
        htScript.battle()
        htScript.end()
        # time_end = time.time()
        cishu = times - 1
        # print('time cost', time_end - time_start, 's')
        print("剩余次数:", times)

if type == 1:
    times = Setting.ylTimes
    while times > 0:
        # time_start = time.time()
        ylScript.start()
        ylScript.battle()
        ylScript.end()
        # time_end = time.time()
        cishu = times - 1
        # print('time cost', time_end - time_start, 's')
        print("剩余次数:", times)


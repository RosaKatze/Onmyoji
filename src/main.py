import time
import guaji
import Setting

cishu = Setting.cishu
while cishu > 0:
    # time_start = time.time()
    guaji.start()
    guaji.battle()
    guaji.end()
    # time_end = time.time()
    cishu = cishu - 1
    # print('time cost', time_end - time_start, 's')
    print("剩余次数:", cishu)

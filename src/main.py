import guaji
import Setting

cishu = Setting.cishu
while cishu > 0:
    guaji.start()
    guaji.battle()
    guaji.end()
    cishu = cishu - 1
    print("剩余次数:", cishu)


# guaji.end()
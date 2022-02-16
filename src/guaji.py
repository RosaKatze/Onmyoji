import time
import random
import win32api
import win32con
import Setting
import Image

"""
开始、战斗、结束的具体功能
"""


def start():
    # 开始界面的图片
    filename = Setting.startimage()
    # 匹配一下
    start_loc = Image.match(filename)
    time.sleep(0.5)
    if start_loc is not None:
        # 如果匹配到了，就把list拿过来，取到4个点
        for i in range(len(start_loc)):
            startregion_lefttop_x = start_loc[i].left
            startregion_lefttop_y = start_loc[i].top
            startregion_rightbot_x = start_loc[i].left + start_loc[i].width
            startregion_rightbot_y = start_loc[i].top + start_loc[i].height
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                suiji(startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y))
            # 单击
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            print("开始")
            # 等待加载
            time.sleep(2.5)
    else:
        print("未匹配到")
        time.sleep(2.5)
        endcheck()


def battle():
    # 战斗界面的图片
    filename = Setting.battleimage()
    # 匹配一下
    battle_loc = Image.match(filename)
    if battle_loc is not None:
        # 如果匹配到了，就把list拿过来，取到4个点
        for i in range(len(battle_loc)):
            battleregion_lefttop_x = battle_loc[i].left
            battleregion_lefttop_y = battle_loc[i].top
            battleregion_rightbot_x = battle_loc[i].left + battle_loc[i].width
            battleregion_rightbot_y = battle_loc[i].top + battle_loc[i].height
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                suiji(battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y))
        print("正在战斗")
        # 这个就是挂机的时间
        time.sleep(Setting.time)
        print("打完了")
        # 等待进入结束界面
        time.sleep(3)


def end():
    # 结束界面的图片
    filename = Setting.endimage()
    # 匹配一下
    end_loc = Image.match(filename)
    if end_loc is not None:
        # 如果匹配到了，就把list拿过来，取到4个点
        for i in range(len(end_loc)):
            endregion_lefttop_x = end_loc[i].left
            endregion_lefttop_y = end_loc[i].top
            endregion_rightbot_x = end_loc[i].left + end_loc[i].width
            endregion_rightbot_y = end_loc[i].top + end_loc[i].height
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
            print("结算中")
            # # 要等一会，跳出界面点才有用
            # time.sleep(1)
            print(i, "在狂点")
            # 随机点击次数6到8次
            for fre in range(0, random.randint(6, 8)):
                print(fre)
                # 移动到随机生成的坐标，防检测
                win32api.SetCursorPos(
                    suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
                # 单击
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                # 每次点击间隔随机
                time.sleep(random.uniform(0.5, 0.8))
    else:
        print("未匹配到")
        time.sleep(2.5)
        endcheck()
    # 等下回到开始界面
    time.sleep(1.5)


def endcheck():
    # 结束界面的图片
    filename = Setting.endimgcheck()
    # 匹配一下
    end_loc = Image.match(filename)
    if end_loc is not None:
        # 如果匹配到了，就直接把4个坐标拿过来
        for i in range(len(end_loc)):
            endregion_lefttop_x = end_loc[i].left
            endregion_lefttop_y = end_loc[i].top
            endregion_rightbot_x = end_loc[i].left + end_loc[i].width
            endregion_rightbot_y = end_loc[i].top + end_loc[i].height
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
            print("结算中")
            # # 要等一会，跳出界面点才有用
            # time.sleep(1)
            print(i, "在狂点")
            # 随机点击次数6到8次
            for fre in range(0, random.randint(1, 3)):
                print(fre)
                # 移动到随机生成的坐标，防检测
                win32api.SetCursorPos(
                    suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
                # 单击
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                # 每次点击间隔随机
                time.sleep(random.uniform(0.5, 0.8))
    else:
        print("error")


# 先确定点击的范围
def suiji(xmin, ymin, xmax, ymax):
    # 在此范围内随机生成一个数
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)
    return x, y

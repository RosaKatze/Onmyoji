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
    fileName = Setting.ylStartImage()
    # 匹配一下
    startCoordinate = Image.match(fileName)
    time.sleep(0.5)
    if startCoordinate is not None:
        # 如果匹配到了，就把list拿过来，取到4个点
        for i in range(len(startCoordinate)):
            startCoordinateLeftTopX = startCoordinate[i].left
            startCoordinateLeftTopY = startCoordinate[i].top
            startCoordinateRightBotX = startCoordinate[i].left + startCoordinate[i].width
            startCoordinateRightBotY = startCoordinate[i].top + startCoordinate[i].height
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                randomRange(startCoordinateLeftTopX, startCoordinateLeftTopY, startCoordinateRightBotX, startCoordinateRightBotY))
            # 单击
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            print("开始")
            # 等待加载
            time.sleep(2.5)
    else:
        print("未匹配到")
        time.sleep(2.5)
        endCheck()


def battle():
    # 战斗界面的图片
    fileName = Setting.ylBattleImage()
    # 匹配一下
    battleCoordinate = Image.match(fileName)
    if battleCoordinate is not None:
        print("正在战斗")
        # 这个就是挂机的时间
        time.sleep(Setting.ylTime)
        print("打完了")
        # 等待进入结束界面
        time.sleep(2)



def end():
    # 结束界面的图片
    fileName = Setting.ylEndImage()
    # 匹配一下
    endCoordinate = Image.match(fileName)
    if endCoordinate is not None:
        # 如果匹配到了，就把list拿过来，取到4个点
        # 第一阶段的点击
        for i in range(len(endCoordinate)):
            endCoordinateLeftTopX = endCoordinate[i].left
            endCoordinateLeftTopY = endCoordinate[i].top
            endCoordinateRightBotX = endCoordinate[i].left + endCoordinate[i].width
            endCoordinateRightBotY = endCoordinate[i].top + endCoordinate[i].height
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                randomRange(endCoordinateLeftTopX, endCoordinateLeftTopY, endCoordinateRightBotX, endCoordinateRightBotY))
            print("结算中")
            # # 要等一会，跳出界面点才有用
            # time.sleep(1)
            print("队友", i, "在狂点")
            # 随机点击次数2到4次
            for clickTimes in range(0, random.randint(2, 4)):
                print(clickTimes)
                # 移动到随机生成的坐标，防检测
                win32api.SetCursorPos(
                    randomRange(endCoordinateLeftTopX, endCoordinateLeftTopY, endCoordinateRightBotX, endCoordinateRightBotY))
                # 单击
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                # 每次点击间隔随机
                time.sleep(random.uniform(0.3, 0.5))
    else:
        print("未匹配到")
        time.sleep(2.5)
        endCheck()
    # 等下回到开始界面
    time.sleep(1)


def endCheck():
    # 结束界面的图片
    fileName = Setting.ylEndImgeCheck()
    # 匹配一下
    endCheckCoordinate = Image.match(fileName)
    if endCheckCoordinate is not None:
        # 如果匹配到了，就直接把4个坐标拿过来
        for i in range(len(endCheckCoordinate)):
            endCheckCoordinateLeftTopX = endCheckCoordinate[i].left
            endCheckCoordinateLeftTopY = endCheckCoordinate[i].top
            endCheckCoordinateRightBotX = endCheckCoordinate[i].left + endCheckCoordinate[i].width
            endCheckCoordinateRightBotY = endCheckCoordinate[i].top + endCheckCoordinate[i].height
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                randomRange(endCheckCoordinateLeftTopX, endCheckCoordinateLeftTopY, endCheckCoordinateRightBotX, endCheckCoordinateRightBotY))
            print("结算中")
            # # 要等一会，跳出界面点才有用
            # time.sleep(1)
            print(i, "在狂点")
            # 随机点击次数6到8次
            for clickTimes in range(0, random.randint(1, 3)):
                print(clickTimes)
                # 移动到随机生成的坐标，防检测
                win32api.SetCursorPos(
                    randomRange(endCheckCoordinateLeftTopX, endCheckCoordinateLeftTopY, endCheckCoordinateRightBotX, endCheckCoordinateRightBotY))
                # 单击
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                # 每次点击间隔随机
                time.sleep(random.uniform(0.5, 0.8))
    else:
        print("error")


# 先确定点击的范围
def randomRange(xMin, yMin, xMax, yMax):
    # 在此范围内随机生成一个数
    x = random.randint(xMin, xMax)
    y = random.randint(yMin, yMax)
    return x, y

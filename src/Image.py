import pyautogui


def match(filename):
    # 在屏幕上查找图像返回(左、顶、宽、高)的第一个位置（配合list函数），如果屏幕上找不到图像返回None,
    # 添加confidence关键字参数指定函数在屏幕上定位图像的准确性
    location = list(pyautogui.locateAllOnScreen(filename, confidence=0.9))
    print(location)
    if location is not None:
        # 如果匹配到了，把直接返回一个list
        return location
    else:
        # 没匹配到，就返回None
        return None

# def match(filename):
#     # 在屏幕上查找图像返回(左、顶、宽、高)的第一个位置（配合list函数），如果屏幕上找不到图像返回None,
#     # 添加confidence关键字参数指定函数在屏幕上定位图像的准确性
#     location = pyautogui.locateOnScreen(filename, confidence=0.9)
#     if location is not None:
#         # 如果匹配到了，把左上和右下的坐标算出来
#         xmin = location.left
#         ymin = location.top
#         xmax = location.left + location.width
#         ymax = location.top + location.height
#         return xmin, ymin, xmax, ymax
#     else:
#         # 没匹配到，就返回None
#         return None

"""
配置文件
"""

# 挂一次的时间
time = 17

# 想要挂多少次
cishu = 30


# 开始界面的图片位置
def startimage():
    templateimage = r"E:\test\start.png"
    return templateimage


# 战斗界面的图片位置
def battleimage():
    templateimage = r"E:\test\battle.png"
    return templateimage


# 结束界面的图片位置
def endimage():
    templateimage = r"E:\test\end.png"
    return templateimage

# 结束界面校验的图片位置
def endimgcheck():
    templateimage = r"E:\test\check.png"
    return templateimage

import pyautogui as pygui

x1,y1 = 650, 507
x2,y2 = 745, 507
x3,y3 = 825, 507
x4,y4 = 895, 507
colorlist = [(1,1,1),(0,2,4)]

try:
    while True:
        square1check = pygui.pixel(x1,y1)
        square2check = pygui.pixel(x2,y2)
        square3check = pygui.pixel(x3,y3)
        square4check = pygui.pixel(x4,y4)

        if square1check in colorlist:
            pygui.click(x1,y1)
        if square2check in colorlist:
            pygui.click(x2,y2)
        if square3check in colorlist:
            pygui.click(x3,y3)
        if square4check in colorlist:
            pygui.click(x4,y4)
except KeyboardInterrupt:
    print('stopped')



#colorlist = [(1,1,1), (1,2,4), (1,2,3), (0,6,4), (74, 212, 212), (0,2,4)]

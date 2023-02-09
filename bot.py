from pyautogui import *
import time
import pyautogui
import win32api
import win32con
import win32gui
import keyboard


def clientResolution():
    for lolResolution in range(1, 4):
        lol = pyautogui.locateOnScreen(
            f'images/clientRes/lol{lolResolution}.png', 
            confidence=0.8
        )
        
        if lol != None:
            break

        else:
            bug = pyautogui.locateOnScreen(
                f'images/clientReg/bug{lolResolution}.png', 
                confidence=0.8
            )

            if bug != None:
                break

    return lolResolution


def clientRegion(size):
    got = False

    while not got:
        l = pyautogui.locateOnScreen(f'images/clientReg/lol{size}.png', confidence=0.8)
        bug = pyautogui.locateOnScreen(f'images/clientReg/bug{size}.png', confidence=0.8)

        if l and bug:
            x = l[0]
            y = l[1]
            width = bug[0] - (l[0] - l[2])
            height = bug[1] - (l[1] - l[3])
            got = True

        else:
            x = 0
            y = 0
            width, height = pyautogui.size()
            got = True

    return x, y, width, height       


def gameRegion():
    got = False

    if not got:
        icon = pyautogui.locateOnScreen(f'images/gameReg/icon.png', confidence=0.8)
        settings = pyautogui.locateOnScreen(f'images/gameReg/settings.png', confidence=0.8)

        if icon and settings:
            x = icon[0]
            y = icon[1]
            width = (settings[0] + settings[2]) - icon[0]
            height = (settings[1] + settings[3]) - icon[1]
            got = True

        

    return x, y, width, height


def storeRegion():
    got = False

    if not got:
        level = pyautogui.locateOnScreen(f'images/storeReg/level.png', confidence=0.8)
        lock = pyautogui.locateOnScreen(f'images/storeReg/lock.png', confidence=0.8)
        gold = pyautogui.locateOnScreen(f'images/storeReg/gold.png', confidence=0.8)

        if level and lock and gold:
            x = level[0]
            y = level[1]
            width = (lock[0] + (lock[2] * 2)) - level[0]
            height = (gold[1] + gold[3] + 10) - level[1]
            got = True

        else:
            x = 0
            y = 0
            width, height = pyautogui.size()
            got = True

    return x, y, width, height


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def rightClick(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)


def check():
    level = pyautogui.locateOnScreen(f'images/gameReg/icon.png', confidence=0.8)
    if level:
        return True
    else:
        return False


def play(size, region):
    play = pyautogui.locateOnScreen(
        f'images/client/play{size}.png', 
        region=region, 
        confidence=0.8
    )

    if play != None:
        playLocation = pyautogui.center(play)
        win32api.SetCursorPos(playLocation)
        x, y = playLocation
        click(x, y)



def playtft(size, region):
    tft = pyautogui.locateOnScreen(
        f'images/client/tft{size}.png', 
        region=region, 
        confidence=0.8
    )


    if tft != None:
        tftLocation = pyautogui.center(tft)
        win32api.SetCursorPos(tftLocation)
        x, y = tftLocation
        click(x, y)



def playtftNormal(size, region):
    tftNormal = pyautogui.locateOnScreen(
        f'images/client/tftNormal{size}.png', 
        region=region, 
        confidence=0.8
    )

    if tftNormal != None:
        tftNormalLocation = pyautogui.center(tftNormal)
        win32api.SetCursorPos(tftNormalLocation)
        x, y = tftNormalLocation
        click(x, y)



def confirm(size, region):
    confirm = pyautogui.locateOnScreen(
        f'images/client/confirm{size}.png', 
        region=region, 
        confidence=0.8
    )

    if confirm != None:
        confirmLocation = pyautogui.center(confirm)
        win32api.SetCursorPos(confirmLocation)
        x, y = confirmLocation
        click(x, y)


def find(size, region):
    find = pyautogui.locateOnScreen(
        f'images/client/find{size}.png', 
        region=region, 
        confidence=0.8
    )

    if find != None:
        findLocation = pyautogui.center(find)
        win32api.SetCursorPos(findLocation)
        x, y = findLocation
        click(x, y)


def accept(size, region):
    accept = pyautogui.locateOnScreen(
        f'images/client/accept{size}.png', 
        region=region, 
        confidence=0.8
    )


    if accept != None:
        acceptLocation = pyautogui.center(accept)
        win32api.SetCursorPos(acceptLocation)
        x, y = acceptLocation
        click(x, y)


def wait(size, region):
    wait = pyautogui.locateOnScreen(
        f'images/client/wait{size}.png', 
        region=region, 
        confidence=0.8
    )

    if wait != None:
        waitLocation = pyautogui.center(wait)
        win32api.SetCursorPos(waitLocation)
        x, y = waitLocation
        click(x, y)


def again(size, region):
    again = pyautogui.locateOnScreen(
        f'images/client/again{size}.png', 
        region=region, 
        confidence=0.8
    )

    if again != None:
        againLocation = pyautogui.center(again)
        win32api.SetCursorPos(againLocation)
        x, y = againLocation
        click(x, y)


def level(region):
    colors = ['Gray', 'Green', 'Blue', 'Purple', 'Yellow']
    for color in colors:
        level = pyautogui.locateOnScreen(
            f'images/game/level{color}.png', 
            region=region, 
            confidence=0.8
        )

        if level != None:
            levelLocation = pyautogui.center(level)
            win32api.SetCursorPos(levelLocation)
            x, y = levelLocation
            click(x, y)


def update(region):
    update = pyautogui.locateOnScreen(
        f'images/game/update.png', 
        region=region, 
        confidence=0.8
    )

    if update != None:
        updateLocation = pyautogui.center(update)
        win32api.SetCursorPos(updateLocation)
        x, y = updateLocation
        click(x, y)


def exp(region):
    golds = ['3', '4', '5', '6']
    for gold in golds:
        exp = pyautogui.locateOnScreen(
            f'images/game/exp.png', 
            region=region, 
            confidence=0.8
        )
        money = pyautogui.locateOnScreen(
            f'images/game/gold{gold}.png', 
            region=region, 
            confidence=0.8
        )
        up4 = pyautogui.locateOnScreen(
            f'images/game/up4.png', 
            region=region, 
            confidence=0.8
        )

        if exp != None and money != None:
            expLocation = pyautogui.center(exp)
            win32api.SetCursorPos(expLocation)
            x, y = expLocation
            click(x, y)
        elif up4 != None:
            expLocation = pyautogui.center(exp)
            win32api.SetCursorPos(expLocation)
            x, y = expLocation
            click(x, y)



def orb(region):
    colors = ['Gray', 'Blue', 'Yellow']
    for color in colors:
        orb = pyautogui.locateOnScreen(
            f'images/game/orb{color}.png', 
            region=region, 
            confidence=0.8
        )

        if orb != None:
            orbLocation = pyautogui.center(orb)
            win32api.SetCursorPos(orbLocation)
            x, y = orbLocation
            rightClick(x, y)


def exit(region):
    exit = pyautogui.locateOnScreen(
        f'images/game/exit.png', 
        region=region, 
        confidence=0.8
    )

    if exit != None:
        exitLocation = pyautogui.center(exit)
        win32api.SetCursorPos(exitLocation)
        x, y = exitLocation
        click(x, y)


def inClient():
    try:
        resolution = clientResolution()
        (x, y, width, height) = clientRegion(resolution)
    except:
        pass

    try:
        play(resolution, (x, y, width, height))
        playtft(resolution, (x, y, width, height))
        playtftNormal(resolution, (x, y, width, height))
        confirm(resolution, (x, y, width, height))
        find(resolution, (x, y, width, height))
        accept(resolution, (x, y, width, height))
        wait(resolution, (x, y, width, height))
        again(resolution, (x, y, width, height))
    except:
        pass


def inGame():
    try:
        (x, y, width, height) = gameRegion()
    except:
        pass

    try:
        (sx, sy, swidth, sheight) = storeRegion()
    except:
        pass

    try:
        level((sx, sy, swidth, sheight))
        exp((sx, sy, swidth, sheight))
        #update((sx, sy, swidth, sheight))
    except:
        pass
 
    try:
        orb((x, y, width, height))
        exit((x, y, width, height))
    except:
        pass


if __name__ == '__main__':
    print('Bot criado por Weoah\nDiscord: We04h#1235')

    while keyboard.is_pressed('q') != None:
        time.sleep(1)

        client = win32gui.FindWindow(0, "League of Legends")
        game = win32gui.FindWindow(0, "League of Legends (TM) Client")

        try:
            if not game:
                win32gui.SetForegroundWindow(client)
                win32gui.BringWindowToTop(client)
                inClient()
            else:
                win32gui.SetForegroundWindow(game)
                win32gui.BringWindowToTop(game)
                inGame()
        except:
            pass
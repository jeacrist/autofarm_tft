import time
import pyautogui
import win32api
import win32con
import win32gui
import keyboard
import pywintypes


def left_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def right_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


def move_to(btn):
    if btn is not None:
        btn_pos = pyautogui.center(btn)
        new_pos = (btn_pos[0] + 30, btn_pos[1] + 50)
        win32api.SetCursorPos(new_pos)
        time.sleep(1)
        left_click(*new_pos)
        time.sleep(0.5)


def button_check(btn, right=False):
    if btn is not None:
        btn_pos = pyautogui.center(btn)
        win32api.SetCursorPos(btn_pos)
        x, y = btn_pos
        if right:
            right_click(x, y)
        else:
            left_click(x, y)


def client_positions():
    for size in range(1, 4):
        l_icon = pyautogui.locateOnScreen(
            f'images/client/lol{size}.png',
            confidence=0.8, grayscale=True)
        bug_icon = pyautogui.locateOnScreen(
            f'images/client/bug{size}.png',
            confidence=0.8, grayscale=True)

        if l_icon is not None and \
                bug_icon is not None:
            return size, l_icon, bug_icon

        find_icon = pyautogui.locateOnScreen(
            f'images/client/again{size}.png',
            confidence=0.8, grayscale=True)

        if find_icon is not None:
            return (size, )

    return (4, )


def client_resolution(positions):
    if positions is not None \
            and len(positions) > 1:
        l_icon = positions[1]
        bug_icon = positions[2]
        x_pos = l_icon[0]
        y_pos = l_icon[1]
        width = bug_icon[0] - (l_icon[0] - l_icon[2])
        height = bug_icon[1] - (l_icon[1] - l_icon[3])
        return x_pos, y_pos, width, height

    abs_width, abs_height = pyautogui.size()
    return 0, 0, abs_width, abs_height


def game_positions():
    window_icon = pyautogui.locateOnScreen(
        'images/game/icon.png',
        confidence=0.8, grayscale=True)
    cog_icon = pyautogui.locateOnScreen(
        'images/game/cog_icon.png',
        confidence=0.8, grayscale=True)
    update_icon = pyautogui.locateOnScreen(
        'images/game/update.png',
        confidence=0.8, grayscale=True)

    if window_icon is not None \
            and cog_icon is not None \
            and update_icon is not None:
        x_pos = window_icon[0]
        y_pos = window_icon[1]
        width = (cog_icon[0] + 30) - window_icon[0]
        height = (update_icon[1] + 30) - window_icon[1]

        return x_pos, y_pos, width, height

    abs_width, abs_height = pyautogui.size()
    return 0, 0, abs_width, abs_height


def in_client(size, resolution):

    def press_button():
        buttons = (
            'play', 'tft', 'tftNormal', 'confirm',
            'find', 'accept', 'wait', 'again')
        for button in buttons:
            press_btn = pyautogui.locateOnScreen(
                f'images/client/{button}{size}.png',
                region=resolution, confidence=0.8, grayscale=True)
            button_check(press_btn)

    return press_button


def in_game(resolution):

    def buy_champ():
        check_need = pyautogui.locateOnScreen(
            'images/game/buy_champion.png',
            region=resolution, confidence=0.8, grayscale=True)

        if check_need is not None:
            exp_btn = pyautogui.locateOnScreen(
                'images/game/update.png',
                region=resolution, confidence=0.8, grayscale=True)
            button_check(exp_btn)

    def get_orbs():
        buttons = ('orb_blue', 'orb_gray', 'orb_yellow')
        for button in buttons:
            press_btn = pyautogui.locateOnScreen(
                f'images/game/{button}.png',
                region=resolution, confidence=0.8, grayscale=True)
            button_check(press_btn, True)

    def upgrade_champions():
        buttons = (
            'up_blue', 'up_green', 'up_gray',
            'up_yellow',  'up_purple')
        for button in buttons:
            press_btn = pyautogui.locateOnScreen(
                f'images/game/{button}.png',
                region=resolution, confidence=0.78, grayscale=True)
            button_check(press_btn)

    def press_static_buttons():
        buttons = (
            'card', 'quit')
        for button in buttons:
            press_btn = pyautogui.locateOnScreen(
                f'images/game/{button}.png',
                region=resolution, confidence=0.8, grayscale=True)
            button_check(press_btn)

    def get_exp():
        checks = (
            'limit_40', 'limit_50', 'limit_60',
            'lvl_up_4', 'lvl_up_5')
        for check in checks:
            check_btn = pyautogui.locateOnScreen(
                f'images/game/{check}.png',
                region=resolution, confidence=0.8, grayscale=True)

            if check_btn is not None:
                exp_btn = pyautogui.locateOnScreen(
                    'images/game/exp.png',
                    region=resolution, confidence=0.8, grayscale=True)
                button_check(exp_btn)

    def item_equip():
        item_checks = (
            'item_1', 'item_2', 'item_3',
            'item_4', 'item_5', 'item_6',
            'item_7', 'item_8', 'item_9',
            'item_10', 'item_11', 'item_12')
        for items in item_checks:
            check_item = pyautogui.locateOnScreen(
                f'images/game/{items}.png',
                region=resolution, confidence=0.85, grayscale=True)

            if check_item is not None:
                check_char_2 = pyautogui.locateOnScreen(
                    'images/game/champion_2.png',
                    region=resolution, confidence=0.8, grayscale=True)

                if check_char_2 is not None:
                    button_check(check_item)
                    time.sleep(0.5)
                    move_to(check_char_2)
                    break

                check_char_1 = pyautogui.locateOnScreen(
                    'images/game/champion_1.png',
                    region=resolution, confidence=0.8, grayscale=True)

                if check_char_1 is not None:
                    button_check(check_item)
                    time.sleep(0.5)
                    move_to(check_char_1)

    def run():
        upgrade_champions()
        get_exp()
        upgrade_champions()
        press_static_buttons()
        upgrade_champions()
        get_orbs()
        upgrade_champions()
        buy_champ()
        upgrade_champions()
        item_equip()

    return run


def start():
    client = win32gui.FindWindow(0, "League of Legends")
    game = win32gui.FindWindow(0, "League of Legends (TM) Client")
    if not game:
        print('\n\nBot criado por Weoah\nDiscord: We04h#1235')
        win32gui.SetForegroundWindow(client)
        win32gui.BringWindowToTop(client)
        in_client_positions = client_positions()
        in_client_resolution = client_resolution(in_client_positions)
        time.sleep(2)
        window_client = in_client(in_client_positions[0], in_client_resolution)
        window_game = False
    else:
        in_game_positions = game_positions()
        time.sleep(2)
        window_game = in_game(in_game_positions)
        window_client = False

    return game, client, window_client, window_game


if __name__ == '__main__':
    game, client, window_client, window_game = start()

    while keyboard.is_pressed('q') is not None:
        time.sleep(0.1)

        try:
            if client:
                win32gui.SetForegroundWindow(client)
                win32gui.BringWindowToTop(client)
                window_client()

            elif game:
                win32gui.SetForegroundWindow(game)
                win32gui.BringWindowToTop(game)
                window_game()
        except pywintypes.error:
            time.sleep(10)
            game, client, window_client, window_game = start()

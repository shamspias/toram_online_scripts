import pyautogui


def close_all():
    """
    Close if any window or bag or anything open
    """
    return pyautogui.click(x=1300,y=32,interval=1.0)

def open_gift():
    """ Open Gift bar """
    return pyautogui.click(x=101,y=483,interval=1.0)

def recive_gifts(number_of_gift=1):
    """
    Recived gift from specific numbers
    """
    close_all()
    open_gift()
    pyautogui.click(x=1000,y=510,interval=1.5)
    for i in range(number_of_gift):
        pyautogui.click(x=1048,y=216,interval=0.5)
        pyautogui.click(x=675,y=682,interval=1.0)
    return close_all()

def send_gift(number_of_gift=1):
    """ send 1st party member gift """
    close_all()
    open_gift()
    for i in range(number_of_gift):
        pyautogui.click(x=1000,y=410,interval=0.5)
        pyautogui.click(x=711,y=260,interval=0.5)
        pyautogui.click(x=680,y=245,interval=0.5)
        pyautogui.click(x=760,y=400,interval=0.5)
        pyautogui.click(x=740,y=200,clicks=2, interval=1.0)
        pyautogui.click(x=966,y=348,interval=1.0)
        pyautogui.click(x=700,y=560,interval=1.0)
        pyautogui.click(x=400,y=344,interval=1.0)
        pyautogui.click(x=722,y=708,interval=0.5)
        pyautogui.click(x=681,y=680,interval=1.5)
    return close_all()


def open_trade():
    """ Open Trade option """
    return pyautogui.click(x=105,y=475,interval=0.5)

def trade(number_of_trade=1):
    """ Trade when get trade request """
    trade_x_cordinates = 780
    close_all()
    for i in range(number_of_trade):
        open_trade()
        pyautogui.click(x=1000,y=300,interval=0.5)
        pyautogui.click(x=880,y=655,interval=1.5)
        pyautogui.click(x=675,y=621,interval=0.5)
        for i in range(4):
            pyautogui.click(x=trade_x_cordinates,y=200,clicks=2, interval=1.0)
            pyautogui.click(x=966,y=348,interval=1.0)
            pyautogui.click(x=700,y=560,interval=1.0)
            trade_x_cordinates += 100
        pyautogui.click(x=355,y=415,interval=1.0)
        pyautogui.click(x=680,y=530,interval=3.0)
        pyautogui.click(x=680,y=530,interval=1.0)
        pyautogui.click(x=690,y=655,interval=5.0)

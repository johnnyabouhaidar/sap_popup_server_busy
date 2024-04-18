import pygetwindow as gw
import pyautogui
from pywinauto import application
import time
import win32gui
import win32con
import win32api



def send_enter_key(hwnd):
    # Send a key down event for Enter
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    # Send a key up event for Enter
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def get_windows_with_text(text):
    windows = gw.getWindowsWithTitle(text)
    return windows

def click_button_in_window(window_title, button_text):
    # Get the window with the specified title
    window = gw.getWindowsWithTitle(window_title)
    if len(window) == 0:
        print(f"Window '{window_title}' not found.")
        return
    
    # Focus on the window
    #window[0].close()
    '''app = application.Application().connect(title="server busy")
    window = app.window(title="testt")
    window.type_keys("{ENTER}")'''
    hwnd = win32gui.FindWindow(None, 'testt')
    send_enter_key(hwnd)
    

    # Find the button by its text
    '''
    button_position = pyautogui.locateOnScreen('Retry.PNG')
    print(button_position)
    if button_position is not None:
        button_center = pyautogui.center(button_position)
        pyautogui.click(button_center)'''
    

# Example usage
if __name__ == "__main__":
    while True:
        time.sleep(10)
        print("checking")
        windows = get_windows_with_text("Server Busy")
        for window in windows:
            #click_button_in_window("SAP Logon 750","Retry")
            click_button_in_window("server busy","Retry")
        time.sleep(59)
import pygetwindow as gw
import pyautogui
import time

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
    window[0].activate()

    # Find the button by its text
    button_position = pyautogui.locateOnScreen('Retry.PNG')
    print(button_position)
    if button_position is not None:
        button_center = pyautogui.center(button_position)
        pyautogui.click(button_center)
        print("CLICKED!!")

# Example usage
if __name__ == "__main__":
    while True:
        print("checking")
        windows = get_windows_with_text("Server Busy")
        for window in windows:
            click_button_in_window("Server Busy","Retry")
        time.sleep(59)
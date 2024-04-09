import pygetwindow as gw
import pyautogui

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
    button_position = pyautogui.locateCenterOnScreen(f"{button_text}.PNG")
    if button_position is None:
        print(f"Button '{button_text}' not found.")
        return

    # Click on the button
    pyautogui.click(button_position)

# Example usage
if __name__ == "__main__":
    windows = get_windows_with_text("testt")
    for window in windows:
        click_button_in_window("testt","OK")
import pyautogui
import time

# Safety: move mouse to corner to abort
pyautogui.FAILSAFE = True

def click_at(x, y, double=False):
    """Clicks at (x, y) coordinates."""
    pyautogui.moveTo(x, y, duration=0.5)
    if double:
        pyautogui.doubleClick()
    else:
        pyautogui.click()

def type_string(text, interval=0.1):
    """Types a string of text."""
    pyautogui.write(text, interval=interval)

def press_key(key):
    """Presses a specific key (e.g., 'enter', 'esc')."""
    pyautogui.press(key)

def scroll(amount):
    """Scrolls up (positive) or down (negative)."""
    pyautogui.scroll(amount)

def get_screen_size():
    """Returns (width, height) of the screen."""
    return pyautogui.size()

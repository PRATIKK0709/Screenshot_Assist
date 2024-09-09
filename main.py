import os
from datetime import datetime
import threading
import time
from PIL import ImageGrab
import keyboard
import customtkinter as ctk
from typing import Callable

class ScreenshotManager:
    def __init__(self, base_path: str):
        self.screenshots_folder = os.path.join(base_path, "Screenshots")
        os.makedirs(self.screenshots_folder, exist_ok=True)

    def take_screenshot(self) -> str:
        screenshot = ImageGrab.grab()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(self.screenshots_folder, filename)
        screenshot.save(filepath)
        return filepath

class TimerManager:
    @staticmethod
    def start_timer(delay: int, callback: Callable[[], None]):
        def timer_thread():
            time.sleep(delay)
            callback()
        threading.Thread(target=timer_thread, daemon=True).start()

class GUI:
    def __init__(self, screenshot_manager: ScreenshotManager):
        self.screenshot_manager = screenshot_manager
        self.app = ctk.CTk()
        self.app.title("Screenshot App")
        self.app.geometry("300x250")
        self._setup_widgets()

    def _setup_widgets(self):
        ctk.CTkButton(self.app, text="Take Screenshot", command=self._take_screenshot).pack(pady=10)
        
        self.timer_entry = ctk.CTkEntry(self.app, placeholder_text="Enter delay in seconds")
        self.timer_entry.pack(pady=10)
        
        ctk.CTkButton(self.app, text="Start Timer", command=self._start_timer).pack(pady=10)
        
        self.message_label = ctk.CTkLabel(self.app, text="")
        self.message_label.pack(pady=10)

    def _take_screenshot(self):
        try:
            filepath = self.screenshot_manager.take_screenshot()
            self._show_message(f"Screenshot saved to {filepath}")
        except Exception as e:
            self._show_message(f"Error taking screenshot: {e}", error=True)

    def _start_timer(self):
        try:
            delay = int(self.timer_entry.get())
            if delay > 0:
                self._show_message(f"Starting timer for {delay} seconds...")
                TimerManager.start_timer(delay, self._take_screenshot)
            else:
                raise ValueError("Delay must be positive")
        except ValueError as e:
            self._show_message(f"Invalid input: {e}", error=True)

    def _show_message(self, message: str, error: bool = False):
        color = "red" if error else "green"
        self.message_label.configure(text=message, text_color=color)
        print(message)

    def run(self):
        self.app.mainloop()

class ShortcutManager:
    def __init__(self, screenshot_func: Callable[[], None], timer_func: Callable[[], None]):
        self.screenshot_func = screenshot_func
        self.timer_func = timer_func

    def setup(self):
        keyboard.add_hotkey('ctrl+s', self.screenshot_func)
        keyboard.add_hotkey('ctrl+d', self.timer_func)

class ScreenshotApp:
    def __init__(self):
        base_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.screenshot_manager = ScreenshotManager(base_path)
        self.gui = GUI(self.screenshot_manager)
        self.shortcut_manager = ShortcutManager(self.gui._take_screenshot, self.gui._start_timer)

    def run(self):
        self.shortcut_manager.setup()
        self.gui.run()

if __name__ == "__main__":
    app = ScreenshotApp()
    app.run()

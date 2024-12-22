import ctypes
import os

from lynxtray import SysTrayIcon

icon_path = os.path.join(os.path.dirname(__file__), "test.ico")
shutdown_called = False
def on_quit(systray: SysTrayIcon) -> None:
	print("Bye")
def do_example(systray: SysTrayIcon) -> None:
	print("Example")
def on_about(systray: SysTrayIcon) -> None:
	ctypes.windll.user32.MessageBoxW(None, "This is a test of infi.systray", "About", 0)

menu_options = (
	("Example", None, do_example),
	("About", None, on_about))
systray = SysTrayIcon(icon_path, "Systray Test", menu_options, on_quit)
systray.start()

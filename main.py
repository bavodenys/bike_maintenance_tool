from main_functions import *
from logger import *
from kivy.app import App
from kivy.uix.label import Label

# Software version
MAJOR_VERSION = 0
MINOR_VERSION = 1

# Set window to screen size
# Window.maximize()

# Init of log file
logfile = LogFile()
logfile.message("----------------------------------------")
logfile.message(f"-- Bike Maintenance Tool {MAJOR_VERSION}.{MINOR_VERSION} -----------------------")
logfile.message("----------------------------------------")

# Try loading the json file with data


class MainApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == "__main__":
    app = MainApp()
    app.run()
    app.stop()
    # Close the debug file
    logfile.close()
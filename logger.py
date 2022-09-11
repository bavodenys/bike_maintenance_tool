from main_functions import *
from datetime import datetime

# Class log file
class LogFile():
    # Init of log file with file name "Bike_maintenance_tool_Log_date.txt
    def __init__(self):
        t = datetime.now()
        date_now_str = t.strftime("%Y") + "-" + t.strftime("%m") + "-" + t.strftime("%d")
        filename = "Bike_maintenance_tool_Log_" + date_now_str + ".txt"
        self.file = open("Logs/"+filename, "a")

    # DEBUG message
    def debug(self, message):
        self.file.write(get_datetime_now_str() + " " + "DEBUG: " + message + "\n")
        print(get_datetime_now_str() + " " + "DEBUG: " + message)

    # WARNING message
    def warning(self, message):
        self.file.write(get_datetime_now_str() + " " + "WARNING: " + message + "\n")
        print(get_datetime_now_str() + " " + "WARNING: " + message)

    # ERROR message
    def error(self, message):
        self.file.write(get_datetime_now_str() + " " + "ERROR: " + message + "\n")
        print(get_datetime_now_str() + " " + "ERROR: " + message)

    # INFO message
    def info(self, message):
        self.file.write(get_datetime_now_str() + " " + "INFO: " + message + "\n")
        print(get_datetime_now_str() + " " + "INFO: " + message)

    # Close
    def close(self):
        self.file.close()
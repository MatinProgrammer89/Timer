import os
from datetime import datetime


def clear_screen():

    os.system("cls")

now = datetime.now()
hour = now.hour
minute = now.minute
second = now.second
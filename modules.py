import time
from utills import clear_screen

class timer:

    def __init__(self,hour,minute,second):

        self.hour = hour
        self.minute = minute
        self.second = second
    
    def increase_hour(self):

        self.hour += 1
        
        if self.hour > 23:

            self.hour = 0 
            self.minute = 0
            self.second = 0
    
    def increase_minute(self):

        self.minute += 1

        if self.minute > 59:

            self.minute = 0
            self.increase_hour()
    
    def increase_second(self):

        self.second += 1
        
        time.sleep(1)
        clear_screen()

        if self.second > 59:

            self.second = 0
            self.increase_minute()
    
    def info(self):

        print(f"""
            {self.hour} : {self.minute} : {self.second}
        """)
    
    def is_divided_1_hour(self,second):

        if second % 59 == 0:

            return True
        
        return False
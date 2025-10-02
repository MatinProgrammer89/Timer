from modules import timer
from utills import hour,minute,second

t = timer(hour,minute,second)

while True:

    t.increase_second()
    t.info()
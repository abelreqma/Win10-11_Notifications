# Libraries
from win10toast import ToastNotifier
from datetime import datetime, time as dtime
import random
import time

# GUI
tn = ToastNotifier()

# Icon
picture = "icon.ico"

# Notification Headers
morningtext = ["Morning Header 1", "Morning Header 2", "Morning Header 3", "Morning Header 4", "Morning Header 5"]
noontext = ["Noon Header 1", "Noon Header 2", "Noon Header 3", "Noon Header 4"]
evetext = ["Evening Header 1", "Evening Header 2", "Evening Header 3", "Evening Header 4"]

mornhead = random.choice(morningtext)
noonhead = random.choice(noontext)
evehead = random.choice(evetext)



# Randomized messages
notes = ["note1", "note2", "note 3", "note 4", "note 5", "note 6", "note 7"]

messages = random.choice(notes)

# Times
morningtime = (dtime(0,0), dtime(11,0)) # 12 am - 11 am
noontime = (dtime(11,30), dtime(17,0)) #  11:30 am - 5 pm
eveningtime = (dtime(17,0), dtime(23,59))  # 5 pm - 11:59 pm

# Sleep Timer
sleeper = 12600 # 4 hours

# Output
while True:
  actual_time = datetime.now().time()
  
  if morningtime[0] <= actual_time <= morningtime[1]: 
    tn.show_toast(mornhead, messages, duration=20, icon_path=picture)

  if noontime[0] <= actual_time <= noontime[1]:
    tn.show_toast(noonhead,messages,duration=20, icon_path=picture)

  if eveningtime[0] <= actual_time <= eveningtime[1]:
    tn.show_toast(evehead,messages,duration=20, icon_path=picture)

  time.sleep(sleeper)

from datetime import date

import time

from datetime import datetime

print(f"Print Today Date : '{date.today()}' and datetime : '{datetime.today()}'")

print(f"Print Today Date : '{date.today().day}'")

print(f"Print Today Day : '{date.today().strftime("%A")}'")

print(f"Print Today Day : '{date.today().strftime("%a")}'")

print(f"Print Month In Number : '{date.today().month}'")

print(f"Print Month In Stribg : '{date.today().strftime("%B")}'")

print(f"Print This Year : '{date.today().year}'")

print(f"Print Week In This Month : '{date.today().weekday()}th' Week")

print(f"Print The Current Time in 24 Hrs : '{datetime.now().strftime("%H:%S:%M")}'")

print(f"Print The Current Time In 12 Hrs : '{datetime.now().strftime("%I:%S:%M %p")}'")

print(f"Print The Current Date and Time In 12 Hrs : '{time.ctime()}'")
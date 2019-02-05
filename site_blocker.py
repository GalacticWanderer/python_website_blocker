import time  # for sleep functionality
from datetime import datetime as dt  # for system date and time

# vars to hold host file address, redirect ip and a list of sites to block
hostAddress = "/ect/hosts"
redirect = "127.0.0.1"
website_list = ["www.reddit.com", "reddit.com"]

# using the datetime func, storing the shift start and end time
work_start = dt(dt.now().year, dt.now().month, dt.now().day, 8)
work_end = dt(dt.now().year, dt.now().month, dt.now().day, 16)

#  the while func makes sure the program runs indefinitely
while True:
    #  checking to see if current time is ahead of work start and/end time
    if work_start < dt.now() < work_end:
        print("working hours")
    else:
        print("non working hours")
    #  sleeps for 5 secs before continuing the while loop
    time.sleep(5)

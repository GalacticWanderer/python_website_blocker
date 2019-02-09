import time  # for sleep functionality
import re
from datetime import datetime as dt  # for system date and time

# vars to hold host file address, redirect ip and a list of sites to block
hostAddress = "/etc/hosts"
tempHostAddress = "/home/joy/pythondevelopments/python_website_blocker/hosts"
redirect = "127.0.0.1"
website_list = ["www.reddit.com", "reddit.com", "apple.com", "yahoo.com"]

# using the datetime func, storing the shift start and end time
work_start = dt(dt.now().year, dt.now().month, dt.now().day, 8)
work_end = dt(dt.now().year, dt.now().month, dt.now().day, 16)

#  the while func makes sure the program runs indefinitely
while True:
    #  checking to see if current time is ahead of work start and/end time
    if work_start < dt.now() < work_end:
        print("working hours")

        #  opening up the hosts file as read and writeable and reading the file
        with open(tempHostAddress, 'r+') as file:
            contents = file.read()
            # loop through the website_list and see if it exits on file
            for site in website_list:
                if site in contents:
                    print(site + " is here, passing")
                    pass
                elif site not in contents:
                    print(site + " not here, appending it!")
                    # appending new items on the file
                    file.write(redirect + " " + site+"\n")

    else:
        print("non working hours")
        #  opening the file
        with open(tempHostAddress, 'r+') as file:
            # reading the file as individual lines instead
            contents = file.readlines()
            # moving the pointer to the beginning to the line so we can append
            # to it at the beginning
            file.seek(0)
            # for loop for every line in content
            for line in contents:
                # if not any of the websites from website_list is in line,
                # then write the lines at the "seek point"
                if not any(website in line for website in website_list):
                    print("replacing sites")
                    file.write(line)
            # truncates remove the texts from before
            file.truncate()
        #  sleeps for 5 secs before continuing the while loop
    time.sleep(5)

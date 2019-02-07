import time  # for sleep functionality
from datetime import datetime as dt  # for system date and time

# vars to hold host file address, redirect ip and a list of sites to block
hostAddress = "/etc/hosts"
tempHostAddress = "/home/joy/pythondevelopments/python_website_blocker/hosts"
redirect = "127.0.0.1"
website_list = ["www.reddit.com", "reddit.com", "apple.com", "yahoo.com"]

# using the datetime func, storing the shift start and end time
work_start = dt(dt.now().year, dt.now().month, dt.now().day, 8)
work_end = dt(dt.now().year, dt.now().month, dt.now().day, 22)

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
                    file.write(redirect + " " + site+"\n")

    else:
        print("non working hours")
        #  remove the site lists and the redirect address

    #  sleeps for 5 secs before continuing the while loop
    time.sleep(5)

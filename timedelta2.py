import datetime


td = datetime.timedelta(days=15, hours=32, seconds=45)

print(td)

def timedelta_formatter(td):                             # defining the function
    td_sec = td.seconds    
    print(td_sec)                              # getting the seconds field of the timedelta
    hour_count, rem = divmod(td_sec, 3600)               # calculating the total hours
    minute_count, second_count = divmod(rem, 60)         # distributing the remainders
    msg = "The time difference is: {} days, {} hours, {} minutes, {} seconds".format(td.days,hour_count,minute_count,second_count)
    print (msg)

timedelta_formatter(td)
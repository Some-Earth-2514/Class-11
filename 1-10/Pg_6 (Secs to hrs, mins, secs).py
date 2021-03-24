# WAP to convert seconds to hours, minutes, and seconds
sec = int(input("Enter time in seconds "))
hour = sec/(60*60)
mins = sec/60
secs = mins % 2
print(sec, "seconds =", hour, "hours,", mins, "minutes,", secs, "seconds")

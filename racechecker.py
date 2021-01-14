# racehours as type of integer
# race time og type integr
# raceseconds of type integr
# personal best time of time integer
# raceminutes of type integer

racehours = int(input("enter the race hours"))
raceminutes = int(input("enter the race minutes"))
raceseconds = int(input("enter the race seconds"))
personalbest = int(input("enter the race personal beest time"))

racetime = (racehours * 3600) + (raceminutes * 60) + raceseconds
if personalbest > racetime:
    print("Your new personal best %d " % (racetime))
elif personalbest == racetime:
    print("new time eequal to old time")
else:
    print("not good enough")

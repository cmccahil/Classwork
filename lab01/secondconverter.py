#secondconverter.py
#Translate seconds into a more readable hours, minutes, and second.
#
#Colin McCahill
#09/03/15

print("Welcome to my Second Converter!")

print("This program will properly calculate the number of minutes and seconds under 60 from a given number of seconds")

seconds=eval(input("How many seconds have you got?"))
hours=(seconds//3600)
minutes=((seconds//60)%60)
second=(seconds%60) 

print(seconds,"seconds is equaul to", hours, "hours, ", minutes, "minutes, ", "and", second, "seconds")   

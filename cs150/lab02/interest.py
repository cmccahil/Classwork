#interest.py
#compute the total amount of money in possesion after n months with an initial deposit, monthly interest rate, a monthly deposits, and number of months
#
#Colin McCahill
#09/10/15

print("Welcome to the Interest Calculator!")

initial=eval(input("Enter your initial savings:"))
interest=eval(input("Enter your monthly interest rate:"))
contribution=eval(input("Enter your monthly contribution:"))
months=eval(input("How many months would you like computed:"))

print("Initially you put in $",initial)
for i in range(1,months+1):
    x=initial+(initial*interest)+contribution
    initial=x
    print("After month",i,"you would have $",(int(x*100))/100)



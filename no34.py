num=int(input("entr nmbr"))
digit=num%10
if digit%3==0:
    print("divisible by 3",digit)
else:
    print("not divisible  by 3",digit)
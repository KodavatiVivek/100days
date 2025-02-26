bill = float(input(" Total bill"))
persons=int(input(" No of persons"))
tip = int(input(" percentage of tip"))

total= bill * (1+ tip/100)
each=round(total/persons)

print(f"{each}")
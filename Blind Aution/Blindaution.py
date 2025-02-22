from autionart import logo

def Winner(Bidder_Names):
    highest_value=0
    #winners=max(Bidder_Names,key=Bidder_Names.get)
    win=""
    for Name in Bidder_Names:
        if Bidder_Names[Name]> highest_value:
            highest_value=Bidder_Names[Name]
            win=Name
    print(f"Congratulations to The Winner is {win} as his/her bid is {highest_value}")
    #print(winners)his/her

Bidder_Names= {}
Next= True

print(logo)
while Next:
    print("Welcome to Auction\n")
    print("You can enter name nobody needs to know as it is secret\n")
    Name = input("Please enter your name:\n")
    Value = int(input("Please enter your BID Value for ITEM:$"))
    Bidder_Names[Name]=Value

    Next_member=input("Are there any members still want to participate YES or NO\n").lower()
    if Next_member =="no":
        Next = False
        print("All members are completed\n Wait for the Results")
        Winner(Bidder_Names)
    elif Next_member =="yes":
        print("\n" * 30)





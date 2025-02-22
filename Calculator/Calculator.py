import CalArt

def add(n1,n2):
    return n1 + n2
def Subract(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations={
    "+": add,
    "-": Subract,
    "*": multiplication,
    "/": divide
}

def Calculator():
    print(CalArt.logo)
    should_accumulate = True
    num1=float(input("Enter the 1st number:\n"))

    while should_accumulate:
        for sym in operations:
            print(sym)
        operate = input("Enter the Operations\n:")
        num2=float(input("Enter the 2nd number:\n"))
        answer= operations[operate](num1,num2)
        print(f"{num1} {operate} {num2}={answer}")

        choice = input(f"Type 'Y' to continue in {answer},'N' to exit:\n ").lower()

        if choice=="n":
            should_accumulate = False
            Calculator()
        else:
            num1=answer

Calculator()


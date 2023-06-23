import math

# This def function outlines the first thing that the user will see on their interface
def opening():
    print("Below are two possible calculators to use to determine values at their time of maturity. Please select which one you'd like by either typing 'investment' or 'bond'.\n")

    print("Investment Calculator - to calculate the amount of interest you'll earn on your investment.\n")

    print("Bond Calculator - to calculate the amount you'll have to pay on a home loan.\n")


# Now I am integrating the 'opening' function
opening()

# This def function outlines the choice made by the user; I have used the strip() function to remove any additional spaces that may affect the code.
def make_choice():
    choice = input("Which calculator would you like to access? ")
    if choice.lower().strip() == "investment":
        investment_calculations()
    elif choice.lower().strip() == "bond":
        bond_calculations()
    else:
        print("Please enter the choice again, taking care not to add any capital letters, additional spaces or symbols.")

# I am now acquiring the different values to be inserted into the investment calculator; depending upon what is entered, the relevant calculator will be applied.
def investment_calculations():
    P = float(input("How much are you looking to deposit? "))
    R = float(input("What is the annual interest rate of return, excluding the '%' sign? "))
    T = float(input("How many years are you looking to invest for? "))
    interest = input("Would you like to calculate simple or compound interest? ")
    if interest.lower().strip() == "simple":
        simple_interest(P, R, T)
    elif interest.lower().strip() == "compound":
        compound_interest(P, R, T)
    else:
        print("This is not an available option. Please enter your choice again.")

# I am now outlining the calculation methods; note the change in capitalisation of P compared to p, and so on.
def bond_calculations():
    p = float(input("What is the present value of the house? "))
    i = float(input("What is the annual interest rate? "))
    n = float(input("Over how many months do you intend to repay the bond? "))
    bond(i, p, n)

# I am now defining the calculation methods for each of the investment types.
def simple_interest(P, R, T):
    interest = (R / 100)
    A = P*(1 + interest*T)
    print(A)

# I am now defining the equation for the compound interest equation
def compound_interest(P, interest_parameter, T):
    interest = (interest_parameter/100)
    A = P * math.pow((1+interest),T)
    print(A)

# I am now defining the equation for the bond equation
def bond(i, p, n):
    monthly_interest = (i / 100)/12
    repayment = (monthly_interest * p)/(1 - (1+monthly_interest)**(-n))
    print(repayment)

# Now I am calling upon the 'make_choice' function, after having defined everything else, as the program seems to be dependent on defining everything first
make_choice()
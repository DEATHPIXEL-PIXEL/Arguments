totalbill=( float (input("Enter your bill  :  ")))
tip=( float(input("Enter your pertcentage of the tip you want to pay  :  ")))



def finalbill(totalbill,tip):
    finalbill=totalbill+(tip/100*totalbill)
    print("The total bill, along with the tip is" , finalbill)


finalbill(totalbill,tip)

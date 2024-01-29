
def calculateWorking(startAge, initialAmt, working):
    endAge = startAge + working[0]
    x = range(startAge, endAge)
    monthlyDeposit = (working[1])
    monthlyReturns = 0
    balance = initialAmt
   
    for i in x:
        yrs= i//12
        mths = i%12
        print('Age {:2d} month {:2d} you have ${:.2f}' .format(yrs, mths, balance))
        monthlyReturns = (balance * 0.045)/12
        balance = balance + monthlyReturns + monthlyDeposit
        pass
    return balance
    
   

def calculateRetired(rStartAge, initialAmt, retired):
    endAge = retired[0]
    x = range(rStartAge, rStartAge+endAge)
    monthlyWithdrawals = retired[1]
    rateOfReturn = retired[2]
    monthlyReturns= 0 
    balance = initialAmt
    
    for i in x:
        yrs= i//12
        mths = i%12
        print('Age {:2d} month {:2d} you have ${:.2f}' .format(yrs, mths, balance))
        monthlyReturns = (balance * rateOfReturn)
        balance= balance + monthlyReturns + monthlyWithdrawals
        pass
    pass



def calculateRetirement(start_age, initial, working, retired):
    amountAtRetirement= calculateWorking(start_age, initial, working)
    calculateRetired(start_age + working[0], amountAtRetirement, retired)
    pass



def main():
    working=(489,1000,0.045/12)
    retired=(384,-4000, 0.01/12)
    calculateRetirement(327, 21345, working, retired)
    pass

if __name__ == "__main__":
    main()
    pass


'''
Function to calculate the price of a European Call Option using basic Black-Scholes theory
'''

# Convert days to expiry into a yearly figure
def daysToYears(days):
    return(days/365)

def evaluateCall(spotPrice,strikePrice,timeToExpiry,riskFreeRate,sigma):
    dOne = (np.log(spotPrice/strikePrice) + (riskFreeRate + (0.5*sigma**2)*(timeToExpiry)))/(sigma*np.sqrt(timeToExpiry))
    dTwo = (np.log(spotPrice/strikePrice) + (riskFreeRate - (0.5*sigma**2)*(timeToExpiry)))/(sigma*np.sqrt(timeToExpiry))
    
    dist1 = norm.cdf(dOne)
    dist2 = norm.cdf(dTwo)
    
    timeDiscount = np.exp(-riskFreeRate*timeToExpiry)
    
    return(spotPrice*dist1 - (strikePrice*timeDiscount*dist2))


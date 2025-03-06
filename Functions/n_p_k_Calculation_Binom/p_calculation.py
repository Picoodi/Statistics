#Function for calculating the p of the binomial distribution
#We need the parameter n and the probability of k = 0

def p_calculation_binomial(n,k_0):
    p = round( 1- (k_0**(1/n)), 8)
    return p





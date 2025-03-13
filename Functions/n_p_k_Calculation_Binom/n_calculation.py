#Function for calculating the n of the binomial distribution
#We need the parameter p and the k and the probability for k
#If we know the value for k = 0
#But we need the input in the fom 1-P(X = k) =>  probability


from math import log, ceil, factorial
from scipy.stats import binom


def n_calculation_binomial(p,k, k_prob):

    if k == 0:
        n = log(1-k_prob, 1-p)
        return ceil(n)
    else:
        n = k  # Minimum trials to have k successes
        while True:
            prob = 1 - binom.cdf(k - 1, n, p)
            if prob >= k_prob:
                return n
            n += 1


print(n_calculation_binomial(0.234, 0, 0.99)) #tescase k = 0
print(n_calculation_binomial(0.45, 3, 0.921456))
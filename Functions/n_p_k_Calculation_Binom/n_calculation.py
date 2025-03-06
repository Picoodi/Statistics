#Function for calculating the n of the binomial distribution
#We need the parameter p and the k and the probability for k

#But we need the input in the fom 1-P(X = k) =>  probability

#And we have to try to get to the right value with trying
#Only if k = 0 we can calculate it directly


from math import log, ceil


def n_calculation_binomial(p,k, k_prob):

    if k == 0:
        n = log(1-k_prob, 1-p)
        return ceil(n)

    else:
        pass #implement here



print(n_calculation_binomial(0.234, 0, 0.99)) #tescase k = 0
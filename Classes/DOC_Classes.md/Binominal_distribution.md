# Binominalverteilung -> Binominal distribution
The binominal distribution has different calculations and different functions than the RandomVariable. It is getting used when u have a you have an experiment that only has the 2 outcomes like True or False. When you do that over and over behind you get a Bernoulli-Chain and then again with a $W(X)$ you can give it real numbers as a solution.  
In tasks it often says the experiment is B(n,p) or B(n,p,k) distributed. The n is the n amount of how often the experiment was run through p is the probability of a hit or True in the experiment and k the probability you want to find with k hits or Trues.  
Only a name, n and p need to be initialized to create the class. The name is optinal for you, but you need to insert one even if its an empty string "".
```python
class Binominalverteilung():
    def __init__(self,name,n,p):
        self.name = name
        self.n = n
        self.p = p
```

## Wahrscheinlichkeitsverteilung -> Probability distribution 
With the binomial coefficient $$P(X=k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$ we can calculate the probability for each k.

```python
def Wahrscheinlichkeitsverteilung(self):
        k = 0
        Pxi = [] #list to store the probabilities
        while k <= self.n: #iteratin thorugh each k
            binom = (factorial(self.n))/((factorial(k)) * (factorial(self.n-k))) #binominal coefficient
            P = binom * (self.p**k) * ((1-self.p)**(self.n-k)) # probaility for the k
            Pxi.append(P)
            k = k+1
        return Pxi
```


## Kumulative Verteilungsfunktion / Cumulative Probability distribution
The cumulative Probability distribution adds all the probabilities up to the given k and thats what we implement in the code aswell.
```python
def kumulative_Verteilungsfunktion(self):
        Pxi = self.Wahrscheinlichkeitsverteilung() # calculating the probabilites for each k alone
        sum = 0
        kWF = [] #list with all cumulative probabilities
        for element in Pxi:
            sum = sum + element #adding all the probabilites up to the given k
            kWF.append(sum)
        return kWF
```
## RangeProbability
Just like the name says this function lets the user calculate the prbability in a specific range the user wants to
```python
def RangeProbability(self,Start, End):
        i = Start
        sum = 0
        while i <= End: #caclulating the probabilities and adding them each time to the whole sum
            sum = sum + self.Wahrscheinlichkeitsverteilung()[i] 
            i = i+1
        return sum
```


## Erwartungswert, Varianz and Standardabweichung
These little functions of the class return the simple math behind it in one line of code in each function 
```python
    def Erwartungswert(self):
        return self.n * self.p #n * p

    def Varianz(self):
        return self.n * self.p * (1- self.p) # n*p*(1-p)

    def Standardabweichung(self):
        return sqrt(self.Varianz()) # Square root of the Varianz
```
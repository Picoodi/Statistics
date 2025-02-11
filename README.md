# Statistics

# Zufallsgröße und Wahrscheinlichkeitsverteilung (Random Variables and Probability Distribution)

This codebase contains classes for random variables and the binominal distribution. The code was built to help me and my classmates to check our experiments and calculations in math class. Because I went to school in germany the function names are german but I will comment everything in englisch and also this ReadMe will be in Englisch.

### Translations
Here are the best translations for the german words i could find.

 
Binominalverteilung -> Binominal distribution
Erwartngswert -> Expected value
Histogramm -> Histogram   
kumulative Wahrscheinlichkeitsverteilung -> Cumulative Probability distribution  
Stabdiagramm -> Bar diagram
Standardabweichung -> Standard deviation     
Tabelle ->Table  
Treppenfunktion -> Staircase function 
Varianz -> Variance   
Wahrscheinlichkeitsverteilung -> Probability distribution 
Zufallsgröße -> RandomVariables 

# Needed Libraries 
Check that you have the following librairies installed. They are needed for the mathematics and valuable and good looking outputs.
```pyhton
import matplotlib.pyplot as plt
from math import sqrt, factorial
from prettytable import PrettyTable
from binarytree import build 
```

# Class Zufallsgröße / RandomVariables (ZG/RV)
In Mathematics you use a ZG/RV  when you want every solution of a random experiment $\omega = \Omega$ as a real number. The variable $x_i$ represents all possible real numbers you get. You give your ZG/RV a name with an uppercase letter like $X$.  
The class takes a Name, the real numbers of $x_i$ (WerteZG) and the corresponding probabilites(WSKWerteZG). Note that both lists need to have the same amonts of elements. The name is optinal for you, but you need to insert one even if its an empty string "".
```python  
class Zufallsgröße():

    def __init__(self, Name, WerteZG, WSKWerteZG):
        self.Name = Name
        self.xi = WerteZG
        self.Pxi = WSKWerteZG
```
Here is an example for a simple experiment like a dice
```python  
X = Zufallsgröße("X",[1,2,3,4,5,6] ,[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
```




## WerteZufallsgröße / ValuesRandomVariables
This is a simple function that returns your inputed $x_i$ values. For the dice that would be 
```pyhton
[1,2,3,4,5,6]
```
## Wahrscheinlichkeitsverteilung / Probability distribution (WV/PD)
This function $W(X)$ is there to show you how all the probabilities are distributed like the name already says. It returns a list with your probabilitis which here is just the input list. In mathematics that would be $P(X=x_i)$.
```python
[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
```


## Stabdiagramm / Bar diagram
This function creates a visual bar diagramm with the help of matplotlib and shows it to the user in an extra window. It takes the self arguments for the neccesary data and labels of the graph.
```python
def Stabdiagramm(self):
        plt.figure() #creates a new figure in matplotlib
        plt.bar(self.xi, self.Pxi, width= 0.1) # bar graph with the xi and Pxi 
        plt.get_current_fig_manager().set_window_title("Stabdiagramm W("+self.Name+")")
        plt.title("Stabdiagramm W("+self.Name+")")
        plt.xlabel("xi")
        plt.ylabel("P("+ self.Name+"= xi)")
        plt.show(block = False)# block is false so mltiple windows can be created
```
There is an example in the picture files.


## Histogram 
The histogramm is like the bar diagramm but it gives you the option to change how thick the bars will be with the one parameter the function takes.
```python
def Histogramm(self, Rechteckbreite):
        # calculating each height vor every bar with the given bar width (Rechteckbreite)
        heights = []
        for element in self.Pxi:
            height = element / Rechteckbreite
            heights.append(height)

        plt.figure() #creates a new figure in matplotlib
        plt.bar(self.xi, heights, width= Rechteckbreite) # bar graph with the xi and the calculated heights
        plt.get_current_fig_manager().set_window_title("Histogramm("+self.Name+")")
        plt.title("Histogramm W("+self.Name+")")
        plt.xlabel("xi")
        plt.ylabel("P("+ self.Name+"= xi)")
        plt.grid()
        plt.show(block = False) # block is false so mltiple windows can be created
```
There is an example in the pictre files.


## Kumulative Verteilungsfunktion / Cumulative Probability distribution
This function is there for the mathematical expression $F(X) = P(X \leq x_i)$. 
It simply means you add all probabilities before and including the $x_i$ element together. 
You do that for every element and then the function returns a list.

```python
def kumulative_Verteilungsfunktion(self):
        VerteilungsfunktionWerte = []
        VerteilungsfunktionWerte.append(self.Pxi[0])
        # we add the first prbability of the experiment cause there is nothing to calculate. Thats why i = 1 and not 0.

        i = 1
        while i < len(self.Pxi): # always adding the next element until we are done
                Wert = self.Pxi[i] + VerteilungsfunktionWerte[i-1] 
                VerteilungsfunktionWerte.append(Wert)
                i = i+1

        return VerteilungsfunktionWerte


#An example return
[0.3, 0.8, 0.9, 1.0]
```
Note that the sum of all probabilities, the last element is always 1.



## Treppenfunktion / Step function
Here again we use matplotlib librarie for nice visuals. The step function shows the cumulative probabilities for each $x_i$ element and the jumps are the probability of the $x_i$ elements.
```python
def Treppenfunktion(self):
    x = self.xi
    F = self.kumulative_Verteilungsfunktion() # the cumulative values as y coordinates 

    plt.figure()
    plt.step(x,F, where= "post", color= "red") #step function of matplotlib with xi and Fxi
    plt.scatter(x,F, color ="red", s= 100) #s is size of the dots, also can be left out 
    plt.get_current_fig_manager().set_window_titel("Treppenfunktion T("+self.Name+")")
    plt.title("Treppenfunktion T("+self.Name+")")
    plt.xlabel("xi")
    plt.ylabel("T("+ self.Name+")")
    plt.grid() #grid for nice visual
    plt.show(block= False)
```
There is an example in the pictre files.



## Ewartungswert / Expected value
The Expected value function returns a number which shows you the most expected and most likely number to happen in your experiment each round if nothing changes. You calculate it with 
$$\mu = E(X) = x_1 \cdot P(X= x_1) + x_2 \cdot P(X = x_2)+\dots = \sum_{i = 1}^{n} x_i \cdot P(X = x_i)$$
We use the sum apprach also in the code by iterating through each $x_i$ and sum up the values.

```python
def Erwartungswert(self): #iterating thorugh each xi value and adding the solution to the expected value
        E = 0
        i = 0
        while i <  len(self.xi): 
            E = E + self.xi[i] * self.Pxi[i] 
            i = i+1

        return E
```

## Varianz / Variance 
The variance uses the expected Value and uses the formula 
$$Var(X) = (x_1-\mu )^2 + P(X=x_1) + (x_2-\mu )^2 + P(X=x_2) + ... + (x_n-\mu )^2 + P(X=x_n)$$
The bigger the variance is the riskier the game is.
```python

def Varianz(self): #iterating thorugh each xi value and adding the solution to the variance
        E = self.Erwartungswert() #need to expected value for the calculation
        i = 0
        V = 0
        while i < len(self.xi):
            V = V + (self.xi[i] - E)**2 * self.Pxi[i]
            i = i +1

        return V
```


## Standardabweichung / Standard deviation
The standard deviation shows you how much the x_i values spread from the middle value on average
and is getting calculated with$$ \sigma = \sqrt{Var(X)}$$
```python
def Standardabweichung(self): # just returns the simple calculation
        return sqrt(self.Varianz())
```


## Tabelle / Table
Table is an extra function that has no mathematics in it. It returns a table with all the most important data of the Random Variable.  
Here is an example how it could look.
```python
Tabelle für die Zufallsgröße X
+------------+----------------------+
|    Was     |        Werte         |
+------------+----------------------+
|     xi     |     [1, 2, 3, 4]     |
|  P(X= xi)  | [0.3, 0.5, 0.1, 0.1] |
| P(X <= xi) | [0.3, 0.8, 0.9, 1.0] |
|    E(X)    |         2.0          |
|   Var(X)   |         0.8          |
|  {sigma}   |  0.8944271909999159  |
+------------+----------------------+
```






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
With the binominal coefficient $$P(X=k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$ we can calculate the probability for each k.

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


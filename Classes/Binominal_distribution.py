import matplotlib.pyplot as plt
from math import sqrt, factorial
from prettytable import PrettyTable
from binarytree import build


class Binominalverteilung():
    def __init__(self,name,n,p):
        self.name = name
        self.n = n
        self.p = p

    def Wahrscheinlichkeitsverteilung(self):
        k = 0
        Pxi = []
        while k <= self.n:
            binom = (factorial(self.n))/((factorial(k)) * (factorial(self.n-k)))
            P = binom * (self.p**k) * ((1-self.p)**(self.n-k))
            Pxi.append(P)
            k = k+1
        return Pxi

    def kumulative_Verteilungsfunktion(self):
        Pxi = self.Wahrscheinlichkeitsverteilung()
        sum = 0
        kWF = []
        for element in Pxi:
            sum = sum + element
            kWF.append(sum)
        return kWF

    def Binary_Tree(self):
        values=["Root"]
        i =0
        while i < (2**self.n)-1:
            values.append(self.p)
            values.append(1-self.p)
            i = i+1

        root = build(values)
        print(root)


    def Histogramm(self, Rechteckbreite):
        Pxi = self.Wahrscheinlichkeitsverteilung()
        heights = [p / Rechteckbreite for p in Pxi]
        plt.figure()
        plt.bar(list(range(self.n + 1)), heights, width=Rechteckbreite)
        plt.get_current_fig_manager().set_window_title("Histogramm("+self.name+")")
        plt.title("Histogramm W("+self.name+")")
        plt.xlabel("xi")
        plt.ylabel("P("+ self.name+"= xi)")
        plt.grid()
        plt.show(block = False)


    def Treppenfunktion(self):
        x = []
        i = 0
        while i <= self.n:
            x.append(i)
            i = i+1
            
        F = self.kumulative_Verteilungsfunktion()

        plt.figure()
        plt.step(x,F, where= "post", color= "red")
        plt.scatter(x,F, color ="red", s= 5)
        plt.get_current_fig_manager().set_window_title("Treppenfunktion T("+self.name+")")
        plt.title("Treppenfunktion T("+self.name+")")
        plt.xlabel("xi")
        plt.ylabel("T("+ self.name+")")
        plt.grid()
        plt.show(block= False)
    
        
        
    def Tabelle(self):
        table = PrettyTable()
        x = []
        i = 0
        while i <= self.n:
            x.append(i)
            i = i+1

        table.field_names = ["Was","Werte"]
        table.add_row(["xi", x])
        table.add_row(["P("+self.name+"= xi)", self.Wahrscheinlichkeitsverteilung()])
        table.add_row(["P("+ self.name+" <= xi)", self.kumulative_Verteilungsfunktion()])
        table.add_row(["E(" + self.name + ")", self.Erwartungswert()])
        table.add_row(["Var(" + self.name + ")", self.Varianz()])
        table.add_row(["{sigma}", self.Standardabweichung()])

        print("Tabelle für die Zufallsgröße "+ self.name)
        print(table)


    def RangeProbability(self,Start, End):
        i = Start
        sum = 0
        while i <= End:
            sum = sum + self.Wahrscheinlichkeitsverteilung()[i]
            i = i+1
        return sum


    def Erwartungswert(self):
        return self.n * self.p

    def Varianz(self):
        return self.n * self.p * (1- self.p)

    def Standardabweichung(self):
        return sqrt(self.Varianz())



X = Binominalverteilung("X", 5, 0.35)
X.Tabelle()
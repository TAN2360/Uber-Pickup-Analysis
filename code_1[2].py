import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data=pd.read_csv("C:/Users/komal/OneDrive/Desktop/uber-raw-data-sep14.csv")


print("-----------------------------UBER TRIPS ANALYSIS----------------------------------")
print("-------------------------------WELCOME PAGE--------------------------------------")
print(" 1. Plotting no. of trips daywise")
print(" 2. Plotting the no. of trips hour wise in the whole month")
print(" 3. Viewing density of uber trips acccording to the regions of New York City")
print(" 4. exit")



ch=int(input("Enter your choice:"))
if (ch == 1):
    d = {}
    for i in data["Date/Time"]:
        x = i.split()
        if(x[0] in d):
            d[x[0]] = d[x[0]]+1
        else:
            d[x[0]] = 1
    print("here")
    x = []
    y = []
    for i in d:
        x.append(i)
        y.append(d[i])
    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('trips daywise')
    plt.show()

elif (ch == 2):
    d = {}
    for i in data["Date/Time"]:
        x = i.split()
        y = x[1].split(":")
        if(y[0] in d):
            d[y[0]] = d[y[0]]+1
        else:
            d[y[0]] = 1
    x = []
    y = []
    for i in d:
        x.append(i)
        y.append(d[i])
    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('trips hourwise in the month of september')
    plt.show()
elif (ch == 3):
    d = {}
    xl = []
    yl = []
    for i in data["Date/Time"]:
        x = i.split()
        xl.append(x[0])
        yl.append(x[1])
    plt.plot(xl, yl)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('density of uber trips')
    plt.show()
else:
    print("enter a valid choice")
    

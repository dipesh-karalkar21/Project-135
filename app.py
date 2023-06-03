import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("new.csv")

name = df["Name"].to_list()
dist = df["Distance"].to_list()
mass = df["Mass"].to_list()
rad = df["Radius"].to_list()
g = df["Gravity"].to_list()

plt.bar(name , mass)
plt.show()
plt.bar(name , rad)
plt.show()
plt.bar(name , dist)
plt.show()
plt.bar(name , g)
plt.show()

import pandas as pd
import seaborn as sns
import random
import numpy as np
import matplotlib.pyplot as plt

# Calculate distance using integral of velocity
def distance(velocity, T):
    distance = 0;
    for i in range(len(velocity-1)):
        distance = distance + velocity(i)*T;
    return distance

def average(input_list):
    return sum(input_list)/len(input_list)

def linear_timeplot(units, data_list, period):
    sns.set(style="darkgrid")
    data_matrix = [[i*period, data_list[i]] for i in range(len(data_list))]
    headers = ["time", units]
    df = pd.DataFrame(data_matrix, columns= headers)
    g = sns.relplot(x= "time", y= units, kind="line", data=df)
    g.fig.autofmt_xdate()
    plt.show()

data_list = [random.random() for i in range(10)]
linear_timeplot("speed", data_list, 0.5)
import pandas as pd
import matplotlib.pyplot as plt
import os

from matplotlib.pyplot import figure

from components.data_load import load_data
paths="./artifacts/charts"

def save_bar(series,title,filename,xlabel=" ",ylabel="count"):
    figure(figsize=(10,10))
    series.plot(kind="bar",rot=0)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(os.path.join(paths,filename))
    plt.close()

def save_hist(series,title,filename,bin=20):
    plt.hist(series,bins=bin)
    plt.xlabel("Age")
    plt.title(title)
    plt.savefig(os.path.join(paths,filename))
    plt.close()

def save_stacked_bar(crossbar,title,filename):
    crossbar.plot(kind="bar",stacked=True,rot=0)
    plt.title(title)
    plt.savefig(os.path.join(paths,filename))
    plt.close()



def save_charts(data:pd.DataFrame):


    save_bar(data["Attrition"].value_counts(),title="Attrition counts",
             filename="bar_plot")
    save_hist(data["Age"],title="Age Distribution",filename="histogram")
    save_stacked_bar(pd.crosstab(index=data["OverTime"],columns=data["Attrition"]),
                     title="OverTime VS Attrition",filename="Stacked_bar")

def main():
    data=load_data()
    save_charts(data)

if __name__=="__main__":
    main()
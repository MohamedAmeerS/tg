import pandas as pd
from components.data_load import load_data
import os
paths="./artifacts/reports"


def eda_operations(data:pd.DataFrame):
    print("\n"+"="*102)
    print("Exploratory Data Analysis".center(102))
    print("="*102)
    print("Shape of the data :",data.shape,"\n"+"-"*len("Shape of the data"))
    print("_" * 70)
    print("Data description\n"+"-"*len("Data description"))
    print(data.describe())
    print("_" * 70)
    print("Target data Attrition\n"+"-"*len("Target data Attrition"))
    print(data["Attrition"].value_counts())
    print("_" * 70)
    print("Balance vs unbalanced\n"+"-"*len("Balance vs unbalanced"))
    print(data["Attrition"].value_counts(normalize=True)*100)
    print("_"*70)
    print("Crosstab","\n"+"-"*len("Crosstab"))
    print(pd.crosstab(data["OverTime"],data["Attrition"]))
    print("_" * 70)

    with open(os.path.join(paths,"data_summary.txt"),"w") as file:
        file.write("=" * 102)
        file.write("\nExploratory Data Analysis".center(102))
        file.write("\n"+"=" * 102)
        file.write(f"\nShape of the data : {data.shape}")
        file.write("\n" + "-" * len("Shape of the data"))
        file.write("\n"+"_" * 70)
        file.write("\nData description\n" + "-" * len("Data description"))
        file.write("\n")
        file.write(data.describe().to_string())
        file.write("\n"+"_" * 70)
        file.write("\nTarget data Attrition\n" + "-" * len("Target data Attrition"))
        file.write("\n")
        file.write(data["Attrition"].value_counts().to_string())
        file.write("\n"+"_" * 70)
        file.write("\nBalance vs unbalanced\n" + "-" * len("Balance vs unbalanced"))
        file.write("\n")
        file.write(str(data["Attrition"].value_counts(normalize=True) * 100))
        file.write("\n"+"_" * 70)
        file.write("\nCrosstab")
        file.write("\n" + "-" * len("Crosstab"))
        file.write("\n")
        file.write(str(pd.crosstab(data["OverTime"], data["Attrition"])))
        file.write("\n"+"_" * 70)


def main():
    data=load_data()
    eda_operations(data)

if __name__=="__main__":
    main()
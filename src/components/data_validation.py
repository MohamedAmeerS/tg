import pandas as pd
from components.data_load import load_data





def dataset_check(data:pd.DataFrame):
    print("*"*30)
    print("Dataset Overview".center(30))
    print("*" * 30,"\n")

    print("Shape of the data :",data.shape,"\n","_"*30)
    print("Names of columns".center(30),'\n',"_"*30)
    print(data.columns.tolist(),"\n","_"*30)
    print("Null Values".center(30), '\n', "_" * 30)
    print(data.isna().sum(), "\n", "_" * 30)
    print("Duplicated values".center(30), '\n', "_" * 30)
    print(data.duplicated().sum(), "\n", "_" * 30)


def main():
    data=load_data()
    dataset_check(data)

if __name__=="__main__":
    main()
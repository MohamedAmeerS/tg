import pandas as pd
def load_data():
    data=pd.read_csv("DATA/RAW/HR-Employee-Attrition.csv")

    return data


if __name__=="__main__":
    data=load_data()
    print("Top 5 rows")
    print(data.head(), "\n", "_" * 40)
    print("rows and columns")
    print(data.shape, "\n", "_" * 40)
    print("data info")
    print(data.info(), "\n", "_" * 40)
    print("data description")
    print(data.describe(), "\n", "_" * 40)
    print(data.describe(include="O"), "\n", "_" * 40)
    print("null values")
    print(data.isna().sum(), "\n", "_" * 40)

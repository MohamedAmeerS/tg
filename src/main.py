from data_load import load_data
def main():
    data=load_data()
    print("Top 5 rows")
    print(data.head( ),"\n","-"*40)
    print("shape of the data")
    print(data.shape,"\n","-"*40)

if __name__==__main__:
    main()
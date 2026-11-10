from components.data_load import load_data
from components.data_validation import dataset_check
from components.eda import eda_operations
def main():
    data=load_data()
    dataset_check(data)
    eda_operations(data)


if __name__=='__main__':
    main()
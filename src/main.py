from components.data_load import load_data
from components.data_validation import dataset_check
from components.eda import eda_operations
from components.visualizations import save_charts
def main():
    data=load_data()
    dataset_check(data)
    eda_operations(data)
    save_charts(data)


if __name__=='__main__':
    main()
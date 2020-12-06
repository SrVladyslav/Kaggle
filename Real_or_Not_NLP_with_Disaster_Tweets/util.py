"""
File that contain all the util functions for data preprocessing and more
"""
import pandas as pd 


DATA_PATH = './data/'

def read_data():
    """
    :return x_train, y_train, x_test, y_test: return the data from the CSV
    """
    X_train = pd.read_csv(DATA_PATH+'train.csv', index_col= 0)
    print(X_train.head())
    

read_data()

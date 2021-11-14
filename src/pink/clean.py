# from pink import hw5
# dataset = hw5.read_data("sample_diabetes_mellitus_data.csv")

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

## b. Split the data between train and test. (you can use train_test_split from sklearn or any other way)
def split(name_dataset, prop_test):
    return train_test_split(name_dataset, test_size = prop_test)

# trainset, testset = split(name_dataset = dataset, prop_test = 0.1)

## c. Remove those rows that contain NaN values in the columns: age, gender, ethnicity.

def drop_nas_in_cols(name_dataset, name_columns):
    for x in name_columns:
        name_dataset = name_dataset[name_dataset[x].notnull()]
    return name_dataset

# ncols = ['age', 'gender', 'ethnicity']
# testset = drop_nas_in_cols(testset, ncols)
# trainset = drop_nas_in_cols(trainset, ncols)

## d. Fill NaN with the mean value of the column in the columns: height, weight.

def impute_mean_in_cols(name_dataset, name_columns):
    for x in name_columns:
        dummy = name_dataset[x].isnull()
        name_dataset[x][dummy]=name_dataset[x].mean()
    return name_dataset

# testset = impute_mean_in_cols(testset, ['height', 'weight'])
# trainset = impute_mean_in_cols(trainset, ['height', 'weight'])

## e. Generate dummies for ethnicity column (One hot encoding)

def gen_dummies_to_cols(name_dataset, name_columns):
    name_dataset = pd.get_dummies(name_dataset, columns = name_columns,
                                  drop_first = True)
    return name_dataset

# testset = gen_dummies_to_cols(testset, ['ethnicity'])
# trainset = gen_dummies_to_cols(trainset, ['ethnicity'])

## f. Create a binary variable for gender M/F

def gen_binary_to_cols(name_dataset, name_columns):
    for x in name_columns:
        val = list(name_dataset[x].unique())[0]
        name_dataset[x] = np.where(name_dataset[x] == val, True, False)
    return name_dataset

# testset = gen_binary_to_cols(testset, ['gender'])
# trainset = gen_binary_to_cols(trainset, ['gender'])
# Import pandas
import pandas as pd

# Load dataset
cc_apps = pd.read_csv('datasets/cc_approvals.data', header=None)
# Inspect data.
print(cc_apps.head())

# Print summary statistics
cc_apps_description = cc_apps.describe()
print(cc_apps_description)
print("\n")
# Print DataFrame information
cc_apps_info = cc_apps.info()
print(cc_apps_info)
print("\n")
print(cc_apps.tail(17))


# Handling missing values
# Import numpy
import numpy as np
# Inspect missing values in the dataset
print(cc_apps.tail(17))
# Replace the '?'s with NaN
cc_apps = cc_apps.replace("?", np.NaN)
# Inspect the missing values again
print(cc_apps.tail(17))
# Impute the missing values with mean imputation
cc_apps.fillna(cc_apps.mean(), inplace=True)
# Count the number of NaNs in the dataset to verify
cc_apps.isnull().sum()

# Iterate over each column of cc_apps fill the empty column of each with max value
for col in cc_apps:
    # Check if the column is of object type
    if cc_apps[col].dtypes == 'object':
        # Impute with the most frequent value
        cc_apps = cc_apps.fillna(cc_apps[col].value_counts().index[0])

# Count the number of NaNs in the dataset and print the counts to verify
cc_apps.isnull().sum()

# Import LabelEncoder
from sklearn.preprocessing import LabelEncoder

# Instantiate LabelEncoder
le = LabelEncoder()

# Iterate over all the values of each column and extract their dtypes
for col in cc_apps:
    # Compare if the dtype is object
    if cc_apps[col].dtypes=='object':
    # Use LabelEncoder to do the numeric transformation
        cc_apps[col]=le.fit_transform(cc_apps[col])

 # Import train_test_split
from sklearn.model_selection import train_test_split

# Drop the features 11 and 13 and convert the DataFrame to a NumPy array
cc_apps = cc_apps.drop([11, 13], axis=1)
cc_apps = cc_apps.values

# Segregate features and labels into separate variables
X,y = cc_apps[:,0:13] , cc_apps[:,13]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,
                                y,
                                test_size=0.33,
                                random_state=42)



import scipy.io
import numpy as np
import pandas as pd


# Load the .mat file
mat_contents = scipy.io.loadmat('/Users/stefanodegiorgis/Desktop/FEP/src/matlab.mat')

data = mat_contents.keys()

df = pd.DataFrame(data)

#print(df)

# Access the MDP data directly
mdp_data = mat_contents['MDP']


# Access the 'F' field
F_data = mdp_data['F'][0, 0]  # The indexing [0, 0] is used because your ndarray shape is (1, 30)

# Inspect the type and shape of F_data
print(type(F_data))
if isinstance(F_data, np.ndarray):
    print("Shape of F_data:", F_data.shape)


if isinstance(F_data, np.ndarray) and len(F_data.shape) == 2:  # Simple 2D array check
    df_F = pd.DataFrame(F_data)
    print(df_F.head())  # Print the first few rows to inspect


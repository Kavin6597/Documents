import numpy as np
import pandas as pd
import os
import string
from string import digits
import matplotlib.pyplot as plt
%matplotlib inline
import re
import seaborn as sns
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.layers import Input, LSTM, Embedding, Dense
from keras.models import Model

# Read the CSV file
lines = pd.read_csv("Hindi_English_Truncated_Corpus.csv", encoding='utf-8')

# Filter the data for 'ted' as the source
lines = lines[lines['source'] == 'ted']

# Remove rows with null values in the 'english_sentence' column
lines = lines[~pd.isnull(lines['english_sentence'])]

# Drop duplicate rows
lines.drop_duplicates(inplace=True)

# Shuffle the dataset and select 25000 rows
lines = lines.sample(n=25000, random_state=42)

# Print the shape of the dataset
print(lines.shape)
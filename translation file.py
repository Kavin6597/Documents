import numpy as np # linear algebra
import pandas as pd # data processing

import os
import string
from string import digits
import matplotlib.pyplot as plt
import re

import seaborn as sns
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.layers import Input, LSTM, Embedding, Dense
from keras.models import Model

lines=pd.read_csv("Hindi_English_Truncated_Corpus.csv",encoding='utf-8')
lines=lines[lines['source']=='ted']
lines=lines[~pd.isnull(lines['english_sentence'])]
lines.drop_duplicates(inplace=True)
# Let us pick any 25000 rows from the dataset
lines=lines.sample(n=25000,random_state=42)
lines.shape
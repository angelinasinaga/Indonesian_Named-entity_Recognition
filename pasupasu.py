# -*- coding: utf-8 -*-
"""Pasupasu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16BS9vk9--jq8UKychzEwbpqlqJftv3HI

## **1. LOAD DATA** ##

**1.1 Import Libraries**
"""

#Data analysis   
import pandas as pd 
import numpy as np
import csv
import nltk
import tensorflow as tf

# Commented out IPython magic to ensure Python compatibility.
#Data visualisation 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
sns.set(font_scale=1)
# %matplotlib inline
from matplotlib import ticker
# %config InlineBackend.figure_format = 'svg'

#Modeling
from sklearn.model_selection import cross_val_predict, cross_val_score
from sklearn.ensemble import RandomForestClassifier

!pip install eli5

# from sklearn_crfsuite import CRF, scorers, metrics
# import sklearn_crfsuite
# from sklearn_crfsuite import scorers
# from sklearn_crfsuite import metrics
# from sklearn_crfsuite.metrics import flat_classification_report
from sklearn.metrics import classification_report, make_scorer
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
import scipy.stats
import eli5

"""**1.2 Load Data**"""

from google.colab import drive
drive.mount('/content/drive')

list_kalimat = []
nomor_kalimat = 1

# open file in read mode
with open('/content/drive/MyDrive/Semester 7/Proyek PBA/Dataset/SINGGALANG.tsv', encoding='UTF-8') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj, delimiter='\t', quotechar=None) #https://www.petanikode.com/python-csv/ 
# https://docs.python.org/id/3.9/library/csv.html
# Menginstruksikan reader untuk tidak melakukan pemrosesan khusus terhadap karakter kutipan
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        if len(row) == 0:
            nomor_kalimat += 1 
        else:
            tmp_row= row
            tmp_row.append(nomor_kalimat)
            list_kalimat.append(tmp_row)

dataset = pd.DataFrame(list_kalimat, columns=['token', 'entitas bernama', 'kalimat'])

dataset.head()

dataset.info()

"""## **2. Exploring / Visualisasi Data (Analisis Data)** ##

Membangun kelas sederhana untuk menggabungkan kata-kata ke dalam kalimat.
"""

print("Jumlah kalimat: ", len(dataset.groupby(['kalimat'])))
words = list(set(dataset["token"].values))
n_words = len(words)
print("Jumlah kata unik : ", n_words)
tags = list(set(dataset["entitas bernama"].values))
print("Entitas bernama:", tags)
n_tags = len(tags)
print("Jumlah entitas bernama: ", n_tags)

#Words tagged as Place
dataset.loc[dataset['entitas bernama'] == 'Place', 'token'].head()

#Words tagged as Person
dataset.loc[dataset['entitas bernama'] == 'Person', 'token'].head()

#Words tagged as Organisation
dataset.loc[dataset['entitas bernama'] == 'Organisation', 'token'].head()

#Words tagged as O
dataset.loc[dataset['entitas bernama'] == 'O', 'token'].head()

"""**Menghitung Jumlah Entitas Bernama**"""

dataframe = dataset.groupby("entitas bernama" )
dataframe["entitas bernama"].count()

"""**Menampilkan 20 token pertama yang paling banyak muncul**"""

dataset['token'].value_counts()[:20]

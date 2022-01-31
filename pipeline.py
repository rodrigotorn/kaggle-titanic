# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload 1

# %%
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from src.preprocess import Preprocess

from src.models.rf import RF
from src.models.knn import KNN
from src.models.svc import SVC
from src.models.adaboost import Adaboost
from src.models.mlp import MLP

import warnings
warnings.filterwarnings('ignore')

# %% tags=[]
raw_train_df: pd.DataFrame = pd.read_csv('data/train.csv', index_col=0)
raw_test_df: pd.DataFrame = pd.read_csv('data/test.csv', index_col=0)
y_train: pd.Series = raw_train_df['Survived']

x_train, x_test = Preprocess(scaler=StandardScaler()) \
  .apply(raw_train_df, raw_test_df)

# %%
predictions: pd.DataFrame = pd.DataFrame({
    'rf': RF().predict(x_train, y_train, x_test),
    'knn': KNN().predict(x_train, y_train, x_test),
    # 'svc': SVC().predict(x_train, y_train, x_test),
    'adaboost': Adaboost().predict(x_train, y_train, x_test),
    'mlp': MLP().predict(x_train, y_train, x_test),
})

# workaround for a SVC unknown error
predictions['svc'] = pd.read_csv(
    'grid_search/suport_vector_machine/svc_predictions.csv',
)

predictions['PassengerId'] = raw_test_df.index
predictions['Survived'] = predictions.mode(axis=1)
predictions = predictions[['PassengerId', 'Survived']]
predictions.to_csv('data/output.csv', index=False)

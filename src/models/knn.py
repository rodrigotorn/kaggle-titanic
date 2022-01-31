"""Concrete K-Nearest Neighbors model"""
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from src._model import BaseModel


class KNN(BaseModel):
  """Concrete K-Nearest Neighbors model"""
  def __init__(self) -> None:
    pass

  def predict(
    self,
    x_train: np.ndarray,
    y_train: pd.DataFrame,
    x_test: np.ndarray,
  ) -> pd.Series:
    model = KNeighborsClassifier(
      n_neighbors=15
    )
    model.fit(x_train, y_train)
    return model.predict(x_test)

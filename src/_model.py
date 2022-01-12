"""Abstract base class for ML models"""

from abc import ABC, abstractmethod

class BaseModel(ABC):
  pass

@abstractmethod
def train():
  pass

@abstractmethod
def predict():
  pass

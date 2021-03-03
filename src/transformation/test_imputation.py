import logging
import numpy as np 
import pandas as pd

from library import Imputation as iptt


BENIGN = np.array([4., 28., 1., 1., 3.])
MALIGNANT = np.array([5., 60., 2., 4., 3.])
BENIGN_COUNT = np.array([1., 1., 1., 1., 1.]) 
MALIGNANT_COUNT = np.array([4., 4., 4., 4., 2.])

PATH = ("data/mammographic/source.csv")
HEADER = ["BI-RADS","AGE","SHAPE","MARGIN","DENSITY","SEVERITY"]

try: 
    df = pd.read_csv(PATH, names = HEADER)
    df = df.head()
except:
    logging.warning("pandas did not find the dataset source")
finally:
    del PATH
    del HEADER
  
 
#  print(((iptt(df, labels).avg())[0]))) 
  
  
def test_benign_avg():
    assert np.array_equal(BENIGN, ((iptt(df,2).avg())[0]))


def test_malignant_avg():
    assert np.array_equal(MALIGNANT, ((iptt(df,2).avg())[1]))
    
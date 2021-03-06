#!/usr/bin/env python

import logging
import numpy as np 
import pandas as pd

from library import Imputation as iptt


SAMPLING = np.array([2, 4, 4, 4, 5, 5, 7, 9])

BENIGN = np.array([4., 28., 1., 1., 3.])
MALIGNANT = np.array([5., 60., 2., 4., 3.])
BENIGN_COUNT = np.array([1., 1., 1., 1., 1.]) 
MALIGNANT_COUNT = np.array([4., 4., 4., 4., 2.])

PATH = ("dataset/mammographic/source.csv")
HEADER = ["BI-RADS","AGE","SHAPE","MARGIN","DENSITY","SEVERITY"]

try: 
    df = (pd.read_csv(PATH, names = HEADER)).head()
except:
    logging.warning("pandas did not find the dataset source")
finally:
    del PATH
    del HEADER

  
def test_benign_avg():
    assert np.array_equal(BENIGN, ((iptt(df,2).avg())[0]))


def test_malignant_avg():
    assert np.array_equal(MALIGNANT, ((iptt(df,2).avg())[1]))

    
def test_standard_deviation():
    avg = 0
    std = 0
    size = len(SAMPLING)

    for i in range(size):    
        avg += SAMPLING[i] / size

    for i in range(size):
        std += (SAMPLING[i] - avg) ** 2 
    std = ((std / size) ** .5)
    
    assert  std == 2  
    
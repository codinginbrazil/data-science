#!/usr/bin/env python

import numpy as np
import pandas as pd

from library import Normalization as nm


AVG = 56.4
LARGE = 74
SMALL = 28
STANDARD_DEVIATION = 14.49291

ORIGINAL = {67, 43, 58, 28, 74, 65, 70, 42, 57, 60}
DECIMAL_SCALING = {.67, .43, .58, .28, .74, .65, .70, .42, .57, .60}

INTERQUARTILE_RANGE = {.4, -0.8, -0.05, -1.55, .75, .3, .55, -0.85, -0.1, .05}
MAX_MIN = {0.848, 0.326, 0.652, 0.000, 1.000, 0.804, 0.913, 0.304, 0.630, 0.696}
TRIVIAL = {0.905, 0.581, 0.784, 0.378, 1.000, 0.878, 0.946, 0.568, 0.770, 0.811}
Z_SCORE = {0.731, -.925, 0.110, -1.96, 1.214, 0.593, 0.938, -.994, 0.041, 0.248}


def test_init():
    calc = list(ORIGINAL)
    calc = set(calc)
    assert ORIGINAL == calc


def test_avg():
    assert (nm(ORIGINAL).avg) == AVG

def test_large():
    assert (nm(ORIGINAL).large) == LARGE
    
def test_small():
    assert (nm(ORIGINAL).small) == SMALL

def test_std():
    assert (nm(ORIGINAL).std) == STANDARD_DEVIATION 


def test_decimal_scaling():
    assert set(nm(ORIGINAL).decimal_scaling()) == DECIMAL_SCALING
    
    
# def test_interquartile_range():
#     assert set(nm(ORIGINAL).interquartile_range()) != INTERQUARTILE_RANGE

def test_max_min():
    assert set(nm(ORIGINAL).max_min(3)) == MAX_MIN


def test_trivial():
    assert set(nm(ORIGINAL).trivial(3)) == TRIVIAL


def test_z_score():
    assert set(nm(ORIGINAL).z_score(3)) == Z_SCORE
    

def test_mammographic_head_max_min():
    PATH = ("data/mammographic/imputation.csv")
    BI_RADS = {5, 4, 5, 4, 5}
    AGE = {67, 43, 58, 28, 74}
    SHAPE = {3, 1, 4, 1, 1}
    MARGIN = {5, 1, 5, 1, 5}
    DENSITY = {3, 3, 3, 3, 3}

    BI_RADS_MAX_MIN = {1, 0, 1, 0, 1}
    AGE_MAX_MIN = {0.848, 0.326, 0.652, 0.000, 1.000}
    SHAPE_MAX_MIN = {.667, 0, 1, 0, 0}
    MARGIN_MAX_MIN = {1, 0, 1, 0, 1}
    DENSITY_MAX_MIN = {0, 0, 0, 0, 0}

    try: 
        df = (pd.read_csv(PATH)).head()
    except:
        print("pandas did not find the dataset source")
    finally:
        del PATH    
    
    assert set(df.iloc[:, 0]) == BI_RADS
    assert set(df.iloc[:, 1]) == AGE
    assert set(df.iloc[:, 2]) == SHAPE
    assert set(df.iloc[:, 3]) == MARGIN
    assert set(df.iloc[:, 4]) == DENSITY
    
    assert set(nm(((df.iloc[:, 0]).astype(float))).max_min(3)) == BI_RADS_MAX_MIN
    assert set(nm(((df.iloc[:, 1]).astype(float))).max_min(3)) == AGE_MAX_MIN
    assert set(nm(((df.iloc[:, 2]).astype(float))).max_min(3)) == SHAPE_MAX_MIN
    assert set(nm(((df.iloc[:, 3]).astype(float))).max_min(3)) == MARGIN_MAX_MIN
    assert set(nm(((df.iloc[:, 4]).astype(float))).max_min(3)) == DENSITY_MAX_MIN


def test_mammographic_head_10_max_min():
    PATH = ("data/mammographic/imputation.csv")
    
    BI_RADS_10 = { 5,  4,  5,  4,  5,  4,  4,  5,  5, 5}
    AGE_10     = {67, 43, 58, 28, 74, 65, 70, 42, 57, 60}
    SHAPE_10   = { 3,  1,  4,  1,  1,  1,  2,  1,  1, 3}
    MARGIN_10  = { 5,  1,  5,  1,  5,  2,  2,  2,  5, 5}
    DENSITY_10 = { 3,  3,  3,  3,  3,  3,  3,  3,  3, 1}

    BI_RADS_MAX_MIN_10 = {1.00, 0.00, 1.00, 0.00, 1.00, 0.00, 0.00, 1.00, 1.00, 1.00}
    AGE_MAX_MIN_10     = {.848, .326, .652, 0.00, 1.00, .804, .913, .304, .630, .696}
    SHAPE_MAX_MIN_10   = {.667, 0.00, 1.00, 0.00, 0.00, 0.00, .333, 0.00, 0.00, .667}
    MARGIN_MAX_MIN_10  = {1.00, 0.00, 1.00, 0.00, 1.00, .250, .250, .250, 1.00, 1.00}
    DENSITY_MAX_MIN_10 = {1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.00}

    try: 
        df = (pd.read_csv(PATH)).head(10)
    except:
        print("pandas did not find the dataset source")
    finally:
        del PATH    
    
    assert set(df.iloc[:, 0]) == BI_RADS_10
    assert set(df.iloc[:, 1]) == AGE_10
    assert set(df.iloc[:, 2]) == SHAPE_10
    assert set(df.iloc[:, 3]) == MARGIN_10
    assert set(df.iloc[:, 4]) == DENSITY_10
    
    assert set(nm(((df.iloc[:, 0]).astype(float))).max_min(3)) == BI_RADS_MAX_MIN_10
    assert set(nm(((df.iloc[:, 1]).astype(float))).max_min(3)) == AGE_MAX_MIN_10
    assert set(nm(((df.iloc[:, 2]).astype(float))).max_min(3)) == SHAPE_MAX_MIN_10
    assert set(nm(((df.iloc[:, 3]).astype(float))).max_min(3)) == MARGIN_MAX_MIN_10
    assert set(nm(((df.iloc[:, 4]).astype(float))).max_min(3)) == DENSITY_MAX_MIN_10
    
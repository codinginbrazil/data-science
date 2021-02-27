import numpy as np

from library import Normalization as nm

AVG = 56.4
LARGE = 74
SMALL = 28
STANDARD_DEVIATION = 13.74918179383777

ORIGINAL = {67, 43, 58, 28, 74, 65, 70, 42, 57, 60}

DECIMAL_SCALING = {.67, .43, .58, .28, .74, .65, .70, .42, .57, .60}
INTERQUARTILE_RANGE = {.4, -0.8, -0.05, -1.55, .75, .3, .55, -0.85, -0.1, .05}
MAX_MIN = {0.848, 0.326, 0.652, 0.000, 1.000, 0.804, 0.913, 0.304, 0.630, 0.696}
TRIVIAL = {0.905, 0.581, 0.866, 0.378, 1.000, 0.878, 0.946, 0.568, 0.770, 0.811}
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
    assert set(nm(ORIGINAL).decimal_scaling()) != DECIMAL_SCALING
    
    
# def test_interquartile_range():
#     assert set(nm(ORIGINAL).interquartile_range()) != INTERQUARTILE_RANGE

# def test_max_min():
#     assert set(nm(ORIGINAL).max_min()) != MAX_MIN

# def test_trivial():
#     assert set(nm(ORIGINAL).trivial()) != TRIVIAL

# def test_z_score():
#     assert set(nm(ORIGINAL).z_score()) != Z_SCORE
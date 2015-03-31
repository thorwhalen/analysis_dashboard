__author__ = 'thor'

import numpy as np


class TestAnalyzer(object):
    def __init__(self, npts=100):
        self.npts = npts

    def get_rand_numbers(self, max_nb=10):
        return np.rand(self.npts) * max_nb

    # def plot_this(self, x):


class TestAnalyzerInterface(TestAnalyzer):
    def __init__(self):
        pass


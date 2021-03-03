import logging
import numpy as np 
import pandas as pd


class Imputation(object):
    
    def __init__(self, df: pd, labels: int):
        logging.basicConfig(filename=('log/imputation.txt'),
        level=logging.DEBUG, 
        format=' %(asctime)s - %(levelname)s - %(message)s')

        self.df = df
        del(df)
        self.rows_size = len(self.df)
        self.columns_size = len(self.df.columns) - 1
        self.label = [labels, self.columns_size]
        self.count = [labels, self.columns_size]

        logging.debug("Dataframe number of rows: - " + str(self.rows_size))
        logging.debug("Dataframe number of columns - " + str(self.columns_size))         
    
    
    def avg(self) -> np: 
        for i in range(self.rows_size):        
            if ((self.df.iloc[i, -1]) == 0):
                for j in range(self.columns_size): 
                    if (self.df.iloc[i, j] != '?'):
                        self.count[0][j] += 1
                        self.label[0][j] += (float(self.df.iloc[i, j]))        
            else:
                for j in range(self.columns_size):
                    if (self.df.iloc[i, j] != '?'):
                        self.count[1][j] += 1
                        self.label[1][j] += (float(self.df.iloc[i, j]))
        
        logging.debug("Imputation.avg")
        logging.debug("Benign sum - " + str(self.label[0]))
        logging.debug("Malignant sum - " + str(self.label[1]))
        logging.debug("Benign count - " + str(self.count[0]))
        logging.debug("Malignant count - " + str(self.count[1]))
                      
        self.label[0] = np.around(self.label[0] / self.count[0])
        self.label[1] = np.around(self.label[1] / self.count[1])

        logging.debug("Benign avg - " + str(self.label[0]))
        logging.debug("Malignant avg - " + str(self.label[1]))
        
        return self.label  
    

    @property
    def rows_size(self):
        return self._rows_size 
    
    @rows_size.setter
    def rows_size(self, rows_size):
        self._rows_size = rows_size
        
    @rows_size.deleter
    def rows_size(self):
        del self._rows_size
        
        
    @property
    def columns_size(self):
        return self._columns_size 
    
    @columns_size.setter
    def columns_size(self, columns_size):
        self._columns_size = columns_size
        
    @columns_size.deleter
    def columns_size(self):
        del self._columns_size
        
    
    @property
    def count(self):
        return self._count 
    
    @count.setter
    def count(self, count):
        self._count = np.zeros(count)
        
    @count.deleter
    def count(self):
        del self._count
        
        
    @property
    def label(self):
        return self._label 
    
    @label.setter
    def label(self, label):
        self._label = np.zeros(label)
        
    @label.deleter
    def label(self):
        del self._label
          
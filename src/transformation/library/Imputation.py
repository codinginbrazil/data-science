import logging
import numpy as np 
import pandas as pd


class Imputation(object):
    
    def __init__(self, df: pd, labels: int):
        logging.basicConfig(filename=('log/imputation.txt'),
        level=logging.DEBUG, 
        format=' %(asctime)s - %(levelname)s - %(message)s')
        logging.disable()

        self.df = df
        self.dimension = labels
        del(df)
        del(labels)
        
        self.rows_size = len(self.df)
        self.columns_size = len(self.df.columns) - 1
        self.label_sum = [self.dimension, self.columns_size]
        self.count = [self.dimension, self.columns_size]

        self._central_trend()
    
        logging.debug("Dataframe number of rows: - " + str(self.rows_size))
        logging.debug("Dataframe number of columns - " + str(self.columns_size))
        logging.debug("Imputation.avg")
        logging.debug("Benign sum - " + str(self.label_sum[0]))
        logging.debug("Malignant sum - " + str(self.label_sum[1]))
        logging.debug("Benign count - " + str(self.count[0]))
        logging.debug("Malignant count - " + str(self.count[1]))         
    
    
    def _central_trend(self): 
        NULL = '?'
        for i in range(self.rows_size):        
            if ((self.df.iloc[i, -1]) == 0):
                for j in range(self.columns_size): 
                    if (self.df.iloc[i, j] != NULL):
                        self.count[0][j] += 1
                        self.label_sum[0][j] += (float(self.df.iloc[i, j]))        
            else:
                for j in range(self.columns_size):
                    if (self.df.iloc[i, j] != NULL):
                        self.count[1][j] += 1
                        self.label_sum[1][j] += (float(self.df.iloc[i, j]))
    
    
    def avg(self) -> np:
        avg = self.label_sum
        avg[0] = np.around(avg[0] / self.count[0])
        avg[1] = np.around(avg[1] / self.count[1])

        logging.debug("Benign avg - " + str(avg[0]))
        logging.debug("Malignant avg - " + str(avg[1]))
        
        return avg
    
    
    # def mode(self) -> np:
    #     pass
    
    
    # def median(self) -> np:
    #     pass
    
    
    # def standard_deviation(self) -> np:
    #     pass
    
    
    def replace(self, find, replace) -> pd:
        NULL = find
        df = self.df
        for i in range(self.rows_size):        
            if ((df.iloc[i, -1]) == 0):
                for j in range(self.columns_size): 
                    if (self.df.iloc[i, j] == NULL):
                        (df.iloc[i, j]) = replace[0][j]         
            else:
                for j in range(self.columns_size):
                    if (df.iloc[i, j] == NULL):
                        (df.iloc[i, j]) = replace[1][j]
        return df
    

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
    def label_sum(self):
        return self._label_sum 
    
    @label_sum.setter
    def label_sum(self, label_sum):
        self._label_sum = np.zeros(label_sum)
        
    @label_sum.deleter
    def label_sum(self):
        del self._label_sum
          
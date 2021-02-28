import numpy as np 


class Normalization(object):
    def __init__(self, value):
        value = list(value)
        self.avg = value
        self.large = value
        self.small = value
        self.std = value
        self.value = value
            
    
    def decimal_scaling(self):
        arr = self.value 
        for i in range(arr.size):
            arr[i] /= 100.0
        return arr
        
    
    def interquartile_range(self):
        return self.value
    
    
    def max_min(self):
        return self.value
    
    
    def trivial(self, decimals):
        arr = self.value 
        for i in range(arr.size):
            arr[i] /= self.large
        return np.around(arr, decimals=decimals)
    
    
    def z_score(self):
        return self.value
    

    @property
    def avg(self):
        return self._avg 
    
    @avg.setter
    def avg(self, avg):
        self._avg = np.mean(avg)
        
    @avg.deleter
    def avg(self):
        del self._avg
        
        
    @property
    def large(self):
        return self._large 
    
    @large.setter
    def large(self, large):
        self._large = np.max(large)
        
    @large.deleter
    def large(self):
        del self._large
    
    
    @property
    def small(self):
        return self._small 
    
    @small.setter
    def small(self, small):
        self._small = np.min(small)
        
    @small.deleter
    def small(self):
        del self._small
        
    
    @property
    def std(self):
        return self._std 
    
    @std.setter
    def std(self, std):
        self._std = np.std(std)
        
    @std.deleter
    def std(self):
        del self._std
    
        
    @property
    def value(self):
        return self._value 
    
    @value.setter
    def value(self, value):
        self._value = np.array(value).astype(float)
        
    @value.deleter
    def value(self):
        del self._value
    
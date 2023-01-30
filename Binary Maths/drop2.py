
from FoxDot import GeneratorPattern, Pattern, asStream, PatternInput
#from FoxDot import *

#import FoxDot # GeneratorPattern, Pattern, asStream, PatternInput


class PDrop(GeneratorPattern):
    def __init__(self,buildup=2, target=1, bar_length=4):
        super().__init__()
        self.buildup = buildup
        self.target = target
        self.bar_length = bar_length
        self._prev = bar_length
        


    def func(self, index):
        if(self.target == self._prev):
            return self.target
        
        beat = index % self.bar_length
        if beat:
            return self._prev
        self._prev = int(index / self.bar_length)
        
        print(index, self._prev, int(index / self.bar_length))
        
        return self._prev

t1 = PDrop(buildup=2, target=1, bar_length=4)[:10]
print(t1[:10])
assert  t1 == Pattern([4,2,2,1,1,1,1,1,1])

'''

class PDrop(GeneratorPattern):
    """ Implementation of the PZ12 algorithm for predetermined random numbers. Using
        an irrational value for p, however, results in a non-determined order of values. 
        Experimental, only works with 2 values.
    """
    def __init__(self, tokens=[1,0], p=[1, 0.5]):
        GeneratorPattern.__init__(self)
        self.data    = tokens
        self.probs = [value / max(p) for value in p]
        self._prev   = []
        self.dearth  = [0 for n in self.data]

    def _count_values(self, token):    
        return sum([self._prev[i] == token for i in range(len(self._prev))])

    def func(self, index):
        index = len(self._prev)
        for i, token in enumerate(self.data):
            d0 = self.probs[i] * (index + 1)
            d1 = self._count_values(token)
            self.dearth[i] = d0-d1
        i = self.dearth.index(max(self.dearth))
        value = self.data[i]
        self._prev.append(value)
        return value

assert PDrop() == [4,2,2,1,1,1,1]
'''
print(PDrop())
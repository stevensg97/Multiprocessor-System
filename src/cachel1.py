import pandas as pd
import time

class CacheL1:
    def __init__(self):
        self.memory = {'Block': [], 'State': [], 'Address': [], 'Data': []}
        self.initMemory()
    
    def initMemory(self):
        for i in range(2):
            self.memory['Block'].append(i)
            self.memory['State'].append('I')
            self.memory['Address'].append(None)
            self.memory['Data'].append('0000')

    def setBlock(self, block, state, address,  data):
        ind = self.memory['Block'].index(block)
        self.memory['State'][ind] = state
        self.memory['Address'][ind] = address
        self.memory['Data'][ind] = data
        time.sleep(1)
        return self.getMemory()
    
    def getMemory(self):
        return print(pd.DataFrame(self.memory))

a = CacheL1()
a.getMemory()
#a.setBlock('1111', 'DM', '1', 'FFFF')
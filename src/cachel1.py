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

    def getMemory(self):
        return self.memory

    def setBlock(self, block, state, address,  data):
        ind = self.memory['Block'].index(block)
        self.memory['State'][ind] = state
        self.memory['Address'][ind] = address
        self.memory['Data'][ind] = data
        time.sleep(1)
        return self.printMemory()
    
    def printMemory(self):
        print(pd.DataFrame(self.memory))

a = CacheL1()
a.printMemory()
a.setBlock(1, 'DM', '1001', 'AC8F')
a.setBlock(0, 'DM', '1100', 'FA4B')
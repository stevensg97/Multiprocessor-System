import pandas as pd
import time

class CacheL2:
    def __init__(self):
        self.memory = {'Block': [], 'State': [], 'Owner': [], 'Address': [], 'Data': []}
        self.initMemory()
    
    def initMemory(self):
        for i in range(4):
            self.memory['Block'].append(i)
            self.memory['State'].append('DI')
            self.memory['Owner'].append(None)
            self.memory['Address'].append(None)
            self.memory['Data'].append('0000')

    def setBlock(self, block, state, owner, address,  data):
        ind = self.memory['Block'].index(block)
        self.memory['State'][ind] = state
        self.memory['Owner'][ind] = owner
        self.memory['Address'][ind] = address
        self.memory['Data'][ind] = data
        time.sleep(3)
        return self.printMemory()
    
    def getMemory(self):
        return self.memory

    def printMemory(self):
        print(pd.DataFrame(self.memory))

a = CacheL2()
a.printMemory()
a.setBlock(2, 'DM', '1', '1101', 'FFFF')
a.setBlock(0, 'DM', '0', '1001', '45EC')
a.setBlock(2, 'DS', '1', '1101', 'FFFF')
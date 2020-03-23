
import pandas as pd
import time

class Memory:
    def __init__(self):
        self.memory = {'Address': [], 'State': [], 'Chip': [], 'Data': []}
        self.memoryAddresses = ['0000', '0001', '0010', '0011', '0100', '0101', '0110',
             '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
        self.initMemory()
    
    def initMemory(self):
        for i in range(16):
            self.memory['Address'].append(self.memoryAddresses[i])
            self.memory['State'].append('DI')
            self.memory['Chip'].append(None)
            self.memory['Data'].append('0000')

    def setBlock(self, address, state, chip, data):
        ind = self.memory['Address'].index(address)
        self.memory['State'][ind] = state
        self.memory['Chip'][ind] = chip
        self.memory['Data'][ind] = data
        time.sleep(5)
        return self.getMemory()
    
    def getMemory(self):
        return print(pd.DataFrame(self.memory))

a = Memory()
a.setBlock('0011', 'DM', '0', 'A3B4')
a.setBlock('1111', 'DM', '1', 'FFFF')
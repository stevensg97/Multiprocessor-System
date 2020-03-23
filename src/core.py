import random
import time
import threading

class Core:
    def __init__(self, nChip, nCore):
        self.nChip = nChip
        self.nCore= nCore
    
    def getNChip(self):
        return self.nChip

    def getNCore(self):
        return self.nCore

    def setNChip(self, nChip):
        self.nChip = nChip
    
    def setNCore(self, nCore):
        self.nCore = nCore

    def genInstruction(self):
        instructionTypes = ["CALC", ["WRITE", "READ"]] #processing instructions and memory access instructions
        instruction = random.choice(instructionTypes)
        archivo = open("log.txt", "a")
        if instruction == "CALC":
            print(self.getNCore() + ',', str(self.getNChip()) + ':', instruction)
            time.sleep(1.5)
            print("Finished")
            archivo.write(self.getNCore() + ', ' + str(self.getNChip()) + ': ' + instruction + '\n')
        else:
            instruction = random.choice(instruction)
            memoryAddresses = ['0000', '0001', '0010', '0011', '0100', '0101', '0110',
             '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
            memoryAddress = random.choice(memoryAddresses)
            if instruction == "READ":
                print(self.getNCore() + ',', str(self.getNChip()) + ':', instruction, memoryAddress)
                time.sleep(3)
                print("Finished")
                archivo.write(self.getNCore() + ', ' + str(self.getNChip()) + ': ' +
                 instruction + ' ' + memoryAddress + '\n')
            else:
                lst = [random.choice("0123456789ABCDEF") for n in range(4)]
                data = "".join(lst)
                print(self.getNCore() + ',', str(self.getNChip()) + ':', instruction, memoryAddress + ';' + data)
                time.sleep(4.5)
                print("Finished")
                archivo.write(self.getNCore() + ', ' + str(self.getNChip()) + 
                ': ' + instruction + ' ' + memoryAddress+ ';' + data + '\n')
        archivo.close()

    def exec(self):
        while True:
            time.sleep(1)
            self.genInstruction()



a = Core(0, 'P0')
b = Core(0, 'P1')
p0 = threading.Thread(target=a.exec)
p1 = threading.Thread(target=b.exec)
p0.start()
p1.start()

 

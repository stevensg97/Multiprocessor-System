import random
import time
import threading
import cachel1

class Core:
    def __init__(self, nChip, nCore):
        self.nChip = nChip
        self.nCore = nCore
        self.l1 = cachel1.CacheL1()
    
    def getNChip(self):
        return self.nChip

    def getNCore(self):
        return self.nCore

    def getL1(self):
        return self.l1

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
                #self.getL1().printMemory()
                if memoryAddress in self.getL1().getMemory()["Address"]:
                    print(self.getNCore() + ',', str(self.getNChip()) + ':', instruction, memoryAddress)
                    time.sleep(3)
                    print("Finished")
                    archivo.write(self.getNCore() + ', ' + str(self.getNChip()) + ': ' +
                    instruction + ' ' + memoryAddress + '\n')
                else:
                    print(self.getNCore() + ',', str(self.getNChip()) + ':', "Read Miss Cache L1")
                    time.sleep(3)
                    archivo.write(self.getNCore() + ', ' + str(self.getNChip()) + ': ' + "Read Miss Cache L1" + '\n')
                    #Ir al siguiente nivel de caché
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

 

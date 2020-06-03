

class Bus:
    def __init__(self):
        self.bus = None

    def l1ReadMiss(self, chip, core, address, state):
        result = {'Block': '', 'State': '', 'Address': '', 'Data': ''}

        result['State'] = "S"
        result['Address'] = address
        result['Data'] = address       
    
    def l1WriteMiss(self):
        """ if state=="I":
            
        elif state=="S":
            result['State'] = "S"
        else:
            result['State'] = "S" """

    def l1ReadHit(self):
        return None

    def l1WriteHit(self):
        return None

    def l2ReadMiss(self):
        return None

    def l2WriteMiss(self):
        return None

    def l2ReadHit(self):
        return None

    def l2WriteHit(self):
        return None
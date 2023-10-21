class Register:
    """takes a value and number of bits, can then print a nice table"""
    def __init__(self,n,n_bits):
        if n < 0:
            self.sign = "-"
            value = -(n-1)
        else:
            self.sign = '+'
            value = n

        self.value =[0]*n_bits

        for i in range(n_bits):
            self.value[i] |= value&1
            value = value >> 1

        self.n_bits = n_bits
        self.print()

    def print(self):
        print("Bit Place:\t",end='')
        for i in range(0,self.n_bits,1):
            print(f"{i:<5d}",end='')
        print()
        print(f"{'Value:':<9s}\t",end='')
        for i in self.value:
            print(f"{i:<5d}",end='')
        print()
        print(f"{'Sign:':<9s}\t{self.sign}",end='')
        print()
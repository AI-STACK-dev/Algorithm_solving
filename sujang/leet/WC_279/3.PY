class Bitset(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.bitset = 0
        self.cnt= 0
        

    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.bitset & (1 << idx) == 0:
            self.bitset |= (1 << idx)
            self.cnt+= 1
        

    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.bitset & (1 << idx) > 0:
            self.bitset ^= (1 << idx)
            self.cnt-= 1
        

    def flip(self):
        """
        :rtype: None
        """
        self.bitset ^= (1 << self.size)-1
        self.cnt = self.size - self.cnt

    def all(self):
        """
        :rtype: bool
        """
        return self.cnt == self.size
        

    def one(self):
        """
        :rtype: bool
        """
        return self.bitset > 0

    def count(self):
        """
        :rtype: int
        """
        return self.cnt        

    def toString(self):
        """
        :rtype: str
        """
        string = bin(self.bitset)[2:]
        return string[::-1] +'0'*(self.size - len(string))
        


# Your Bitset object will be instantiated and called as such:
size = 2
obj = Bitset(size)
print(obj.toString())
obj.flip()
print(obj.toString())
obj.unfix(1)
print(obj.toString())
print(obj.all())


# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.cnt)
# param_7 = obj.toString()
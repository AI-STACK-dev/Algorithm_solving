class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        # zero
        if num == 0:
            return 0
        # pos
        elif num > 0:
            numList = list(map(int,list(str(num))))
            numList.sort()
            zc = 0
            for i in range(len(numList)):
                if numList[i] == 0:
                    zc += 1
                else:
                    for j in range(zc):
                        numList.insert(i+1,0)
                    break
            charList = list(map(str,numList))
            return int(''.join(charList))
        else:
            numList = list(map(int,list(str(-num))))
            numList.sort(reverse=True)
            charList = list(map(str,numList))
            return -int(''.join(charList))            
            
            


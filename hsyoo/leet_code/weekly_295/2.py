class Solution:
    def discountPrices(self, sentence, discount):
        sentence = sentence.replace('10', '#')
        s = ''
        num = ''
        for idx, case in enumerate(sentence):
            if idx > 0 and (case.isdigit() or case == '#') and sentence[idx-1] == '$':
                if case == '#':
                    temp = 10
                    dis = 10 * discount / 100
                    temp -= dis
                    temp = "%.2f" %(temp)
                    num = str(10)
                else:
                    temp = int(case)
                    dis = temp * discount / 100
                    temp -= dis
                    temp = "%.2f" %(temp)
                    num = str(temp)
            elif idx == 0 and case.isdigit():
                s += case
            elif len(num) > 0 and case == ' ':
                s += temp
                num = ''
                s += case
            elif len(num) > 0 and case != ' ':
                s += num
                num = ''
                s += case
            else:
                s += case
        return s

#elif에 $이면서 len(num) > 0인 경우 처리 봐야함
print(Solution().discountPrices("there are $1 $2 and 5$ candies in the shop", 50))
print(Solution().discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100))
print(Solution().discountPrices("ka3caz4837h6ada4 r1 $602", 9))
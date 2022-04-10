class Solution:
    def minimizeResult(self, expression: str) -> str:
        front, end = [], []
        a,b = expression.split("+")

        for i in range(len(a)):
            if i == 0:
                front.append( (1,int(a), "".join(["(",a])) )
            else:
                front.append((int(a[:i]), int(a[i:]), "".join([a[:i],"(",a[i:]])))

        for i in range(len(b)):
            if i == len(b)-1:
                end.append( (int(b),1,"".join([b,")"])) )
            else:
                end.append( (int(b[:i+1]), int(b[i+1:]),"".join([b[:i+1],")",b[i+1:]])) )
        
        ans = int(1e9)
        temp = ""
        for fA,fB,f in front:
            for eA,eB,e in end:
                v = fA * (fB+eA) * eB
                if v < ans:
                    ans = v
                    temp = f+"+"+e
        
        return temp

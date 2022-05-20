import re
from collections import defaultdict

def solution(word, pages):
    pageRepo = defaultdict(list)
    pageBasicScoreRepo = defaultdict(int)
    pageScoreRepo = defaultdict(int)
    pageIdxRepo = defaultdict(int)
    for i,p in enumerate(pages):
        key = re.search('<meta property="og:url" content="(.*)"/>', p, re.I|re.S).group(1)
        values = re.findall('<a href="(https://[\S]*)"', p, re.I|re.S)
        # find link pagse
        for v in values:
            pageRepo[v].append(key)
        pageIdxRepo[key] = i
    
        key = re.search('<meta property="og:url" content="(.*)"/>', p, re.I|re.S).group(1)
        body = re.search('<body>(.*)</body>', p, re.I|re.S).group(1)
        processed_body = re.sub('<a href="(.*)</a>', '', body)
        # count score
        basic_score = 0
        result = re.findall(r'[a-zA-Z]+',processed_body, re.I|re.S)
        for r in result:
            if r.lower() == word.lower():
                basic_score += 1
        a = len(values)
        pageBasicScoreRepo[key] = basic_score
        pageScoreRepo[key] += basic_score/a 
        
    ans = [0,int(1e9)]
    for k in pageIdxRepo.keys():
        temp = pageBasicScoreRepo[k]
        for r in pageRepo[k]:
            if r in pageScoreRepo:
                temp += pageScoreRepo[r]
        if ans[0] < temp :
            ans[0] = temp
            ans[1] = pageIdxRepo[k]
        elif ans[0] == temp and ans[1] > pageIdxRepo[k]:
            ans[0] = temp
            ans[1] = pageIdxRepo[k]            
    
    return ans[1]
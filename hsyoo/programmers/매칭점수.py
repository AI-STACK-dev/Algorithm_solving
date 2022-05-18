# from collections import defaultdict

# def solution(word, pages):
#     word = word.lower()
#     base_score = defaultdict(int)
#     out_link = defaultdict(int)
#     h_link = defaultdict(list)

#     for page in pages:
#         temp = page.split('content="')
#         web_key = temp[-1].split('"')[0].lower()
#         content = temp[-1].split('<body>')
#         a_string = content[-1].split('</body>')[0].split('<a ')
#         n_string = []
#         for a in a_string:
#             n_string.extend(a.split('\n'))
#         # print(n_string)
#         cnt = 0
#         word_split = []
#         for s in n_string:
#             s=s.lower()
#             if 'href' in s:
#                 temp2 = s.split('"')[1]
#                 if 'https' in temp2:
#                     hyper_link = temp2
#                     h_link[hyper_link].append(web_key)
#                     out_link[web_key] += 1
#             else:
#                 tmp = ''
#                 for case in s:
#                     if case.isalpha():
#                         tmp += case
#                     else:
#                         word_split.append(tmp)
#                         tmp = ''
#                 word_split.append(tmp)
#         # print(word_split)
#         cnt += word_split.count(word)
#         base_score[web_key] += cnt
#     print(base_score)
#     print(out_link)
#     print(h_link)
#     answers = []
#     for web_key in base_score.keys():
#         score = base_score[web_key]
#         for hyper_link in h_link[web_key]:
#             score += base_score[hyper_link] / out_link[hyper_link]
#         answers.append(score)
#     print(answers)
#     return answers.index(max(answers))

import re
from collections import defaultdict

def solution(word, pages):
    webpage = []
    webpageName = []
    webpageGraph = defaultdict(list)

    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        basicScore = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                basicScore += 1
        exiosLink = re.findall('<a href="(https://[\S]*)"', page)
        print(exiosLink)
        print(exiosLink)


        for link in exiosLink:
            webpageGraph[link].append(url)
        webpageName.append(url)
        webpage.append([url, basicScore, len(exiosLink)])
    
    maxValue = 0
    result = 0
    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]
        if url in webpageGraph.keys():
            for link in webpageGraph[url]:
                a,b,c = webpage[webpageName.index(link)]
                score += (b/c)
        if maxValue < score:
            maxValue = score
            result = i
    return result

# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
# print(solution('blind', pages))
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution('Muzi', pages))
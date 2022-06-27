def solution(words,queries):
    head, head_rev = {}, {}
    word_count = []

    def add(head,word):
        len_word = len(word)
        node = head
        for w in word:
            if w not in node:
                node[w]={}
            node = node[w]
            if 'len' not in node:
                node['len'] = [len_word]
            else:
                node['len'].append(len_word)
        node['end'] = True
    

    for word in words:
        add(head,word)
        add(head_rev,word[::-1])
        word_count.append(len(word))


    def search(head, querie):
        len_qu = len(querie)
        node = head
        for q in querie:
            if q == '?':
                return node['len'].count(len_qu)
            elif q not in node:
                break
            node = node[q]
        return 0 

    ans = []
    for querie in queries:
        len_qu = len(querie)
        if querie[0] == '?':
            if querie[-1] == '?':
                ans.append(word_count.count(len_qu))
            else:
                ans.append(search(head_rev, querie[::-1]))
        else:
            ans.append(search(head, querie))
    return ans
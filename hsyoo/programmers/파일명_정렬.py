def solution(files):
    file_list = []
    for file in files:
        head_flag = True
        number_flag = False
        temp = ''
        num_len = 0
        for idx, case in enumerate(file):
            if head_flag == True and case.isdigit() == False:
                temp += case
            elif head_flag == True and case.isdigit():
                head = temp
                temp = case
                num_len += 1
                head_flag = False
            elif head_flag == False and (case.isdigit() and num_len <= 5):
                temp += case
                num_len += 1
            else:
                number = temp
                tail = file[idx:]
                number_flag = True
                break
        if number_flag == False:
            number = temp
            tail = ''
        file_list.append((head, number, tail, file))
    file_list.sort(key = lambda x : (x[0].lower(), int(x[1])))
    answer = [i[3] for i in file_list]
    return answer

# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# print(solution(['muzi1.txt', 'MUZI1.txt', 'muzi001.txt', 'muzi1.TXT']))
print(solution(['F-15']))
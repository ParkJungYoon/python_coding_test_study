# 비속어 단어와 완벽 일치 => #로
# . 하나는 1 이상 k 이하 알파벳으로 대체 가능
import re

def solution(k, dic, chat):
    result = []
    chat_word = chat.split()
    for i in chat_word:
        filtered = filtered_word(k, dic, i)
        result.append(filtered)
    return ' '.join(result)

def filtered_word(k, dic, word):
    if word in dic:
        return '#' * len(word)
    if '.' in word:
        # ..으로만 이루어진 단어
        if word.count('.') == len(word):
            print(1)
            for i in dic:
                if len(word) * k >= len(i): 

                    return '#' * len(i)
                return word

        # .이 알파벳 사이에 있을 땐 어떻게 해야할까아아~~~
    
    return word

# def solution2(k, dic, chat):
#     # replace [a-z]{1,k} -> match
#     chat_replace = re.sub('.',,chat)
#     return chat_replace

# ----------------------------------------------
dic1 = ["slang", "badword"]
chat1 = "badword ab.cd bad.ord .word sl.. bad.word"
print(solution(2, dic1, chat1))
# print(solution2(2, dic1, chat1))
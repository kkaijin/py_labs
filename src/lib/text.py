
def normalize(text: str) -> str:
    sym = ['\\n','\\r','\\t','\\b','\\f','\\v','\n','\r','\t','\\','\'','\"','\b','\f','\v']
    s = ''
    for i in sym:
        text = text.split(i)
        text = [i for i in text]
        s = ''
        for i in text:
            s += i+' '
        text = s

    text = text.replace('ё','е').replace('Ё','Е')
    text = text.casefold()

    s = ''
    text = text.split()
    for i in range(len(text)):
        if i != len(text)-1:
            s += text[i]+' '
        else:
            s += text[i]
    return s

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка",True,True))
# print(normalize("Hello\r\nWorld",True,True))
# print(normalize("  двойные   пробелы  ",True,True))



def tokenize(text: str) -> list[str]:
    for j in range(len(text)):
        if not((text[j] >= 'a' and text[j] <= 'z') or text[j] == '-' or text[j] == '+' or text[j] == '_' or (text[j] >= 'а' and text[j] <= 'я') or text[j] == ' ' or (text[j] >= '0' and text[j] <= '9')):
            text = text.replace(text[j], ' ')
    return text.split()

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    if len(tokens) == 0:
        return
    set_tokens = set(tokens)
    arr_tokens = []
    dict_tokens = {}
    for i in set_tokens:
        arr_tokens.append([i,tokens.count(i)])
    arr_tokens = sorted(arr_tokens, key=lambda item: item[1], reverse = True)
    c=0
    for i in arr_tokens:
        dict_tokens[i[0]] = i[1]
        c+=1
    return dict_tokens

# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if len(freq) == 0:
        return 
    list_freq = []
    if all(len(k)==len(list(freq.keys())[0]) for k,v in freq.items()):
        freq = sorted(freq.items(), key=lambda item: item[0], reverse = False)
    else:
        freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)
    c=0
    for k,v in freq:
        if c < n:
            list_freq.append(tuple([k,v]))
        else:
            break
        c += 1
    return list_freq
    

# print(top_n({"a":3,"b":2,"c":1}, 2))
# print(top_n({"aa":2,"bb":2,"cc":1}, 2))
print(count_freq(""))
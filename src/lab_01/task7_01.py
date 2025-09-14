import string
alp = string.ascii_uppercase
numb = '0123456789'
s = input('in: ')
s_o = ''
flag = 0
dist = 0
s_i = -1
for i in range(len(s)):
    if flag == 0 and s[i] in alp:
        s_o += s[i]
        flag = 1
        dist = i
    if flag == 2:
        s_o += s[i]
        dist = i - dist
        s_i = i + dist
        flag = 3
    if flag == 1 and s[i] in numb:
        flag = 2
    if i == s_i:
        s_o += s[i]
        s_i += dist
print('out:',s_o)    

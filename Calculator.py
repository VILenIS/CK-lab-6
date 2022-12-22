#print("!hello\nPlese write ")



def cal(s):
    if len(s)%2==0:
        return "ERROR"
    k = int(s[0])
    for i in range(len(s)-1):
        if i % 2 != 0:
            if s[i] == '-':
                k = k-int(s[i+1])
            elif s[i] == '+':
                k = k+int(s[i+1])
            elif s[i] == '*':
                k = k*int(s[i+1])
            elif s[i] == '/':
                k = k/int(s[i+1])
    return k

print(cal(s))



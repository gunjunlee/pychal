a = ['1']

for i in range(0, 31):
    string = a[i]
    nextstring = ""
    chk = string[0]
    cnt = 0
    for j in range(len(string)):
        if chk == string[j] and j < len(string):
            cnt = cnt + 1
        else:
            nextstring = nextstring + str(cnt)
            nextstring = nextstring + chk
            chk = string[j]
            cnt = 1
    nextstring = nextstring + str(cnt)
    nextstring = nextstring + chk
    a.append(nextstring)

print(len(a[30]))

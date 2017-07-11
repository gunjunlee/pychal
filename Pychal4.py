import urllib.request
number = 3022
while 1:
    fp = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"%number)
    text = fp.read().decode()
    print(text)
    number = ""
    for i in text:
        if i.isdigit():
            number = number + i
    number = int(number)

import zipfile

path = '90052.txt'

fp = zipfile.ZipFile("channel.zip")
result = ""

while True:
    text = fp.read(path).decode()
    result = result + fp.getinfo(path).comment.decode()
    path = ""
    for i in text:
        if i.isdigit() == True:
            path = path + i
    path = path + '.txt'
    if path == '.txt':
        break

print(result)

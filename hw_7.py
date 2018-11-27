with open('file/file.txt', 'r') as f:
    countLine = 0
    for x in f.readlines():
        countLine += 1
    print('Rows {countLine}'.format(countLine = countLine))


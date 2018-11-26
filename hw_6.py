with open('file/file.txt', 'r') as f:
    file_read = f.read()
    max_word = max(file_read.split(), key=len)
    print(max_word)
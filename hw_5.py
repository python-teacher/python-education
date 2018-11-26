x = int(input('Введіть скільки останніх рядків відобразити?: '))
with open('file/file.txt' , 'r') as f:
    lines = f.readlines()[-x:]
    for line in lines:
        print(line)

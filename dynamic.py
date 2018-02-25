def load(str):
    word =0
    lines =0
    char =0
    with open(str) as h:
        for line in h:
            lines = lines+1
            line = line.split()
            word = word + len(line)
            for item in line:
                char = char + len(item)
    print(str)
    print('line ',lines)
    print('word ',word)
    print('char ',char)
            
x = int(input('enter a number\n'))
load('first.txt')
if(x%2 ==0):
    load('even.txt')
else:
    load('odd.txt')
    

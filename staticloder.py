def load(str):
    word = 0
    lines = 0
    char = 0
    with open(str)as f:
        for line in f:
            lines = lines + 1
            line = line.split()
            word = word + len(line)
            for item in line:
                char = char + len(item)
    print(str)
    print('char ',char)
    print('word ',word)
    print('lines ',lines)

with open('input.txt') as f:
    for line in f:
        line = line.split()
        for item in line:
            if item.startswith('load'):
                item = item[6:]
                item = item[:-3]
                load(item)
        

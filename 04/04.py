def partone(input):
    sum = 0
    with open(input, 'r') as fp:
        for line in fp.read().split('\n'):
            winning = [x for x in line.split(' | ')[0].split()]
            numbers = [x for x in line.split(' | ')[1].split()]
            matches = [x for x in numbers if x in winning]
            if matches:
                sum += pow(2, len(matches)-1)
    print(sum)
        
def parttwo(input):
    sum = 0
    cards = {}
    with open(input, 'r') as fp:
        lines = fp.read().split('\n')
        for i, line in enumerate(lines):
            if i not in cards:
                cards[i] = 1
            else:
                cards[i] += 1
            winning = [x for x in line.split(' | ')[0].split()]
            numbers = [x for x in line.split(' | ')[1].split()]
            matches = [x for x in numbers if x in winning]
            if matches:
                for j in range(len(matches)):
                    if i+j+1 not in cards and i+j+1 < len(lines):
                        cards[i+j+1] = cards[i]
                    elif i+j+1 in cards and i+j+1 < len(lines):
                        cards[i+j+1] += cards[i]
                    
    for key in cards:
        sum += cards[key]
    print(sum)

partone('input')
parttwo('input')
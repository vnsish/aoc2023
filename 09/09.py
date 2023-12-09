def extrapolate(sequence, dir):
    new_sequence = []
    for i in range(len(sequence)-1, 0, -1):
        new_sequence.insert(0,sequence[i]-sequence[i-1])
    if(len(set(new_sequence))) == 1:
        return new_sequence[0]
    if  dir == 'f':
        return new_sequence[-1]+extrapolate(new_sequence, 'f')
    elif  dir == 'b':
        return new_sequence[0]-extrapolate(new_sequence, 'b')

def partone(input):
    with open(input, 'r') as fp:
        lines = fp.read().split('\n')

    sequences = []
    
    for line in lines:
        sequences.append([int(x) for x in line.split()])

    sum = 0
    for sequence in sequences:
        next_val = extrapolate(sequence, 'f')
        sum += sequence[-1]+next_val
    print(sum)

def parttwo(input):
    with open(input, 'r') as fp:
        lines = fp.read().split('\n')

    sequences = []
    
    for line in lines:
        sequences.append([int(x) for x in line.split()])

    sum = 0
    for sequence in sequences:
        next_val = extrapolate(sequence, 'b')
        sum += sequence[0]-next_val
    print(sum)

partone('input')
parttwo('input')
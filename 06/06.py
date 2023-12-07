import math

def partone(input):
    with open(input, 'r') as fp:
        lines = fp.read().split('\n')

    times = [int(x) for x in lines[0].split()]
    records = [int(x) for x in lines[1].split()]

    result = 1
    for i in range(len(times)):
        possiblewins = 0
        for j in range(1, times[i]):
            distance = j*(times[i]-j)
            if distance > records[i]:
                possiblewins += 1

        result *= possiblewins
    print(result)

def parttwo(input):
    with open(input, 'r') as fp:
        lines = fp.read().split('\n')

    times = int(lines[0].replace(' ', ''))
    records = int(lines[1].replace(' ', ''))

    result = 1
    possiblewins = 0 

    for j in range(1, times):
        distance = j*(times-j)
        if distance > records:
            possiblewins += 1

    result *= possiblewins
    print(result)

def parttwo_minmax(input):
    with open(input, 'r') as fp:
        lines = fp.read().split('\n')

    times = int(lines[0].replace(' ', ''))
    records = int(lines[1].replace(' ', ''))

    result = 1
    possiblewins = 0 

    for j in range(1, times):
        distance = j*(times-j)
        if distance > records:
            max_val = j

    for j in range(times, 1, -1):
        distance = j*(times-j)
        if distance > records:
            min_val = j
    
    print(max_val-min_val+1)


def parttwo_quadratic(input):
    with open(input, 'r') as fp:
        lines = fp.read().split('\n')

    time = int(lines[0].replace(' ', ''))
    distance = int(lines[1].replace(' ', ''))

    min_d = (-time+((pow(time,2)-4*distance)**0.5))/(-2)
    max_d = (-time-((pow(time,2)-4*distance)**0.5))/(-2)

    result = math.floor(max_d - min_d)+1

    print(result)

partone('test')
parttwo('input')
parttwo_minmax('input')
parttwo_quadratic('input')
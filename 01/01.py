import time

def partone(file):
    sum = 0
    
    with open(file, 'r') as fp:
        for line in fp.read().split():
            first = last = None
            for char in line:
                if first == None:
                    if char.isdigit():
                        first = last = char
                else:
                    if char.isdigit():
                        last = char
            sum += int(first+last)

    print(sum)

def parttwo(file):
    digits = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
    sum = 0

    with open(file, 'r') as fp:
        for line in fp.read().split():
            for i in range(len(line)+1):
                for key in digits:
                    if key in line[:i]:
                        line = line.replace(key, digits[key])
            first = last = None
            for char in line:
                if first == None:
                    if char.isdigit():
                        first = last = char
                else:
                    if char.isdigit():
                        last = char
            sum += int(first+last)

    print(sum)

partone('input')
parttwo('input')
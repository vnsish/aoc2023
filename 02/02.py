def partone(input):
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    valid_games = 0
    
    with open(input, 'r') as fp:
        for i, line in enumerate(fp.read().split('\n')):
            invalid = False
            valid_games += i+1
            for draw in line.split('; '):
                for cube_count in draw.split(', '):
                    if int(cube_count.split(' ')[0]) > max_cubes[cube_count.split(' ')[1]]:
                        invalid = True
                        valid_games -= i+1
                        break
                if invalid: break
    print(valid_games)

def parttwo(input):
    power_sum=0
    
    with open(input, 'r') as fp:
        for i, line in enumerate(fp.read().split('\n')):
            min_r = 0
            min_g = 0
            min_b = 0
            for draw in line.split('; '):
                for cube_count in draw.split(', '):
                    match cube_count.split(' ')[1]:
                        case 'red':
                            if min_r < int(cube_count.split(' ')[0]):
                                min_r = int(cube_count.split(' ')[0])
                        case 'green':
                            if min_g < int(cube_count.split(' ')[0]):
                                min_g = int(cube_count.split(' ')[0])
                        case 'blue':
                            if min_b < int(cube_count.split(' ')[0]):
                                min_b = int(cube_count.split(' ')[0])
            power_sum += (min_r*min_g*min_b)
    
    print(power_sum)


partone('input')
parttwo('input')
def partone(input):
    with open(input, 'r') as fp:
        data = fp.read().split('\nx\n')
    
    seeds = [int(x) for x in data[0].split()]
    steps = {}
    for i,step in enumerate(data[1:]):
        steps[i] = []
        for mrange in step.split('\n'):
            steps[i].append([int(x) for x in mrange.split()])
    final_loc = []
    for seed in seeds:
        for step in steps:
            for i in range(len(steps[step])):
                if seed >= steps[step][i][1] and seed < steps[step][i][1]+steps[step][i][2]:
                    seed = steps[step][i][0] + (seed - steps[step][i][1])
                    break
        final_loc.append(seed)
        
    print(f'{min(final_loc)}')

def process_seed(seed, steps):
    for step in steps:
            for i in range(len(steps[step])):
                if seed >= steps[step][i][1] and seed < steps[step][i][1]+steps[step][i][2]:
                    seed = steps[step][i][0] + (seed - steps[step][i][1])
                    break
    return seed

#very slow
def parttwo(input):
    with open(input, 'r') as fp:
        data = fp.read().split('\nx\n')
    
    seedranges = [int(x) for x in data[0].split()]
    
    steps = {}
    for i,step in enumerate(data[1:]):
        steps[i] = []
        for mrange in step.split('\n'):
            steps[i].append([int(x) for x in mrange.split()])
    
    min_loc = -1
    
    for srange in range(0, len(seedranges), 2):
        print(f'processing range {seedranges[srange]} -> {seedranges[srange]+seedranges[srange+1]}')
        for seed in range(seedranges[srange],seedranges[srange]+seedranges[srange+1]):
            seed = process_seed(seed, steps)
            if min_loc == -1:
                min_loc = seed
            elif seed < min_loc:
                min_loc = seed

        
    print(min_loc)

def reverse_step(loc, steps, cur):
    matched = False
    if cur == 0:
        return loc
    
    for step in steps[cur-1]:
        if loc in step[0]:
            matched = True
            loc = reverse_step(loc-step[0][0]+step[1], steps, cur-1)
            break

    if not matched:
        loc = reverse_step(loc, steps, cur-1)
    
    return loc

#faster, but still slow
def parttwo_reverse(input):

    with open(input, 'r') as fp:
        data = fp.read().split('\nx\n')
    
    seeds = []
    seedranges = [int(x) for x in data[0].split()]
    for i in range(0, len(seedranges), 2):
        seeds.append(range(seedranges[i], seedranges[i]+seedranges[i+1]))

    steps = {}
    for i,step in enumerate(data[1:]):
        steps[i] = []
        for mrange in step.split('\n'):
            values = [int(x) for x in mrange.split()]
            steps[i].append((range(values[0], values[0]+values[2]), values[1]))
    
    
    found = False
    i = 0
    while not found:
        seed = reverse_step(i, steps, 7)
        for seedrange in seeds:
            if seed in seedrange:
                found = True

        if i%100000 == 0:
            print(f'currently processing {i}')
        if not found:
            i += 1
            
    print(i)


partone('input')
#parttwo('input')
parttwo_reverse('input')

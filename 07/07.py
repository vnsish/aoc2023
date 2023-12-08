from collections import Counter
from operator import itemgetter

def partone(input):
    stringo = 'AKQJT98765432'
    card_power = [x for x in stringo]

    with open(input, 'r') as fp: 
        lines = fp.read().split('\n')

    hands = {}
    for line in lines:
        hands[line.split()[0]] = int(line.split()[1])

    hand_type = {}
    
    for hand in hands:
        power = 0
        card_count = Counter(hand)
        max_card = max(card_count, key=card_count.get)
        #power = count of card with max frequency - number of different cards
        power = card_count[max_card] - len(card_count)-1
        if power not in hand_type:
            hand_type[power] = []
            hand_type[power].append(hand)
        else:
            hand_type[power].append(hand)
    
    hand_type = dict(sorted(hand_type.items()))

    rank = 1
    total_wins = 0

    for key in hand_type:
        if len(hand_type[key]) == 1:
            total_wins += rank*hands[hand_type[key][0]]
            rank+=1
        else:
            sorted_ranks = sorted(hand_type[key], key=lambda word: [card_power.index(c) for c in word], reverse=True)
            for hand_rank in sorted_ranks:
                total_wins += rank*hands[hand_rank]
                rank+=1
    
    print(total_wins)

def parttwo(input):
    stringo = 'AKQT98765432J'
    card_power = [x for x in stringo]

    with open(input, 'r') as fp: 
        lines = fp.read().split('\n')

    hands = {}
    for line in lines:
        hands[line.split()[0]] = int(line.split()[1])

    hand_type = {}
    
    for hand in hands:
        power = 0
        card_count = Counter(hand)
        card_count_sorted = sorted(card_count.items(), key=lambda x:x[1], reverse=True)
        max_card = max(card_count, key=card_count.get)
        if 'J' in card_count:
            if max_card == 'J' and card_count['J'] == 5:
                power = 3
            elif max_card == 'J' and len(card_count) == 5:
                power = -3
            elif max_card == 'J':
                max_card = card_count_sorted[1][0]
                card_count[max_card] += card_count['J']+1
                power = card_count[max_card] - len(card_count)-1
            else:
                card_count[max_card] += card_count['J']
                power = card_count[max_card] - len(card_count)
        else:
            power = card_count[max_card] - len(card_count)-1
        if power not in hand_type:
            hand_type[power] = []
            hand_type[power].append(hand)
        else:
            hand_type[power].append(hand)
    
    hand_type = dict(sorted(hand_type.items()))

    rank = 1
    total_wins = 0

    for key in hand_type:
        if len(hand_type[key]) == 1:
            total_wins += rank*hands[hand_type[key][0]]
            rank+=1
        else:
            sorted_ranks = sorted(hand_type[key], key=lambda word: [card_power.index(c) for c in word], reverse=True)
            for hand_rank in sorted_ranks:
                total_wins += rank*hands[hand_rank]
                rank+=1
    print(total_wins)

partone('test')
parttwo('input')
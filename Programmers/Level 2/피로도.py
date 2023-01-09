import itertools

def solution(k, dungeons):
    result = 0
    sequence = [i for i in range(len(dungeons))]
    
    for case in itertools.permutations(sequence, len(dungeons)):
        count = 0
        energy = k
        for i in case:
            if dungeons[i][0] <= energy:
                count += 1
                energy -= dungeons[i][1]
        if count > result:
            result = count
    return result
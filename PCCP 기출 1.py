def solution(bandage, health, attacks):
    answer = 0
    time = 0
    HP = health
    t = 0
    j = 0
    hps = bandage[1]
    end = bandage[2]
    
    for i in range (0, attacks[-1][0]):
        time += 1
        if attacks[j][0] == time:
            HP = HP - attacks[j][1]
            t = 0
            j= j+1
            if 0 > HP or 0 == HP:
                return -1
            continue
        elif health > HP:
            HP = HP + hps
            t = t + 1
            if HP >= health:
                HP = health
            if t == bandage[0]:
                HP = HP + end
                t = 0
                if HP >= health:
                    HP = health
        else:
            t = t + 1
        if 0 > HP or 0 == HP:
            return -1
    
    return HP
    

import random
#roll 7 sets of 4d6 keep the highest 3 of the d6 per set and drop the lowest set of 4d6
def rolling_die_six ():
    die_six = [random.randrange (1,7),random.randrange (1,7),random.randrange (1,7),
    random.randrange (1,7),random.randrange (1,7),random.randrange (1,7),]
    die_six.sort()
    rolled_die_six = die_six[3:]
    stat = sum(rolled_die_six)
    return stat

def stat_array ():
    array = []
    for i in range(7):
        stat = rolling_die_six()
        array.append(stat)
    array.sort()
    array.pop(0)
    return array


def set_stat(index):
    stat = {}
    x = float(index)
    if x == 1:
        stat = {index: -5}
    elif x == 2 or x == 3:
        stat = {index: -4}
    elif x == 4 or x == 5:
        stat = {index: -3}
    elif x == 6 or x ==7:
        stat = {index: -2}
    elif x == 8 or x ==9:
        stat = {index: -1}
    elif x == 10 or x ==11:
        stat = {index: +0}
    elif x == 12 or x ==13:
        stat = {index: +1}
    elif x == 14 or x ==15:
        stat = {index: +2}
    elif x == 16 or x ==17:
        stat = {index: +3}
    elif x == 18 or x ==19:
        stat = {index: +4}
    elif x == 20 or x ==21:
        stat = {index: +5}
    
    return stat

def end_stats ():       
    stats = stat_array() 
    stat1 = set_stat(stats[0])
    stat2= set_stat(stats[1])
    stat3= set_stat(stats[2])
    stat4= set_stat(stats[3])
    stat5= set_stat(stats[4])
    stat6= set_stat(stats[5])
    modified_stat = f"Stat One: {stat1},Stat Two: {stat2},Stat Three: {stat3},Stat Four: {stat4},Stat Five: {stat5},Stat Six: {stat6},"
    # modified_stats = [stat1, stat2, stat3, stat4, stat5, stat6]
   
    return modified_stat


print(end_stats())
#Base stat placement off preference?
#User enter prefered stats -> highest stats are added to the prefered stats -> rest are randomly placed



        


    


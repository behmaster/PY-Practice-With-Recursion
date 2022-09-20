# Write code for algorithm 3 below

def algo3(num):
    if num <= 0:
        return num
    elif num==1:
        return 0
    elif num==2:
        return 1
    else:
        return algo3(num-1)+algo3(num-2) 

print(algo3(10))
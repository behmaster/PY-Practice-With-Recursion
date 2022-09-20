# Write code for algorithm 4 below
def algo4(a,b):
    if b < 1:
        return 0
    elif b == 1:
        return a
    else:
        return a * algo4(a,b-1)

algo4(4,4)
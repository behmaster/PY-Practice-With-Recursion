# Write code for algorithm 1 below

def algo1(num):
    if num < 1:
        return
    else:
        print(num)
        return (algo1(num-1))

algo1(0)
algo1(5)
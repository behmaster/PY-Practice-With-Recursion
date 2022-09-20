# Write code for algorithm 2 below
def algo2(n, i=1):
    if i > n:
        return
    else:
        print(i)
        algo2(n,i+1)

# algo2(0)
algo2(5)

def automorf(n):
    sq = n**2
    l = len(str(n))
    return sq % (10**l) == n


print(automorf(5))
print(automorf(7))
print(automorf(25))


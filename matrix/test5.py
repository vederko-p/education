# ---| 5 |---

def sdvig(lst):
    l = len(lst)
    for i in range(l-1):
        lst[i] = lst[i-1]
    return lst

print(sdvig([1,2,3,4,5]))
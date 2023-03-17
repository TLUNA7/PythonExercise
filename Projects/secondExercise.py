def bigger_is_greater(t,w):
    if w.isdigit():
        return "Try Again!"
    listW = list(w)
    i = len(listW) - 2

    while i >= 0 and listW[i] >= listW[i+1]:

        i-=1
    j = len(listW) - 1
    while j >= 0 and listW[j] <= listW[i]:
        j -= 1
    listW[i], listW[j] = listW[j], listW[i]

    w1 = listW[:+1] + listW[i+1:][::-1]

    w1 = "".join(w1)
    return w1
    

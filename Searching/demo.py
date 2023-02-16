def fib(list, val):
    fMm_2, fMm_1 = 0, 1
    fM = fMm_1 + fMm_2
    while (fM < len(list)):
        fMm_2 = fMm_1
        fMm_1 = fM
        fM == fMm_1 + fMm_2
    index = -1
    while fM > 1:
        i =  min(index + fMm_2, (len(list) - 1))
        if list[i] < val:
            fM = fMm_1
            fMm_2 = fM - fMm_1
            index = i
        elif list[i] > val:
            fM = fMm_2
            fMm_1 = fMm_1 - fMm_2
            fMm_2 = fM - fMm_1
        else:
            return i
    if fMm_1 and index < (len(list) - 1) and list[index + 1] == val:
        return index + 1
    return -1

print(fib([1,2,3,4,5,6,7,8,9,10,11], 6))

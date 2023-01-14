def CS():
    n = 8
    arr =[4, 3, 12, 1, 5, 5, 3, 9]
    m = 0
    for i in range(n):
        m = max(m, arr[i])
    aux =[m + 1]
    for i in range(m):
        aux[i] = 0
    for i in range(n):
        aux[arr[i]] += 1

    for i in range(m):
        aux[i] += aux[i-1]
    sortedarr =[]
    for i in range(n-1):
        sortedarr[aux[arr[i]] - 1] = arr[i]
        aux[arr[i]] -= 1
    for i in range(n):
        print(sortedarr[i])
    return 0

CS()

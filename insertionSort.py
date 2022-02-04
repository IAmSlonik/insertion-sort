def iSort(array, length):
    for i in range(1, length):
        #print(array)
        #print(length)
        pom = array[i]
        #print(pom)
        k = i - 1
        while k >= 0 and pom < array[k]:
            array[k + 1] = array[k]
            #print(array[k + 1])
            k = k - 1
        array[k + 1] = pom

arr = []
print("Podaj długość tablicy:")
length = int(input())
for es in range(length):
    print("Podaj liczbę ", (es + 1), ":")
    arr.append(int(input()))
iSort(arr, length)
print(arr)




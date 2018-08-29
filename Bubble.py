unsorted = [1,2,9,8,6,6,5,4,2,124,54,12,18,98,0.3,3]

for x in unsorted:
    for num in range(0,len(unsorted) - 1):
        if unsorted[num + 1] < unsorted[num]:
            unsorted[num + 1],unsorted[num] = unsorted[num],unsorted[num + 1]

print(unsorted)



# Or a better way
unsort = [1,24,544,32,4,5,69,69,490,24]

print(sorted(unsort))

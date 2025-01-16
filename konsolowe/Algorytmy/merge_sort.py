def mergeSort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        left = tab[:mid]
        right = tab [mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1

            k += 1


        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            tab[k] = right[j]
            j+= 1
            k +=1

        return tab

print(mergeSort([12, 12, 2, 3, 5, 6, 7]))
print(mergeSort([12, 11, 132, -3, 5, 56, 7]))
print(mergeSort([13, 12, 15, 3, 10, 11, 37]))
print(mergeSort([4, 2, 8, 1, 1, 7, 3]))


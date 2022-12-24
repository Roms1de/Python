import math


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


# list of random numbers
list = [345, 4556, 67, 43, 567, 234, 67, 34, 567, 234, 567, 78678, 567567, 456456, 34, 45665756, 345, 1, 567567567, 7686, 56546]
new_list = bubble_sort(list)
count, summ = 0, 0
maxx = -math.e
for i in range(len(new_list)):
    if new_list[i] < 10000:
        count += 1
        summ += new_list[i]
        maxx = max(maxx, summ)

print(count, maxx, sep="")
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
start, end = map(int, input().split())
extracted = lst1[start-1:end]
extracted.reverse()
lst2.extend(extracted)
del lst1[start-1:end]
print(lst1)
print(lst2)

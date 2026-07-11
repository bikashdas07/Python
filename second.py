l1 = [3, 6, 9]
l2 = [5, 10, 15]
l3 = [6, 12, 18]
print("Original list:")
print(l1)
print(l2)
print(l3)
sum = map(lambda x, y, z: x + y + z, l1, l2, l3)
print("Resulted list: ")
print(list(sum))
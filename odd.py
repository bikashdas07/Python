def odd_increase():
    lis1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in range(len(lis1)):
        if i%2==0:
            i+1
            print(i)
        else:
            print(i+5)
            odd_increase()
class targetSum:
    numbers = [10,20,10,40,50,60,70]
    n = len(numbers)
    target = int(input("Enter target Number: "))
    dict = {}
    count = 0;
    for i in range(0,n):
        for j in range(0,n):
            if((numbers[i]+numbers[j]) == target):
                count+=1
                dict.update({count:[i,j]})

    print(dict)
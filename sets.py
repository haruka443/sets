lst1 = []
lst2 = []
while len(lst1) != 5 or len(lst2) != 5:
    lst1 = input('Input 5 numbers for the first list splitting them with ",": ').split(',')
    lst2 = input('Input 5 numbers fot the second list splitting them with ",": ').split(',')
    if len(lst1) != 5 or len(lst2) != 5:
        print('The lists should consist of 5 numbers!')

try:
    sum = [int(x) + int(y) for x, y in zip(lst1, lst2)]
    print(sum)

    set1 = set(lst1)
    set2 = set(lst2)

    print('-' * 10)
    print('Sum of the sets')
    print(set1 | set2)

    print('-' * 10)
    print('Intersection of the sets')
    print(set1 & set2)

    print('-' * 10)
    print('Everything beyond intersection of the sets')
    print(set1 ^ set2)
    
except ValueError:
    print('The lists must consist only of numbers')



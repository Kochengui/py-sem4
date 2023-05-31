
# 1).

n=int(input('введите кол-во элементов первого множества: '))
set1=set([int(i) for i in input(f'введите {n} элементов первого множества: ').split()])

m=int(input('введите кол-во элементов второго множества: '))
set2=set([int(i) for i in input(f'введите {m} элементов второго множества: ').split()])

set3=set1.intersection(set2)
to_list=list(set3)
to_list.sort()

print(set3)



# 2).

bush=int(input('введите кол-во кустов: '))
bushes=[int(i) for i in input(f'введите колличество ягод на каждом кусту: ').split()]
print(bushes)
summ=0
max_bush=0

  
for i in range(bush):
       
        if bushes[i]==bushes[-1]:
                summ=bushes[i]+bushes[0]+bushes[i-1]
                # print(summ)
        elif  bushes[i]==bushes[0]:
                summ=bushes[i]+bushes[-1]+bushes[i+1]
                # print(summ)
        elif bushes[i]!=bushes[0] and bushes[i]!=bushes[-1]:
                summ=bushes[i]+bushes[i+1]+bushes[i-1]
                # print(summ)
        if summ>max_bush:
                max_bush=summ
print(f'максимальное число ягод, которое может собрать за один заход собирающий модуль равен = {max_bush} ягод')

        

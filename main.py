#1-misol
a = (3, 5, 7, 9)
print("Yigiundi", sum(a))

#2-misol
numbers = tuple(map(int, input("Son kirit: ").split()))
print(numbers)

#3-misol
t1 = (1, 3, 6, 7)
t2 = (4, 5, 8, 9)
yangi_t = t1 + t2
print(yangi_t)

#4-misol
numbers = (1, 2, 3, 4, 5, 6, 7, 8)

juftlar = ()  # bu yerda yangi tuple ochamiz

for i in numbers:
    if i % 2 == 0:
        juftlar += (i,)

print(f"Juft sonlar: {juftlar}")

#5-misol
my_tuple = (2, 3, 18, 12, 31)
teskari_tuple = my_tuple[::-1]
print(teskari_tuple)





# 3. Create a generator function using the yield keyword that produces numbers from 1 to
# 5 one by one to illustrate how lazy evaluation can save memory when dealing with large
# datasets.
def num_generator(num):
    i=1
    while i<=num:
        yield i
        i+=1

numbers=num_generator(5)
for number in numbers:
    print(number)
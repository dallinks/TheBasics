def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean
print(mean([1,4,5]))
def squaremaker(num):
    square = num*num
    return square

x = input("Enter Number to be Squared:")

print(squaremaker(float(x)))
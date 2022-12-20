numbers = list(range(1,10))
print(numbers)

numbers = list(range(1,10,2))
print(numbers)

numbers = []
for number in range(2,10):
    numbers.append(number)
print(numbers) 

##maximum and minimum values
print(max(numbers)) 
print(min(numbers))  

##sum numbers
print(sum(numbers))

GB = []
for num in range(1,1000001):
    GB.append(num)
print("sum of 1 million numbers " + str(sum(GB)))
print("maximum number in list of 1- 1 million " + str(max(GB))) 
print(min(GB))   

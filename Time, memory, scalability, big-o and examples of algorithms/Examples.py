
input = [1,2,3,4,5]
coloumn = []
row = []

#TIME EXAMPLES
#O(n)
def function_example1():
    for num in input:
        print(num)
    return


#O(n*2)
def function_example2():
    for num in input:
        print(num)
    for num in input:
        print(num)
    return


#O(n^2)
def function_example3():
    for num1 in input:  
        for num2 in input:
            print(num1)
            print(num2)
    return


#O(n^2)
def function_example4():
    for num in input:
        print(num)
    for num1 in input:  
        for num2 in input:
            print(num1)
            print(num2)
    
#MEMORY EXAMPLE
#O(n^2)   
def function_example5():
    for i in range(len(input)):
        row.append(i)
        for j in range(len(input)):
            coloumn.append(j)
    matrix = [[row], [coloumn]]
    return matrix
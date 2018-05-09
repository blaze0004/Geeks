# Program for array rotation
# Best is method 3

# Method 1 Using Temp array 
# Time Complexity = O(n)
# Space Complexity = O(d)

def method1():
    import array

    def rotateLeft(arr, times, n):
        
        temp = array.array('i', arr[:times])

        for i in range(times):
            arr = arr[1:n]

        for i in temp:
            arr.append(i)        



    def rotateRight(arr, times, n):
        pass

    arr = array.array('i', [int(i) for i in range(10)])

    rotateLeft(arr, 3, 10)
    print(arr)

    rotateRight(arr, 3, 10)
    print(arr)

# Method 2 Rotate One By One
# Time Complexity = O(n*d)
# Space Complexity = O(1)

def method2():
    import array

    def rotateLeftByOne(arr, n):
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]

        arr[n-1] = temp 

    def rotateRightByOne(arr, n):
        temp = arr[n-1]
    
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]

        arr[0] = temp

    def rotateLeft(arr, times , n):
        for i in range(times):
            rotateLeftByOne(arr,n)

    def rotateRight(arr, times, n):
        for i in range(times):
            rotateRightByOne(arr, n)

    arr = array.array('i', [1,2,3,4,5,6,7,8,9,10])

    print("Initial Array is: ")
    print(arr)

    rotateLeft(arr, 3, 10)
    print(arr)

    rotateRight(arr, 3, 10)
    print(arr)


#Driver Program
methodChoice = 0
while(methodChoice != -1):
    methodChoice = int(input("Choose A Method: \n1. Use Temperory Array\t2.Rotate One By One\t3. The Juggling Algorithm \n"))
    if methodChoice == 1:
        method1()
    elif methodChoice == 2:
        method2()
    elif methodChoice == 3:
        method3()
    elif methodChoice not in [1,2,3]:
        break


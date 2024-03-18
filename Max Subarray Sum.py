#Question
'''
Develop a program to read an array of n elements and print the maximum subarray sum

I/P Format:-
Read the number of elements (n) in the array in line 1

Read n numbers in the next n lines

O/P Format:-
Print the maximum subarray sum
'''

def max_subarray(A, low, high):
    if (low == high):
        return A[low]
    else:
        mid = (low+high) // 2
        leftsub_sum = max_subarray(A, low, mid)
        rightsub_sum = max_subarray(A, mid+1, high)
        crosssub_sum = cross_subarray(A, low, high, mid)
    
    return max(leftsub_sum, rightsub_sum, crosssub_sum)

def cross_subarray(A, low, high, mid):
    sum = 0
    leftsum = rightsum = float('-inf')

    for i in range(mid, low, -1):
        sum += A[i]
        if leftsum < sum :
            leftsum = sum
    sum = 0
    for i in range(mid+1, high+1):
        sum += A[i]
        if rightsum < sum :
            rightsum = sum
    
    return (leftsum + rightsum)

Array = []

for i in range(int(input('Enter the number of elements: '))):
    Array.append(int(input(f'Enter the {i+1} element of Array: ')))

low = 0
high = len(Array) - 1

print("Max Sum:",max_subarray(Array, low, high))
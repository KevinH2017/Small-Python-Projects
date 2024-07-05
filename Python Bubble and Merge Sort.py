# Python Bubble and Merge Sort

# Bubble Sort
# Makes checks with neighboring values to change order of array values from lowest to highest

# Function to sort array by bubble method
def bubble_sort(arr):
    swapped = False
    arr_len = len(arr)
    # Goes through all of array
    for i in range(arr_len - 1):
        for j in range(0, arr_len-i-1):
            # Swap elements if element is greater than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

# Array before it is sorted
bubble = [64, 34, 25, 12, 22, 11, 90]
print("Array before bubble sort: ", bubble)

bubble_sort(bubble)

# Array after it is sorted
print("Sorted Array Using Bubble Method: ")
for i in range(len(bubble)):
    print("% d" % bubble[i], end=" ")

print()

# Merge Sort
# Breaks down an array into smaller arrays to be sorted and then puts them back together

# # Divides array into temporary sub-arrays and merges them back into one array
# def merge_func(arr, l, m, r):
#     # First subarray is arr[l..m]
#     # Second subarray is arr[m+1..r]
#     arr_1 = m - l + 1
#     arr_2 = r - m

#     temp_arr_1 = [0] * (arr_1)
#     temp_arr_2 = [0] * (arr_2)

#     for i in range(0, arr_1):
#         temp_arr_1[i] = arr[l + i]

#     for j in range(0, arr_2):
#         temp_arr_2[j] = arr[m + 1 + j]

#     i = 0           # Initial index of first sub-array
#     j = 0           # Initial index of second sub-array
#     k = l           # Initial index of merged sub-array

#     while i < arr_1 and j < arr_2:
#         if temp_arr_1[i] <= temp_arr_2[j]:
#             arr[k] = temp_arr_1[i]
#             i += 1
#         else:
#             arr[k] = temp_arr_2[j]
#             j += 1
#         k += 1

#     # Copy the remaining elements of temp_arr_1
#     while i < arr_1:
#         arr[k] = temp_arr_1[i]
#         i += 1
#         k += 1

#     # Copy the remaining elements of temp_arr_2
#     while j < arr_2:
#         arr[k] = temp_arr_2[j]
#         j += 1
#         k += 1

# # Function to sort array by merge method
# def merge_sort(arr, l, r):
#     if l < r:

#         m = l + (r-1) // 2

#         merge_sort(arr, l, m)
#         merge_sort(arr, m+1, r)
#         merge_func(arr, l, m, r)

# # Array before it is sorted
# merge = [12, 11, 13, 5, 6, 7]
# merge_len = len(merge)
# print("Array before merge sort: ", merge)

# merge_sort(merge, 0, merge_len-1)
# print("\nSorted Array using Merge Method: ")
# for i in range(merge_len):
#     print("% d" % merge[i], end=" ")

def merge(arr, l, m, r):
	arr_1 = m - l + 1
	arr_2 = r - m

	# create temp arrays
	temp_arr_1 = [0] * (arr_1)
	temp_arr_2 = [0] * (arr_2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, arr_1):
		temp_arr_1[i] = arr[l + i]

	for j in range(0, arr_2):
		temp_arr_2[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < arr_1 and j < arr_2:
		if temp_arr_1[i] <= temp_arr_2[j]:
			arr[k] = temp_arr_1[i]
			i += 1
		else:
			arr[k] = temp_arr_2[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < arr_1:
		arr[k] = temp_arr_1[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < arr_2:
		arr[k] = temp_arr_2[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")
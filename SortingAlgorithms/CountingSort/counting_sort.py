def counting_sort(arr: list[int]) -> list[int]:

    # Step 1: Find the maximum value to determine the range of count array
    max_val = max(arr)

    # Step 2: Initialize the count array with zeroes
    count = [0] * (max_val + 1)

    # Step 3: Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Step 4: Update count array to store cumulative positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build the output array, iterate in reverse to maintain stability
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Example usage
my_list = [3, 3, 1, 2, 2, 1, 4]
sorted_list = counting_sort(my_list)
print(f"Sorted Array: {sorted_list}")
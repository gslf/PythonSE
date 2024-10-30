def bucket_sort(arr):
    # Step 1: Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    
    # Step 2: Insert elements into respective buckets
    for value in arr:
        # Determine the appropriate bucket for each value
        bucket_index = int(value * num_buckets)
        buckets[bucket_index].append(value)

    # Step 3: Sort individual buckets using Insertion Sort
    def insertion_sort(bucket):
        for i in range(1, len(bucket)):
            current_value = bucket[i]
            j = i - 1
            while j >= 0 and current_value < bucket[j]:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = current_value
        return bucket

    sorted_array = []
    for bucket in buckets:
        # Sort each bucket and extend to the sorted array
        sorted_array.extend(insertion_sort(bucket))
    
    return sorted_array


data = [0.64, 0.5, 0.25, 0.12, 0.22, 0.11, 0.90]
sorted_data = bucket_sort(data)
print("Sorted Data:", sorted_data)
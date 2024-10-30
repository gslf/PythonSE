# The Bucket Sort algorithm in Python

Bucket Sort is a distribution sort that works by partitioning an array into a number of smaller 'buckets' and then sorting these individual buckets. It is most effective when the input data is uniformly distributed across a known range, which means it's particularly well-suited for scenarios with floating-point values between 0 and 1.  This is because values in this range can be easily mapped into evenly spaced buckets, ensuring a balanced distribution across all buckets. This balanced distribution minimizes the likelihood of any bucket becoming overloaded, which optimizes the overall efficiency of the sorting process. Additionally, the limited range allows for simple calculations to determine bucket placement, reducing computational overhead.

Think of Bucket Sort as organizing a motorsport team preparing for a race. Imagine the team needs to sort different car components such as tires, fuel, and engine parts. To do this efficiently, they create separate buckets for each component type. Once sorted into buckets, the components can then be organized for quick access during the race, ensuring the team can make rapid, strategic adjustments. This process is similar to how Bucket Sort groups elements, sorts each group, and then puts them all together to achieve a fully optimized result.



## How it work
The algorithm typically follows these steps:

1. Divide: The input data is divided into several evenly distributed buckets.
2. Sort: Each bucket is then sorted individually, often using another sorting algorithm (like Insertion Sort).
3. Combine: Finally, the sorted buckets are combined into a single array, giving us the fully sorted output.

![Bucked Sort algorithm - visual representation](/SortingAlgorithms/BucketSort/res/bucket_sort_visualization.png)

## Implementation
Here is an implementation of the vucket sort algorithm in python:

```python
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
```
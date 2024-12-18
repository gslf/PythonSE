# External Sort in Python
Unlike in-memory sorting algorithms such as QuickSort or MergeSort, External Sort is specifically designed for scenarios where datasets are too large to be stored entirely in RAM. It operates by dividing the dataset into smaller chunks that fit into memory, sorting these chunks, and then merging them to produce the final sorted output.

The External Sort algorithm is typically implemented as an External Merge Sort, which comprises two main phases:

1. Divide and Sort (Run Generation): The large dataset is split into smaller, manageable chunks (runs) that can fit into memory. Each chunk is loaded into memory, sorted using an efficient in-memory sorting algorithm, and written back to disk.
2. Merge Phase: The sorted runs are progressively merged into a single sorted file. Instead of merging two runs at a time, modern implementations use a k-way merge strategy, where k is determined by the number of chunks that can be processed simultaneously in memory.

This algorithm can be likened to the process of organizing a vast collection of books. The objective is to alphabetize the entire collection, but the constraint is that only a limited number of books can be transported at a time. The process begins by loading as many books as possible into a vehicle, sorting them immediately, and then returning the now-organized books to their respective warehouse. This procedure is repeated for all warehouses, ensuring that each subset of books is perfectly ordered. Once every warehouse has been processed, a centralized system—akin to a massive conveyor belt—gathers the sorted sections. A sophisticated merging algorithm is then employed to efficiently combine these sorted subsets into a single, seamlessly ordered collection.

![External Sort algorithm - visual representation](/SortingAlgorithms/ExternalSort/res/external_sort_visualization.png)

This algorithm finds critical applications in domains such as database management systems, large-scale analytics, and big data processing, where handling datasets spanning gigabytes or terabytes is commonplace.

## Implementation

```python
import heapq
import os

def merge_files(output_file, chunk_size):
    """
    Merges sorted data from temporary files into a single output file.

    Args:
        output_file (str): Path to the output file.
        chunk_size (int): Number of lines to buffer before writing to the output file.
    """

    buffer_size = 1000  # Number of lines to buffer before writing
    buffer = []  # Buffer to accumulate lines for writing

    heap = []
    temp_files = [file for file in os.listdir('.') if file.startswith('temp_')]

    # Open temporary files
    in_files = [open(temp_file, 'r') for temp_file in temp_files]

    # Initialize the heap
    for i, f in enumerate(in_files):
        element = f.readline().strip()
        if element:  # Skip empty lines
            heap.append((element, i))
    heapq.heapify(heap)  # Transform list into a heap in O(n)


    with open(output_file, "w") as out:
        while heap:
            # Extract the smallest element from the heap
            root = heapq.heappop(heap)
            buffer.append(root[0])  # Add to the buffer

            # Write the buffer to disk if it's full
            if len(buffer) >= buffer_size:
                out.write('\n'.join(buffer) + '\n')
                buffer = []

            # Read the next element from the corresponding file
            element = in_files[root[1]].readline().strip()
            if element:  # Skip empty lines
                heapq.heappush(heap, (element, root[1]))

        # Write any remaining lines in the buffer
        if buffer:
            out.write('\n'.join(buffer) + '\n')

    # Close temporary files
    for file in in_files:
        file.close()

    # Delete temporary files
    for temp_file in temp_files:
        os.remove(temp_file)

def create_initial_runs(input_file, chunk_size):
    """
    Reads chunks of data from an input file, sorts them, and writes sorted chunks to temporary files.

    Args:
        input_file (str): Path to the input file.
        chunk_size (int): Number of lines to process per chunk.
    """
    chunk_index = 0

    with open(input_file, "r") as in_file:
        while True:
            # Read a chunk of lines
            data = [line.strip() for _, line in zip(range(chunk_size), in_file) if line.strip()]

            if not data:  # Exit loop if no more data
                break

            # Sort the data lexicographically
            data.sort()

            # Write the sorted data to a temporary file
            temp_file = f"temp_{chunk_index}"
            with open(temp_file, 'w') as out_file:
                out_file.write('\n'.join(data) + '\n')

            print(f"Chunk {chunk_index} written to {temp_file}")
            chunk_index += 1

def external_sort(input_file, output_file, chunk_size):
    """
    Performs external sorting on a large file by dividing it into chunks, sorting each chunk,
    and merging them into a single sorted output file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
        chunk_size (int): Number of lines to process per chunk.
    """
    create_initial_runs(input_file, chunk_size)
    merge_files(output_file, chunk_size)





# Test the code
chunk_size = 1000  # Size of each chunk

input_file = "commedia.txt"
output_file = "sorted_commedia.txt"

external_sort(input_file, output_file, chunk_size)

```

## Performances Analysis

**Time Complexity**

- Run Generation: Sorting each chunk of size M (where M is the chunk size) takes O(MlogM). If the dataset has N elements, and there are N/M chunks, this phase costs O((N/M)⋅MlogM)=O(NlogM).

- Merge Phase: The k-way merge over N/M chunks takes O(Nlog(N/M)).
Overall Time Complexity: O(NlogM+Nlog(N/M))=O(NlogN)

**Space Complexity**
The algorithm uses memory to store:

- One chunk of size M during the sort phase.
- Buffers for each of the k runs during the merge phase.

Disk space is required to store temporary sorted runs.
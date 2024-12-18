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



# Ask for file name
filename = input("Enter the filename (e.g., file.txt): ")

# Initialize counters
num_lines = 0
num_words = 0
num_chars = 0

try:
    with open(filename, 'r') as file:
        for line in file:
            num_lines += 1
            words = line.split()
            num_words += len(words)
            num_chars += len(line)

    # Print results
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of characters: {num_chars}")

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

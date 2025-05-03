import matplotlib.pyplot as plt

def plot_word_length_histogram(filename):
    word_lengths = []

    try:
        # Open and read the file
        with open(filename, 'r') as file:
            content = file.read()

            # Split content into words
            words = content.split()

            # Calculate length of each word and store it
            for word in words:
                cleaned_word = word.strip(",.!?;:()[]{}").lower()  # Clean punctuation and convert to lowercase
                word_lengths.append(len(cleaned_word))

        # Plotting the histogram of word lengths
        plt.hist(word_lengths, bins=range(1, max(word_lengths) + 1), edgecolor='black')
        plt.title("Histogram of Word Lengths")
        plt.xlabel("Word Length")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# Example usage:
filename = input("Enter the filename (e.g., textfile.txt): ")
plot_word_length_histogram(filename)

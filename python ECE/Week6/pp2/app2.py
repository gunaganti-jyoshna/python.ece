def find_n_letter_words_starting_with_vowel(filename, n):
    vowels = ('a', 'e', 'i', 'o', 'u')  # Vowels to check
    result = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()  # Split line into words
                for word in words:
                    word = word.strip(",.!?;:()[]{}").lower()  # Clean word of punctuation and lowercase it
                    if len(word) == n and word[0] in vowels:
                        result.append(word)
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    
    return result


# Example usage:
filename = input("Enter the filename (e.g., file.txt): ")
n = int(input("Enter the number of letters for the words (n): "))

matching_words = find_n_letter_words_starting_with_vowel(filename, n)

print(f"Words that are {n} letters long and start with a vowel: ")
print(matching_words)

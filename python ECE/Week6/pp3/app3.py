def extract_secret_message(paragraph, n):
    secret_message = []
    
    # Loop through the text and pick every nth character
    for i in range(n - 1, len(paragraph), n):  # Start from n-1 (because indexing starts from 0)
        secret_message.append(paragraph[i])
    
    # Join the characters to form the secret message
    return ''.join(secret_message)

# Example usage:
filename = input("Enter the filename (e.g., secret.txt): ")

try:
    with open(filename, 'r') as file:
        paragraph = file.read()  # Read the entire file content
        
    n = int(input("Enter the nth number to find the hidden message: "))
    secret_message = extract_secret_message(paragraph, n)
    
    print("Secret message found:")
    print(secret_message)
    
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

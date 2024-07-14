# Define a function to count the number of words in a given text
def count_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The input text to count words from.

    Returns:
        int: The number of words in the input text.
    """
    # Split the input text into a list of words using whitespace as the delimiter
    words = text.split()
    
    # Return the number of words in the list
    return len(words)


# Define a main function to handle user input and output
def main():
    """
    The main function that handles user input, counts the words, and displays the output.
    """
    # Prompt the user to enter a sentence or paragraph
    print("Welcome to the Word Counter program!")
    user_input = input("Please enter a sentence or paragraph: ")

    # Check if the user input is empty
    if not user_input:
        print("Error: Input cannot be empty. Please try again.")
        return

    # Count the number of words in the user input
    word_count = count_words(user_input)

    # Display the word count to the console
    print(f"The input contains {word_count} word(s).")


# Call the main function to start the program
if __name__ == "__main__":
    main()
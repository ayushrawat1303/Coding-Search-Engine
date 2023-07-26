import re

# List of common words to be removed from the text
common_words = ["Input", "Output", "Explaination", "Example", "the", "a", "an", "is", "are", "and", "in", "of", "to", "that", "or", "at"]

def writeToFile(pageContent, index):
    """
Write the provided `pageContent` to a new file named `questionContentLeetcode{index}.txt`.

    Parameters:
        pageContent (str): The content to be written to the file.
        index (int): The index used in the file name.
    """
    # Open a new file in write mode

    file= open(f'questionContentLeetcode{index}.txt','a+')
    file = open(f'cleanedQuestion/questionContentLeetcode{index}.txt', 'w')
        

    # Write the content to the file
    file.write(pageContent)
    # Close the file
    file.close()

def getPageContent(index):
 
    # Read the content from a file named `questionContent/questionContentLeetcode{index}.txt` 


    # Construct the file path using the provided index
    target_directory = f'questionContent/questionContentLeetcode{index}.txt'
    # Open the file in read mode
    file = open(target_directory, 'r')
    # Read the content from the file and store it in 'content'
    content = file.read()
    # Return the content as a string
    return content

def remove(pattern, pageContent):
    """
    Remove various patterns, numbers, and common words from the given `pageContent`.

    Parameters:
        pattern (str): Regular expression pattern to be removed from the text.
        pageContent (str): The text content to be cleaned.

    Returns:
        str: The cleaned text after removing patterns, numbers, and common words.
    """

    # here we are doing extensive cleaning at each step using regular expression

    # Remove all digits/numbers from the content
    pageContent = re.sub(r'\d+', '', pageContent) 

    # Remove the given pattern from the content using regular expression
    pageContent = re.sub(pattern, '', pageContent)

    # Replace multiple whitespaces with a single whitespace and remove leading/trailing whitespaces
    pageContent = re.sub(r'\s+', ' ', pageContent).strip()

    # Remove all special characters except for alphanumeric and whitespaces
    pageContent = re.sub(r'[^\w\s]', '', pageContent)

    # Remove single characters/words from the content
    pageContent = re.sub(r'\b\w\b', '', pageContent)

    # this line ensures that common words string(which is written at top) should not be present in any lower or uppercase form in page content
    pageContent = ' '.join([word for word in pageContent.split() if word.lower() not in common_words])

    return pageContent

def main_function():
    # Get the content from file with index 1
    pageContent = getPageContent(1)

    # we are removing all the text that is enclosed in square brackets like this "[ ]" to make processing fast
    pattern = r'\[.*?\]'

    # Clean the content by removing the pattern and common words
    pageContent = remove(pattern, pageContent)

    # Print the cleaned content (optional)
    print(pageContent)

    # Write the cleaned content to a new file with index 1
    writeToFile(pageContent, 1)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main_function()

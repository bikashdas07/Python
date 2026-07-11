# This code snippet is designed to print the contents of a specified directory(OS here).
import os

def print_directory_contents(path):
    """
    Prints the contents of a directory.
    
    Args:
        path (str): The path to the directory.
    """
    try:
        # Get the list of files and directories in the directory
        contents = os.listdir(path)
        
        # Print each item in the directory
        for item in contents:
            print(item)
    except OSError as e:
        print(f"Error accessing directory: {e}")

# Example usage
print_directory_contents("C:\\Users\\Asus\\Desktop\\Folders Association")
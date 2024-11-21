import os


def process_file() -> None:
    """
    Process files in a specific directory and print their contents.

    This function performs the following tasks:
    1. Prints the contents of the current working directory.
    2. Attempts to read and print the contents of files in the '/files_to_read' directory.

    If the '/files_to_read' directory does not exist, an error message is printed.

    Returns:
        None
    """
    # Print all content in the current directory
    current_directory: str = os.getcwd()
    print("Contents of the current directory:")
    for item in os.listdir(current_directory):
        print(item)
    print("\n")

    files_directory: str = "/files_to_read"

    if not os.path.exists(files_directory):
        print(f"Error: Directory {files_directory} does not exist.")
        return

    for filename in os.listdir(files_directory):
        file_path: str = os.path.join(files_directory, filename)

        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                content: str = file.read()
                print(f"Content of {filename}:")
                print(content)
                print("\n")


if __name__ == "__main__":
    process_file()

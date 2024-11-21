import os


def process_file() -> None:
    """
    Process files in a specific directory and print their contents.

    This function attempts to read and print the contents of files in the '/files_to_read' directory.

    If the '/files_to_read' directory does not exist, an error message is printed.

    Returns:
        None
    """

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

class FileNotFoundError(Exception):
    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__(f"File not found: {file_path}")

class InvalidInputDataError(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid input data: {message}")

class DiskSpaceFullError(Exception):
    def __init__(self, message):
        super().__init__(f"Disk space is full: {message}")

def read_input_data(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read and process the input data
            # Add your text processing logic here
            pass
    except FileNotFoundError as e:
        raise e  # Re-raise the custom FileNotFoundError
    except Exception as e:
        raise InvalidInputDataError(str(e))  # Raise InvalidInputDataError for unexpected input data

def store_processed_results(output_file_path, processed_data):
    try:
        with open(output_file_path, 'w') as output_file:
            # Write the processed data to the output file
            # Add your code to store the processed results here
            pass
    except IOError as e:
        raise DiskSpaceFullError(str(e))  # Raise DiskSpaceFullError for disk space full

def main():
    input_file_path = input("Enter the input file path: ")
    output_file_path = input("Enter the output file path: ")

    try:
        input_data = read_input_data(input_file_path)
        processed_data = process_text_data(input_data)
        store_processed_results(output_file_path, processed_data)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except InvalidInputDataError as e:
        print(f"Invalid Input Data: {e}")
    except DiskSpaceFullError as e:
        print(f"Disk Space Full: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

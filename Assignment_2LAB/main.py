import platform
import sys
import pandas
import numpy
import os

print("Current System:")
print("OS: ", platform.system())
print("OS version: ", platform.version())
print("Python version: ", sys.version)
print("Numpy version: ", numpy.__version__)
print("Pandas version: ", pandas.__version__)
print("")

class CustomException(Exception):
    pass

class OSNotFoundException(CustomException):
    pass

class OSSNotSupportedException(CustomException):
    pass

class OSVersionNotSupportedException(CustomException):
    pass

class PythonVersionNotFoundException(CustomException):
    pass

class LibsNotFoundException(CustomException):
    pass

class LibsVersionNotMentionedException(CustomException):
    pass

def validate_requirements(requirements):
    if 'OS' not in requirements:
        raise OSNotFoundException("OS not found")
    if platform.system() not in requirements:
        raise OSSNotSupportedException("OS not supported")
    # if platform.version() not in requirements:
    #     raise OSVersionNotSupportedException("OS version not supported")
    # if sys.version() not in requirements:
    #     raise PythonVersionNotFoundException("Python version not found")
    if 'numpy' not in requirements:
        raise LibsNotFoundException("Libs numpy not found")
    if 'pandas' not in requirements:
        raise LibsNotFoundException("Libs pandas not found")
    if numpy.__version__ not in requirements:
        raise LibsVersionNotMentionedException("numpy version not supported")
    if pandas.__version__ not in requirements:
        raise LibsVersionNotMentionedException("pandas version not supported")

def generate_output_file(output_data):
    with open('D:\Sem-5\\adv. python\Assignment_2L\\output.txt', 'w') as output_file:
        output_file.write(output_data)

def main():
    try:
        # Read the input file
        for file in os.listdir('D:\Sem-5\\adv. python\Assignment_2L'):
            if file.endswith(".txt"):
                with open (os.path.join('D:\Sem-5\\adv. python\Assignment_2L', file), 'r') as input_file:
                    requirements = input_file.read()  # Using eval for simplicity, use a safer alternative in production
                # print(requirements)
                # Validate the requirements
                validate_requirements(requirements)

                # Generate the output dynamically (for demonstration purposes, generating a simple output string)
                output_data = "Requirements validated successfully!\n"
                output_data += "Input requirements: {}\n\n".format(requirements)

                # Generate the output file
                generate_output_file(output_data)

                print("Output file 'output.txt' generated successfully.")
    except CustomException as e:
        print("Validation error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

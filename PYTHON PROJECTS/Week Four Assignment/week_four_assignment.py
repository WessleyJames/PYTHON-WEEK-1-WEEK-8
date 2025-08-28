# file: week_four_assignment.py

def read_and_modify_file(input_filename, output_filename="output.txt"):
    """
    Reads content from input_filename, modifies it, and writes to output_filename.
    Modification: convert all text to uppercase.
    """
    try:
        with open(input_filename, "r", encoding="utf-8") as infile:
            content = infile.read()

        modified_content = content.upper()

        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write(modified_content)

        print(f"File processed successfully. Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    filename = input("Enter the filename to read: ")
    read_and_modify_file(filename)
 

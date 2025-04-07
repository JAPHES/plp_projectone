def read_and_modify_file():
    # Ask the user for the input filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Example modification: Convert all text to uppercase
        modified_content = content.upper()

        # Define the name of the output file
        output_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Run the function
read_and_modify_file()

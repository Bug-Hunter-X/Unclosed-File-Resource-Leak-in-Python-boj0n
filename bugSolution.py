def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write("This is some sample text")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
function_with_closed_file('my_file.txt') # The file is always closed, even if there is an exception.
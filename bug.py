def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    f.close() #this line might not be reached if an exception is raised

# Example usage:
try:
    function_with_unclosed_file('my_file.txt')
except Exception as e:
    print(f"An error occurred: {e}")
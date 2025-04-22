import math

def read_file_to_array(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()  # Read all lines into a list
        
        # Convert each line to an integer after stripping newline characters
        data = [float(line.strip()) for line in data]
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    

def write_sum_to_file(sum, output_filename):
    try:
        with open(output_filename, 'a') as file:
            file.write(str(sum) + "\n")  # Ensures a new line after each entry
    except IOError:
        print(f"Error: Could not write to {output_filename}.")

    

# Example usage
filename = "data.txt"
values = read_file_to_array(filename)

sum=0

for i in values:
    radius = ((1/math.pi)*i)**0.5
    volume = (4/3)*(math.pi)*(radius**3)
    sum=sum+volume

write_sum_to_file(sum,"vol.txt")





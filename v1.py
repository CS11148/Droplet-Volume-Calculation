def sum_volumes(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            values = [float(line.strip()) for line in file if line.strip()]
        total_volume = sum(values)

        with open(output_file, "w") as file:
            file.write(str(total_volume) + "\n")

        print(f"Sum of volumes: {total_volume} (saved to {output_file})")
    except (IOError, ValueError) as e:
        print(f"Error: {e}")

# Example usage
sum_volumes("vol.txt", "droplet_volume.txt")

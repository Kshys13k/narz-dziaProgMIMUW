import os
import csv


def sum_computation_times(root_dir):
    total_time = 0

    #walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:

            if filename == 'Solutions.csv':
                file_path = os.path.join(dirpath, filename)

                # read csv
                with open(file_path, mode='r') as file:
                    reader = csv.reader(file, delimiter=';')
                    next(reader)  # Skip the header row

                    for row in reader:
                        model, output_value, time_of_computation = row
                        if model.strip() == 'A':
                            # Remove the 's' from the time
                            time_of_computation = int(time_of_computation.strip().replace('s', ''))
                            total_time += time_of_computation

    return total_time



current_directory = os.getcwd()
root_directory = os.path.join(current_directory, 'week_folders')

# Calculate the total time of computation for model A
total_computation_time = sum_computation_times(root_directory)
print(f"Total time of computation for model A: {total_computation_time}s")

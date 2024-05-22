import os
import random
import csv


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
parts_of_day = ["morning", "evening"]

#create main folder
root_path = "./week_folders"
os.makedirs(root_path, exist_ok=True)

for day in days:
    #create a folder for each day
    day_path = os.path.join(root_path, day)
    os.makedirs(day_path, exist_ok=True)

    for part in parts_of_day:
        # create a morning, evenings folders
        subfolder_path = os.path.join(day_path, part)
        os.makedirs(subfolder_path, exist_ok=True)

        #create csv file
        csv_file_path = os.path.join(subfolder_path, 'Solutions.csv')

        model = random.choice(['A', 'B', 'C'])
        output_value = random.randint(0, 1000)
        time_of_computation = f"{random.randint(0, 1000)}s"

        with open(csv_file_path, mode='w') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Model', 'Output value', 'Time of computation'])
            writer.writerow([model, output_value, time_of_computation])

print("Folders and files have been created successfully.")
import os
import csv

# Set the path to the directory containing the captcha images
captcha_dir = 'facebook_captcha_labels'

# Initialize an empty list to store the file names and titles
captcha_files = []

# Iterate over the files in the captcha directory
index = 0
for filename in os.listdir(captcha_dir):
    # Get the full path to the file
    filepath = os.path.join(captcha_dir, filename)
    # Check if the file is an image
    if os.path.isfile(filepath) and filename.endswith('.png'):
        # Add the file name and title to the list
        captcha_files.append([filename.split(',')[0], index])
        index += 1

# Write the file names and titles to a CSV file
with open('captcha_files.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Filename', 'Title'])
    # Write the data rows
    writer.writerows(captcha_files)
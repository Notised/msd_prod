import os
import csv
import json


def search_directories_for_files(root_dir, search_dir_names):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['BU', 'Journey Name', 'Audience Name', 'Created', 'Last Modified', 'Status'])
        for dir_name, subdir_list, file_list in os.walk(root_dir):
            for search_dir_name in search_dir_names:
                if search_dir_name in subdir_list:
                    subdir_list.remove(search_dir_name)  # Exclude the search directory from further traversal
                    file_dir = os.path.basename(dir_name)
                    search_in_folder(os.path.join(dir_name, search_dir_name), file_dir, writer)


def search_in_folder(folder_path, file_dir, writer):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as f:
                json_data = json.load(f)
                if 'triggers' in json_data:
                    for trigger in json_data['triggers']:
                        if 'audienceType' in trigger['metaData'] and trigger['metaData']['audienceType'] == 'GA360':
                            name = json_data.get('name')
                            if name:
                                writer.writerow([file_dir, name, trigger['metaData']['audienceName'],json_data['createdDate'], json_data['modifiedDate'], json_data['status']])


# Example usage:

root_directory = '/home/andrew/Documents/sfmc/msd_prod/prod/retrieve/msd_prod'

search_directory_names = ['journey']


search_directories_for_files(root_directory, search_directory_names)

import os
import requests

def function_to_run(file_path):

    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': '7e8fafe4fd10f5fb30305cf8eea438904a643b31d90ea851f7f1eefa3deea6e5'}
    files = {'file': (file_path, open(file_path, 'rb'))}

    response = requests.post(url, files=files, params=params)
    res = response.json()['response_code']
    return res

def traverse_directory(directory):
    for entry in os.listdir(directory):
        entry_path = os.path.join(directory, entry)
        if os.path.isfile(entry_path):
            res = function_to_run(entry_path)
            if res != 0:
                return True
        elif os.path.isdir(entry_path):
            if traverse_directory(entry_path):
                return True
    return False


if __name__ == "__main__":
    # folder_path = input("Enter the folder address: ").strip('"')
    folder_path = r"C:\Users\mika\OneDrive\מסמכים" #example path
    folder_path = os.fsdecode(folder_path)
    clear_from_virus = traverse_directory(folder_path)
    if clear_from_virus:
        print("This path is clear from viruses")
    else:
        print("Virus detected")

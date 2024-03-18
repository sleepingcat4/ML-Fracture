import os
import zipfile

def json_files():
    json_files = [file for file in os.listdir() if file.endswith('.json')]
    
    if json_files:
        with zipfile.ZipFile('json_files.zip', 'w') as zip_file:
            for json_file in json_files:
                zip_file.write(json_file)
        
        print("JSON files zipped successfully.")
    else:
        print("No JSON files found in the working directory.")

json_files()

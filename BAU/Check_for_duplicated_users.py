import json
import os
import glob
import pandas as pd

folder = r"D:\_Lab\Git\LAB-1\JSON"

json_files = glob.glob(os.path.join(folder, "*.json"))

all_frames = []

for file in json_files:
    print(f"Processing: {os.path.basename(file)}")
    
    with open(file, 'r') as f:
        data = json.load(f)

    if 'assignments' in data:
        temp_df = pd.DataFrame(data['assignments'])
        temp_df['Source_File'] = os.path.basename(file)
        all_frames.append(temp_df)
    else:
        print(f"Skipping {file}: No 'assignments' key found.")

if all_frames:
    master_df = pd.concat(all_frames, ignore_index=True)

    master_df = master_df.explode('user-or-group')

    print("\n--- MASTER AUDIT TABLE ---")
    print(type(master_df))

else:
    print("No valid JSON data found.")

duplicate_mask = master_df.duplicated(subset=['object', 'user-or-group'], keep=False)
all_duplicates = master_df[duplicate_mask]

print(all_duplicates.sort_values(by=['object', 'user-or-group']))

print(dir(master_df))
master_df.explo
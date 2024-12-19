import json
import csv
import os

# Directory containing the JSON files
input_directory = "/home/abi/PycharmProjects/NLP_DS/"
output_file = "all_st_vincent_lyrics_solo_lps.csv"

# Initialize an empty list to store all lyrics
all_lyrics_data = []

# Loop through all JSON files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".json"):  # Process only JSON files
        file_path = os.path.join(input_directory, filename)

        # Load the JSON data
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                # Extract tracks
                songs = data.get("tracks", [])
                for track in songs:
                    song = track.get("song", {})
                    title = song.get("title", "Unknown Title")
                    lyrics = song.get("lyrics", "Lyrics not available")
                    all_lyrics_data.append({"Title": title, "Lyrics": lyrics, "Source File": filename})
            except json.JSONDecodeError:
                print(f"Could not decode {filename}, skipping.")

# Save all data to a single CSV
with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Title", "Lyrics", "Source File"])
    writer.writeheader()
    writer.writerows(all_lyrics_data)

print(f"All lyrics saved to {output_file}")

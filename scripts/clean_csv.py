import re
import csv
import os

# Input CSV file (generated previously)
input_file = "all_st_vincent_lyrics_solo_lps.csv"

# Output CSV file for cleaned data
output_file = "all_st_vincent_lyrics_cleaned_solo_lps.csv"

# Read the input CSV, clean only the "Lyrics" column, and write to a new file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames  # Preserve original column names
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    # Write the header row to the output file
    writer.writeheader()

    # Process each row
    for row in reader:
        # Clean the "Lyrics" column
        lyrics = row.get("Lyrics", "")

        # Remove text in parentheses or brackets (e.g., [Chorus], (Verse 1))
        cleaned_lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)

        # Remove empty lines
        cleaned_lyrics = os.linesep.join([s for s in cleaned_lyrics.splitlines() if s.strip()])

        # Update the row with cleaned lyrics
        row["Lyrics"] = cleaned_lyrics

        # Write the cleaned row to the output file
        writer.writerow(row)

print(f"Cleaned lyrics saved to {output_file}")

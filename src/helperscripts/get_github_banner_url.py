import os

# Define the local folder path and GitHub URL base
local_folder_path = "/Users/suhail/Library/CloudStorage/Dropbox/matrix/packages/notionUtils/assets/media/banner/"
github_base_url = "https://github.com/suhailphotos/notionUtils/blob/main/assets/media/banner/"

# Get the list of files in the folder
files = [f for f in os.listdir(local_folder_path) if os.path.isfile(os.path.join(local_folder_path, f))]

# Generate the SQL statement with indentation and remove file extensions from cover_name
values = []
for file in files:
    cover_name = os.path.splitext(file)[0]  # Remove the file extension
    cover_url = f"{github_base_url}{file}?raw=true"
    values.append(f"    ('{cover_name}', '{cover_url}', NOW(), NOW())")

sql = (
    "INSERT INTO cover_pages (cover_name, cover_url, created_at, updated_at)\n"
    "VALUES\n"
    + ",\n".join(values)
    + ";\n"
)

# Save the SQL statement to a file or print it
with open("insert_cover_pages_readable.sql", "w") as f:
    f.write(sql)

print("SQL script generated: insert_cover_pages_readable.sql")

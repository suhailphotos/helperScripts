import os
import shutil

# Define the base path for the matrix directory
base_path = "/home/suhail/Dropbox/matrix"

# Define the paths for the new directories
config_path = os.path.join(base_path, "config")
backups_path = os.path.join(config_path, "backups")
credentials_path = os.path.join(config_path, "credentials")
settings_path = os.path.join(config_path, "settings")

# List of credentials and settings files with their current location in config folder
credentials_files = [
    "client_secrets.json",
    "github.txt",
    "googledrive.txt",
    "PyPI-Recovery-Codes-suhailphotos-2024-08-02T00_21_08.140030.txt",
    "PyPiToken.txt"
]
settings_files = [
    "config.ini"
]

# Create necessary directories if they don't exist
os.makedirs(backups_path, exist_ok=True)
os.makedirs(credentials_path, exist_ok=True)
os.makedirs(settings_path, exist_ok=True)

# Move credentials files to the credentials folder
for file_name in credentials_files:
    src = os.path.join(config_path, file_name)
    dest = os.path.join(credentials_path, file_name)
    if os.path.exists(src):
        shutil.move(src, dest)
        print(f"Moved {file_name} to {credentials_path}")

# Move settings files to the settings folder
for file_name in settings_files:
    src = os.path.join(config_path, file_name)
    dest = os.path.join(settings_path, file_name)
    if os.path.exists(src):
        shutil.move(src, dest)
        print(f"Moved {file_name} to {settings_path}")

print("Folder structure created and files moved successfully.")

import os

def create_folder_structure(base_path):
    # Define the folder structure
    structure = {
        "ml": {
            "cfg": {},  # Configuration files for machine learning
            "data": {
                "raw": {},  # Raw data
                "proc": {}  # Processed data
            },
            "envs": {},  # Conda environment files
            "exps": {},  # Experiments and configurations
            "models": {},  # Trained models and checkpoints
            "nb": {},  # Jupyter notebooks
            "scripts": {},  # ML-specific scripts
            "src": {},  # Source code for ML modules
        },
        "tools": {
            "bash": {},  # Bash scripts for system tasks
            "python": {}  # Python scripts for system tasks
        }
    }

    # Function to create directories recursively
    def create_dirs(path, structure):
        for folder, subfolders in structure.items():
            new_path = os.path.join(path, folder)
            os.makedirs(new_path, exist_ok=True)
            create_dirs(new_path, subfolders)
    
    # Create the base folder structure
    create_dirs(base_path, structure)

def create_readme(base_path):
    readme_path = os.path.join(base_path, "README.md")
    content = """
# Matrix Folder Structure

This document describes the folder structure of the `matrix` directory.

## Top-Level Folders

- **assets/**: Contains various assets like banners, icons, and images.
- **backups/**: Stores backup files.
- **config/**: Configuration files for different projects or setups.
- **data/**: General datasets that are not specific to machine learning.
- **packages/**: Reusable modules and libraries organized into subfolders.

## ML-Specific Folders

- **ml/**: Main directory for machine learning projects and files.
  - **cfg/**: Configuration files for machine learning models and experiments.
  - **data/**: Datasets used for machine learning projects.
    - **raw/**: Raw, unprocessed data files.
    - **proc/**: Processed data files ready for use in modeling.
  - **envs/**: Conda environment files for different ML setups.
  - **exps/**: Experiment scripts, configurations, and results.
  - **models/**: Trained models, checkpoints, and related files.
  - **nb/**: Jupyter notebooks for exploratory data analysis and model development.
  - **scripts/**: Scripts for data processing, training, and model evaluation.
  - **src/**: Source code for reusable machine learning modules and functions.

## Tools for System Maintenance

- **tools/**: Contains scripts and tools for system maintenance.
  - **bash/**: Bash scripts for various system tasks like managing environment variables and file operations.
  - **python/**: Python scripts for system maintenance and CLI tools.
    """
    
    # Write the README content to the file
    with open(readme_path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    # Get the base directory from the MATRIX environment variable
    base_dir = os.getenv("MATRIX")

    if base_dir:
        create_folder_structure(base_dir)
        create_readme(base_dir)
        print(f"Folder structure created and README.md file added at {base_dir}.")
    else:
        print("MATRIX environment variable is not set. Please set it before running this script.")

from pathlib import Path
import shutil
import kagglehub

# Download the Kaggle dataset
dataset_path = Path(
    kagglehub.dataset_download(
        "yudhaislamisulistya/plants-type-datasets"
    )
)

# Original dataset location
source_dir = dataset_path / "split_ttv_dataset_type_of_plants"

# Final output folder
output_dir = Path.home() / "Downloads" / "plants_dataset"
output_dir.mkdir(parents=True, exist_ok=True)

split_folders = [
    "Train_Set_Folder",
    "Validation_Set_Folder",
    "Test_Set_Folder"
]

for split in split_folders:
    split_path = source_dir / split

    for class_folder in split_path.iterdir():

        if class_folder.is_dir():

            # Example: plant_dataset/banana
            destination_class = output_dir / class_folder.name
            destination_class.mkdir(parents=True, exist_ok=True)

            for image_path in class_folder.iterdir():

                if image_path.is_file():

                    destination = destination_class / image_path.name

                    # Prevent overwriting if two files have the same name
                    if destination.exists():
                        destination = (
                            destination_class
                            / f"{split}_{image_path.name}"
                        )

                    shutil.copy2(image_path, destination)

print("Dataset reorganised successfully.")
print(f"Saved to: {output_dir}")
import imgaug as ia
import imgaug.augmenters as iaa
import imageio
import os

def remove_svg_from_all_filenames(root_folder):
    """Recursively removes '.svg' from image filenames in a folder and its subfolders."""
    for dirpath, _, filenames in os.walk(root_folder):  # Walk through all directories
        for filename in filenames:
            if filename.endswith((".jpg", ".jpeg", ".png", ".gif", ".svg")):
                new_name = filename.replace("px-Vietnam_road_sign_", "")
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

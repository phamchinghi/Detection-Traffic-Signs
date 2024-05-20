from per.dataaccess import Crawling
from per.dataaccess import Creating
import os


if __name__ == '__main__':
    # url = "https://en.wikipedia.org/wiki/Road_signs_in_Vietnam"
    # Crawling.download_images(url)

    root_folder = "dataset/VN"  # Replace with the path to your main folder
    Creating.remove_svg_from_all_filenames(root_folder)

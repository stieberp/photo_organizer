import os
import shutil
from pathlib import Path

import click
from PIL import Image, ExifTags


def get_date(path):
    with Image.open(path) as image:
        img_exif = image.getexif()
        if img_exif:
            for key, val in img_exif.items():
                if key in ExifTags.TAGS:
                    if "DateTimeOriginal" == ExifTags.TAGS[key]:
                        result = val.split(" ")[0]
                        split = result.split(":")
                        result = f"{split[0]}-{split[1]}"
                        return result


def orgainze_photos(dir):
    # only tested to work with jpg for now
    # photo_extensions = ['jpg', 'gif', 'png', 'bmp', 'JPG']
    photo_extensions = ["jpg", "JPG"]
    ls = os.listdir(dir)

    for item in ls:
        path = f"{dir}\\{item}"
        if os.path.isfile(path):
            photo = list(filter(path.endswith, photo_extensions)) != []
            if photo:
                # if item.split('.')[1] in photo_extensions:
                date = get_date(path)
                if date:
                    dest_dir = f"{dir}\\{date}"
                else:
                    dest_dir = f"{dir}\\no_date"

                # get or create directory
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                # move file
                split = path.split("\\")
                dest_path = f"{dest_dir}\\{split[len(split) - 1]}"
                shutil.move(path, dest_path)


@click.command()
@click.option(
    "-d",
    "--directory",
    prompt="photo directory",
    help="photo directory",
)
def main(directory):
    orgainze_photos(Path(directory))


if __name__ == "__main__":
    main()
    # orgainze_photos(Path('C:/path/to/photos'))

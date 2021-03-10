import os
import shutil

from PIL import Image, ExifTags

PHOTO_DIRECTORY = ''


def get_date(path):
    img = Image.open(path)
    img_exif = img.getexif()
    if img_exif:
        for key, val in img_exif.items():
            if key in ExifTags.TAGS:
                if 'DateTimeOriginal' == ExifTags.TAGS[key]:
                    result = val.split(' ')[0]
                    split = result.split(':')
                    result = f'{split[0]}-{split[1]}'
                    return result


def orgainze_photos(dir):
    photo_extensions = ['jpg', 'gif', 'png', 'bmp', 'JPG']
    ls = os.listdir(dir)

    for item in ls:
        path = f'{dir}\\{item}'
        if os.path.isfile(path):
            photo = list(filter(path.endswith, photo_extensions)) != []
            if photo:
                # if item.split('.')[1] in photo_extensions:
                date = get_date(path)
                if date:

                    dest_dir = f'{dir}\\{date}'
                else:
                    dest_dir = f'{dir}\\no_date'

                # get or create directory
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                # move file
                split = path.split('\\')
                dest_path = f'{dest_dir}\\{split[len(split) - 1]}'
                shutil.move(path, dest_path)


if __name__ == '__main__':
    orgainze_photos()

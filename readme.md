# Photo Organizer

A quick and dirty script to organize photos by year and month.
This script looks at the photo's metadata to get the date, and 
will put photos into directories named like YYYY-MM. 
If the photo doesn't have a metadata date, it will be placed in a 'no_date' directory.

## Developer Setup Instructions

This project requires Python 3.9  

1. Create and activate a virtual environment.

1. Install project dependencies.
    ```commandline
    pip install -r requirements.txt
    ```
1. Build the executable.
   ```commandline
    pyinstaller --onefile main.py --name photo_organizer
    ```

##Instructions
- Move all of your photos in one directory  
  this script doesn't look in subdirectories
- Setup a virtual environment
- Install the requirements
- run the executable from the command line  
  ```
  photo_organizer.exe -d C:/photos
  ```


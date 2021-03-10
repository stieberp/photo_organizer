###A quick and dirty script to organize photos by year and month.
This script looks at the photo's metadata to get the date, and 
will put photos into directories named like YYYY-MM. 
If the photo doesn't have a metadata date, it will be placed in a 'no_date' directory.

###Instructions
- Move all of your photos in one directory  
  this script doesn't look in subdirectories
- Setup a virtual environment
- Install the requirements
- Set PHOTO_DIRECTORY in the script
- Run main.py

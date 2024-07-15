"""
Remember we want the final video to be in chronological order of when those images
were captured or created or shared. So the following holds a lot of emphasis.

The crucial reason behind creating this file is that, even though images coming
from Google Drive has a metadata attribute 'createdTime', it seems to be not
accurate and reliable on when it was uploaded or edited by a device, hence relying
on that metadata alone isn't going to work.

So we are going to extract dates from the file names itself and then compare it with
'createdTime' metadata and choose the earliest date&time among those two.

# Known patterns to dissect

    1. 2016-05-07-23-26-37-161_1462861145654.jpg
    2. 20140702_193810.jpg, *
       20150105_205630 (1).jpg
    3. 20150125_025739_20150126143255133.jpg
    4. B612_20151228_132423.jpg *
    5. Screenshot_2023-04-05-17-48-02-94_40deb401b9ffe8e1df2f1cc5ba480b12
       Screenshot_2021-03-21-01-27-51-81 * 
    6. IMG-20200601-WA0030 *
       IMG_20160218_212803.jpg *
    7. collage_20141221154525979_20141221154619994.jpg
       collage_20141221154525979.jpg

These might not cover all of the patterns but, these were extracted manually by going 
through images as a starting point.

At first, we will use general methods like dateutil.parser which can help
extract dates from most common formats. And then we will use regex to
extract dates from other filenames.

* - handled by dateutil.parser
"""

import re
from datetime import datetime
from dateutil import parser
from typing import Optional

def get_actual_createdTime(file:str) -> str:
    """
    Determines the actual creation time of a file based on its metadata.

    Args:
    - file (dict): Dictionary containing metadata of the file including 
    'createdTime' and 'name'.

    Returns:
    - datetime: The determined creation time of the file.

    This function attempts to parse the creation time from the file name 
    using date parsing utilities. If parsing fails, it falls back to the 
    provided 'createdTime' metadata from Google Drive. It then compares 
    the parsed date and the 'createdTime' and returns the earlier of the two.

    """

    # Initialize variables
    utils_date = None
    extracted_utils_date = None
    
    # Get the truncated creation time without timezone info
    created_time = file["createdTime"][:-5]
    modified_time = file["modifiedTime"][:-5]
    
    # Extract file name without extension
    fname = file["name"].split(".")[0]
    
    try:

        # Attempt to parse date from file name
        parsed_date = parser.parse(fname, fuzzy=True)

        # Format parsed date to standard datetime string
        utils_date = parsed_date.strftime("%Y-%m-%dT%H:%M:%S")
        
        # Convert formatted date string to datetime object
        utils_date = datetime.strptime(utils_date, "%Y-%m-%dT%H:%M:%S")

        # dateutil parser has weird problem where it passes numbers such as 
        # 567 and converts it to 0567-07-15 00:00:00 so, since I know my files
        # aren't older than 2014, let's instead use modified time using an if
        # condition
        if utils_date < datetime.strptime("2014-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S"):
            utils_date = datetime.strptime(modified_time, "%Y-%m-%dT%H:%M:%S")

    except Exception as e:

        # If parsing fails, fallback to the provided 'createdTime' from metadata
        utils_date = datetime.strptime(created_time, "%Y-%m-%dT%H:%M:%S")
        
        # Attempt to match and extract date from file name using custom format matching function
        extracted_utils_date = match_dates_format(fname)
        
    else:

        # If parsing succeeds, use the provided 'createdTime' as fallback
        extracted_utils_date = datetime.strptime(created_time, "%Y-%m-%dT%H:%M:%S")
        
    finally:

        # Compare parsed and fallback dates, return the earlier one
        # ":" isn't allowed in file names in windows os
        if extracted_utils_date is None:
            return str(utils_date).replace(":", "_")
        return str(min(utils_date, extracted_utils_date)).replace(":", "_")

def match_dates_format(fname:str) -> Optional[datetime]:
    """
    Extracts date from the filename and returns it in ISO 8601 
    format (YYYY-MM-DDTHH:MM:SS).

    Args:
    - fname (str): The filename to extract the date from.

    Returns:
    - date: The extracted date in ISO 8601 format or None if no date is found.
    """

    # Known patters found in the names of the files
    patterns = [
        r"(20\d{2})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})",
        r"(20\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(?:\d{2,3})",
        r"(20\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(?:\d{2,3})",
        r"(20\d{2})_(\d{2})_(\d{2})_(\d{2})_(\d{2})_(\d{2})_(?:\d{2,3})"
    ]

    # Looping through each pattern
    for pattern in patterns:
        
        # searching for matches
        matches = re.search(pattern, fname)
        
        # if match(es) is found
        if matches:
            # returns datetime object with specific format
            return datetime.strptime("{0}-{1}-{2}T{3}:{4}:{5}".format(
                *matches.groups()), "%Y-%m-%dT%H:%M:%S")

    # else returns None
    return None
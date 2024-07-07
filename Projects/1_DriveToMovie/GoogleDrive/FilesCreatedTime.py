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

(20\d{2}-\d{2}-\d{2})-(\d{2}-\d{2}-\d{2}-\d{2,3})

(20\d{6})_(\d{6})

(20\d{6})(\d{6}\d{2,3})

(20\d{2}_\d{2}_\d{2})_(\d{2}_\d{2}_\d{2}_\d{2,3})
"""


import re
import datetime
from dateutil import parser

def get_actual_createdTime(files):
    
    for file in files:
        utils_date = None
        fname = file["name"].split(".")[0]
        try:
            parsed_date = parser.parse(fname, fuzzy=True)
            utils_date = parsed_date.strftime(r"%Y-%m-%dT%H:%M:%S.%f")
        except OverflowError as e:
            print(f"\nUnable to parse due to {e}.")
        except parser._parser.ParserError as e:
            print(f"\nUnable to parse due to {e}.")
        except Exception as e:
            print(f"\nUnable to parse due to {e}.")
        else:
            re.match()

def main():
    
    files = [{'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1lCeKnYgXKCdsqwrZxSECTSoK6mOkYmwj', 'name': 'Copy of collage_20141221154525979_20141221154619994.jpg', 'createdTime': '2024-07-07T02:28:45.177Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1tiAE-2pxX2AFiFKlLoryzZjcD-cJoLLz', 'name': 'Copy of collage_20141221154525979.jpg', 'createdTime': '2024-07-07T02:28:45.177Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1esN60Zf3a2bCGo6LBIiHfGw8oV64OQVw', 'name': 'Copy of IMG_20160218_212803.jpg', 'createdTime': '2024-07-07T02:28:25.307Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1qTzbLSI7ek6ZrBsNJR-GFRngjzweE9wK', 'name': 'Copy of IMG-20200601-WA0030.jpg', 'createdTime': '2024-07-07T02:28:08.750Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '10H3ugbK-AIdZk8iCAWOf1pS8vXvVqkPH', 'name': 'Copy of Screenshot_2021-03-21-01-27-51-81.jpg', 'createdTime': '2024-07-07T02:27:55.725Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1f4rMBjGgS9EOdsqNENoYDKI3qsVaUBLq', 'name': 'Copy of Screenshot_2023-04-05-17-48-02-94_40deb401b9ffe8e1df2f1cc5ba480b12.jpg', 'createdTime': '2024-07-07T02:27:39.971Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1L_oi5jwm9Jm7DEeJ80rE3udHe42yIm3-', 'name': 'Copy of B612_20151228_132423.jpg', 'createdTime': '2024-07-07T02:27:25.358Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1dQFp9-z8UyBQCQba89g6zSl0feklgwrn', 'name': 'Copy of 20150125_025739_20150126143255133.jpg', 'createdTime': '2024-07-07T02:27:11.335Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1wwMGltoplShKQZNUyRyq8HA4m1ypi_-w', 'name': 'Copy of 2016-05-07-23-26-37-161_1462861145654.jpg', 'createdTime': '2024-07-07T02:26:43.115Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1aab7nnmvqeC_NYxcM0Iq03EpwDt9SxqH', 'name': 'Copy of 20150114_164645 (1).jpg', 'createdTime': '2024-07-07T02:25:50.030Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1Rbv0eUF7dpqPP4slRdUM2HmPoZf-fjPK', 'name': 'Copy of 20140702_193810.jpg', 'createdTime': '2024-07-07T02:25:27.328Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1ZfiGmRd2uCUNZKPo71abpLv03FfxRF2F', 'name': 'Copy of 2019-02-20_11-28-01_UTC', 'createdTime': '2024-07-07T02:25:08.057Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1wG0GFtSrDd1AFYnT7DRoSMGzKBzX2G9t', 'name': 'Copy of 2016-05-07-23-26-37-161_1462861145654.jpg', 'createdTime': '2024-07-07T02:24:58.545Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1TrVXOna0T66hINkRc7omBnFGtYrHkvKG', 'name': 'Copy of 2016-10-31-17-24-57-828_1477922339024.jpg', 'createdTime': '2024-04-09T23:27:45.482Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1WYGVhlq22SmKJeHbt29vjQb1ZWC5Bj39', 'name': 'Copy of 20150429_184516.jpg', 'createdTime': '2024-04-09T23:27:45.482Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1AXwDXMbCargdiWNORlyo2xQ7UUUoUbaV', 'name': 'Copy of .B612_20160305_131718.jpg.raw', 'createdTime': '2024-04-09T23:27:45.482Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1g6euaRsrBoawxX5RYJDY6yx6IWH7svdp', 'name': 'Copy of 20150424_183601.jpg', 'createdTime': '2024-04-09T23:27:45.482Z'}, {'mimeType': 'image/jpeg', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1ieKl4UfQz0bAO8svUY_teKnZsssU97-k', 'name': 'Copy of _20150820_161738.JPG', 'createdTime': '2024-04-09T23:27:45.482Z'}, {'mimeType': 'image/png', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1SPlTgRL8NuUhIfS23UAr59o0jMpRYKs-', 'name': 'carbon (17).png', 'createdTime': '2024-04-10T01:07:31.422Z'}, {'mimeType': 'image/png', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '107lNUITbZAQtf1fsdvo25g1WPaBbgR1l', 'name': 'carbon (14).png', 'createdTime': '2024-04-10T01:07:33.777Z'}, {'mimeType': 'image/png', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1QEu6FhiCQxfa6oQklWpyI0hPZudlYK7t', 'name': 'carbon (11).png', 'createdTime': '2024-04-10T01:07:33.777Z'}, {'mimeType': 'image/heif', 'parents': ['1Cjb5u1lp1X_fYxNNR3tZp1cNFagy3E3t'], 'id': '1NVd48rzywb5j81kKRvlCBQP0E_Ftextk', 'name': '1.HEIC', 'createdTime': '2024-06-28T09:15:57.879Z'}]
    
    print([f['name'] for f in files])

    print(get_actual_createdTime(files))

if __name__ == "__main__":
    main()
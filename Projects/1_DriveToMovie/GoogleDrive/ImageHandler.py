import cv2
from sys import exit
from os import listdir, path, mkdir



def image_modifier(downloading_path):

    # if directory doesn't exist, create
    if not path.exists(downloading_path):
        print(f"==== The directory {downloading_path} doesn't exist. ====")
        print(f"==== Exiting workflow. ====")
        exit()

    root, folder = downloading_path.split("\\")
    mofidied_foler_path = path.join(root, f"modified_{folder.title()}") 
    
    if path.exists(mofidied_foler_path):
        print(f"==== The directory {mofidied_foler_path} already exist. ====")
        print(f"==== Exiting workflow. ====")
        exit()
    else:
        mkdir(mofidied_foler_path)
        

    filesnames = listdir(downloading_path)
    total_files = len(filesnames)
    
    for file in filesnames:
        fname = path.join(downloading_path, file)
        print(image_alteration(fname, total_files))
        break


def image_alteration(fname, total_files, max_h=1080, max_w=1920):

    """
    Alters an image by resizing, padding, and blending it with a grayscale version.

    Args:
        image_path (str): Path to the input image.
        filename (str): The name of the file, used to determine the desaturation ratio.
        max_h (int): Maximum height of the resized image.
        max_w (int): Maximum width of the resized image.
        total_files (int): Total number of files, used to determine the desaturation ratio.

    Returns:
        final_img (numpy.ndarray): The altered image.
    """

    # Final image
    final_img = None
        
    # Annoying Iphone images, OMG!
    if fname.split(".")[1] == "heic":
        # Use pillow-heif extension
        img_t = open_heif(fname, convert_hdr_to_8bit=False, bgr_mode=True)
        img = np.asarray(img_t)
            
    else:
        # Load the image from the file
        img = cv2.imread(fname)

    # Check if the image was loaded successfully
    if img is not None:
            
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            
        # Actual image dimensions
        img_h, img_w = img.shape[:2]

        # Calculate scaling factors for width and height
        scale_width = max_w / img_w
        scale_height = max_h / img_h

        # Determine scaling factor to fit within max_width and max_height
        scale = min(scale_width, scale_height)

        # Calculate new dimensions after scaling
        new_w = int(img_w * scale)
        new_h = int(img_h * scale)

        # Resize the image
        resized_img = cv2.resize(img, (new_w, new_h))

        # Calculate padding
        top = (max_h - new_h) // 2
        bottom = max_h - new_h - top
        left = (max_w - new_w) // 2
        right = max_w - new_w - left

        # Add padding to resized image
        pad_img = cv2.copyMakeBorder(resized_img, top, bottom, left, right, 
                cv2.BORDER_CONSTANT)

        # Calculate the ratio of desaturation based on the number of images
        # From 1 (full color) to 0 (grayscale)
        ratio = (int(fname.split('.')[0])) / total_files  
            
        # Desaturate the image
        d_img = cv2.cvtColor(pad_img, cv2.COLOR_BGR2GRAY)

        # Channels
        cd_img = cv2.merge((d_img, d_img, d_img))
            
        # Blend the original and desaturated image based on the ratio
        final_img = cv2.addWeighted(pad_img, 1 - ratio, cd_img, ratio, 0)

        # Deleting
        del img, resized_img, d_img, cd_img

    else:
        print(f"## Unsupported File -  {filename} ##")

    return final_img


image_modifier(path.join("downloaded_folder", "Test"))
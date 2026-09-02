from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

def load_saved(input_folder,save_folder):
    # Create the folder to save the binarized images if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    # Define the threshold value
    threshold = 128

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png') or filename.endswith('.tiff'):  # Add other extensions if needed
            # Construct full file path
            image_path = os.path.join(input_folder, filename)

            # Open the image and convert to grayscale
            img = Image.open(image_path).convert('L')

            # Extract the image name without extension
            image_name = os.path.splitext(filename)[0]

            # Convert to NumPy array
            img_array = np.array(img)

            # Replace pixel values: 1 -> 0, 2 -> 255
            img_array[img_array == 1] = 255
            img_array[img_array == 3] = 255
            img_array[img_array == 2] = 0
            # Set a threshold for classification, for example, pixels greater than 100 -> 255, others -> 0
            # threshold = 128
            #
            # # Apply the condition for probability image based on threshold
            # img_array[img_array > threshold] = 255
            # img_array[img_array <= threshold] = 0

            # # Apply thresholding to get only 0 and 255 values
            # binary_img_array = np.where(img_array > threshold, 255, 0).astype(np.uint8)

            # Convert back to image
            binary_img = Image.fromarray(img_array)

            # Define the path to save the binary image using the original name
            save_path = os.path.join(save_folder, f'{image_name}.png')

            # Save the image with 0 and 255 pixel values
            binary_img.save(save_path)

            print(f'Binarized image saved at: {save_path}')
        else:
            print(f'Skipped non-image file: {filename}')

def convert_pixels(image_path,save_folder):
    img = Image.open(image_path)

    # Convert to NumPy array
    img_array = np.array(img)

    # Replace pixel values: 1 -> 0, 2 -> 255
    img_array[img_array == 1] = 0
    img_array[img_array == 2] = 255

    # Convert back to image
    binary_img = Image.fromarray(img_array.astype(np.uint8))

    # Save the modified image
    # save_folder = 'Y:/Kabir Hossain/Works Kabir/Python_jupyter/modified_images/'  # Folder to save the modified image
    os.makedirs(save_folder, exist_ok=True)  # Create folder if it doesn't exist

    # Extract the image name without extension
    image_name = os.path.splitext(os.path.basename(image_path))[0]

    # Define the save path and save the image
    save_path = os.path.join(save_folder, f'{image_name}.png')
    binary_img.save(save_path)

def check(file):
    img = Image.open(file)
    # Check the image mode
    img_mode = img.mode

    # Print whether the image is grayscale or not
    if img_mode == 'L':
        print(f'{os.path.basename(file)} is a grayscale image.')
    else:
        print(f'{os.path.basename(file)} is NOT a grayscale image. Mode: {img_mode}')

    # Convert to NumPy array
    img_array = np.array(img)
    # Get unique pixel values
    unique_values = np.unique(img_array)

    # Print the unique pixel values
    print("Unique pixel values in the image:", unique_values)

    # Display the image
    plt.imshow(img)
    plt.axis('off')  # Hide axis
    plt.show()

# Define the folder containing the images
# input_folder = 'Y:/Kabir Hossain/Works Kabir/Python_jupyter/Mask_image/'  # Replace with the path to your folder containing images
# save_folder = 'Y:/Kabir Hossain/Works Kabir/Python_jupyter/Mask_image_binary/'  # Folder where the binarized images will be saved
input_folder = 'C:/WVSU_Documents/Research/Root_Segment_Dr.Reddy/Segmentation/results_New_process_Input/'
save_folder = 'C:/WVSU_Documents/Research/Root_Segment_Dr.Reddy/Segmentation/results_New_process_Input/Process_New_process_Input/'

# image_path="Y:/Kabir Hossain/Works Kabir/Python_jupyter/data/IMG_8819_class.png"
# save_folder="Y:/Kabir Hossain/Works Kabir/Python_jupyter/data/"
# convert_pixels(input_folder, save_folder)

load_saved(input_folder,save_folder)  # this function is the main that process the image
# test='Y:/Kabir Hossain/Works Kabir/Python_jupyter/Mask_imageV2_binary/'
# check(test+'IMG_6306_class.png') # below's function can be used to check whether processed image binary or not
# test='C:/WVSU_Documents/Research/Root_Segment_Dr.Reddy/Segmentation/results_New_process_Input/Process_New_process_Input/'
# check(save_folder+'/8_1.png')

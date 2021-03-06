"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

This function will get best pixel from each inputed image and return the 'ghost' effect image.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    num = (red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2
    color_distance = math.sqrt(num)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_green = 0
    total_blue = 0
    # Sum for rgb
    for i in range(len(pixels)):
        total_red += pixels[i].red
        total_green += pixels[i].green
        total_blue += pixels[i].blue
    # Calculate average of rgb
    red = total_red//len(pixels)
    green = total_green//len(pixels)
    blue = total_blue//len(pixels)
    rgb = [red, green, blue]  # List
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    red = avg[0]
    green = avg[1]
    blue = avg[2]
    minimum = 0
    best_pixel = None
    for i in range(len(pixels)):
        distance = get_pixel_dist(pixels[i], red, green, blue)
        if minimum == 0:
            minimum = distance
            best_pixel = pixels[i]
        else:
            if distance < minimum:
                minimum = distance
                best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    Returns:
        result (image): an new image with ghost effect
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    for x in range(width):
        for y in range(height):
            best_pixel = images[0].get_pixel(x, y)  # Give best_pixel an object
            pixels = []
            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                pixels.append(pixel)
                best_pixel = get_best_pixel(pixels)
            pixel_result = result.get_pixel(x, y)
            pixel_result.red = best_pixel.red
            pixel_result.green = best_pixel.green
            pixel_result.blue = best_pixel.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

## Focal Length Distribution of Photographs

This Python script analyzes the focal length distribution of photographs in a specified folder. The script uses the `exifread` library to extract the focal length information from the EXIF metadata of each JPEG image in the folder. The focal lengths are then plotted in a histogram using the `matplotlib` library.

The script first defines an empty list called `focal_lengths` to store the focal lengths of the photographs. The `get_focal_length` function opens the JPEG file and extracts the focal length information from its EXIF metadata. It then returns the focal length in decimal format.

The `main` function specifies the directory of the photo folder as a string and loops over each file in the directory. It checks if the file is a JPEG image and if so, calls the `get_focal_length` function to extract its focal length and append it to the `focal_lengths` list.

Finally, the `matplotlib` library is used to create a histogram of the focal lengths. The `hist` function plots the histogram and takes the `focal_lengths` list as its input. The `xlim` function sets the lower and upper limits of the x-axis to the minimum and maximum values in `focal_lengths`, respectively. The `xticks` function sets the tick marks on the x-axis to be in increments of 10. The `xlabel`, `ylabel`, and `title` functions set the labels and title of the plot. Finally, the `show` function displays the plot.

The resulting histogram provides a visual representation of the distribution of focal lengths used in the photographs in the specified folder. This can be useful for photographers to understand their common focal lengths and lenses used.

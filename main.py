import exifread
import os
import matplotlib.pyplot as plt

focal_lengths = []

def get_focal_length(filename):
    f = open(filename, 'rb')
    tags = exifread.process_file(f)
    focal = tags['EXIF FocalLength']
    return focal.values[0].num # focal length stored in decimal format

if __name__ == '__main__':
    photo_folder = 'E:\\DCIM\\100CANON'
    for filename in os.listdir(photo_folder):
        if filename.endswith(('.jpg', '.JPG')):
            focal = get_focal_length(os.path.join(photo_folder, filename))
            focal_lengths.append(focal)

    # Plot histogram
    plt.hist(focal_lengths, bins=40)
    plt.xlim(min(focal_lengths), max(focal_lengths))
    plt.xticks(range(min(focal_lengths), max(focal_lengths) + 1, 10))
    plt.xlabel('Focal length (mm)')
    plt.ylabel('Number of photos')
    plt.title('Focal length distribution')
    plt.show()
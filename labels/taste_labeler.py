from os import listdir
import subprocess
from os.path import isfile, join
from PIL import Image
import csv

def seen_images():
    labeled_images = set()
    with open('womensart_labels.csv', 'r') as image_csv:
        reader = csv.reader(image_csv)
        for row in reader:
          labeled_images.add(row[0])
    return labeled_images

def main(labeled_images):
    art_path = '/Users/dydt/workspace/datasets/womensart/'
    image_paths = [f for f in listdir(art_path) if isfile(join(art_path, f))]

    for path in image_paths:
        if path in labeled_images:
            continue
        image_path = f'{art_path}{path}'
        subprocess.run(["imgcat " + image_path], shell=True)
        label = input("Press 1 if you like it; 0 otherwise. ")
        with open('womensart_labels.csv', 'a') as image_csv:
            writer = csv.writer(image_csv)
            writer.writerow([path, label])

if __name__ == '__main__':
    main(seen_images())
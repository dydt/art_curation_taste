from os import listdir
import subprocess
from os.path import join
from PIL import Image
import csv
from random import shuffle

def create_initial_csv():
    womens_path = '/Users/dydt/workspace/datasets/womensart'
    channel_path = '/Users/dydt/workspace/datasets/artpicschannel'

    women_images = [join(womens_path,f) for f in listdir(womens_path)]
    channel_images = [join(channel_path,f) for f in listdir(channel_path)]
    with open('whichchannel_images.csv', 'a') as initial_csv:
        writer = csv.writer(initial_csv)
        for path in women_images:
            writer.writerow([path, 1])
        for path in channel_images:
            writer.writerow([path, 0])

def queued_images():
    done_images = set()
    with open('whichchannel_labels.csv', 'r') as label_csv:
        reader = csv.reader(label_csv)
        for row in reader:
          done_images.add(row[0])

    queued_rows = []
    with open('whichchannel_images.csv', 'r') as path_csv:
        reader = csv.reader(path_csv)
        for row in reader:
            if row[0] not in done_images:
                queued_rows.append([row[0], row[1]])
    shuffle(queued_rows)

    return queued_rows

def main(queued_rows):
    for path, channel in queued_rows:
        subprocess.run(["imgcat " + path], shell=True)
        label = input("Press 1 if it comes from womensart, 0 otherwise. ")
        with open('whichchannel_labels.csv', 'a') as label_csv:
            writer = csv.writer(label_csv)
            writer.writerow([path, channel, label])

if __name__ == '__main__':
    create_initial_csv()
    main(queued_images())
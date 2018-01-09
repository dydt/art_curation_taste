import csv

def womensart_labeled():
    labeled_images = set()
    with open('womensart_labels.csv', 'r') as womensart_csv:
        reader = csv.reader(womensart_csv)
        for row in reader:
          labeled_images.add(row[0])
    return labeled_images

def main(labeled_images):
    with open('whichchannel_labels.csv', 'r') as channel_csv:
        with open('whichchannel_labels_fresh.csv', 'w') as new_channel_csv:
            reader = csv.reader(channel_csv)
            writer = csv.writer(new_channel_csv)
            for row in reader:
                filename = row[0].split('/')[-1]
                if row[0].split('/')[-1] not in labeled_images:
                    writer.writerow(row)

if __name__ == '__main__':
    main(womensart_labeled())
                


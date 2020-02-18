import glob
from classify import MultinomialNB
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import skimage.measure

TRAINING_POSITIVE = 'ID_Images/train/positives/*.jpg'
TRAINING_NEGATIVE = 'ID_Images/test/negatives/*.jpg'
TEST_POSITIVE = 'ID_Images/test/positives/*.jpg'
TEST_NEGATIVE = 'ID_Images/test/negatives/*.jpg'

# How many pixels to grab from the top-right of image.
CROP_WIDTH, CROP_HEIGHT = 200, 150 #(height, width)
RESIZED = (16, 16)


def get_image_data(infile):
    image = Image.open(infile)
    width, height = image.size
    # left upper right lower
    box = width - CROP_WIDTH, 0, width, CROP_HEIGHT
    region = image.crop(box)
    im = np.array(region)
    #im = im.reshape(1,-1)
    #im = skimage.measure.block_reduce(im, (2,2,1), np.max)
    plt.imshow(im)
    plt.show()
    print(im.reshape(-1))
    return im.reshape(-1)


def main():
    watermark = MultinomialNB()
    # Training
    count = 0
    for infile in glob.glob(TRAINING_POSITIVE):
        data = get_image_data(infile)
        watermark.train((data, 'positive'))
        count += 1
        print 'Training', count
    for infile in glob.glob(TRAINING_NEGATIVE):
        data = get_image_data(infile)
        watermark.train((data, 'negative'))
        count += 1
        print 'Training', count
    

    # Testing
    correct, total = 0, 0
    for infile in glob.glob(TEST_POSITIVE):
        data = get_image_data(infile)
        prediction = watermark.classify(data)
        print(prediction)
        if prediction.label == 'positive':
            correct += 1
        total += 1
        print 'Testing ({0} / {1})'.format(correct, total)
    for infile in glob.glob(TEST_NEGATIVE):
        data = get_image_data(infile)
        prediction = watermark.classify(data)
        print(prediction)
        if prediction.label == 'negative':
            correct += 1
        total += 1
        print 'Testing ({0} / {1})'.format(correct, total)
    print 'Got', correct, 'out of', total, 'correct'


if __name__ == '__main__':
    main()
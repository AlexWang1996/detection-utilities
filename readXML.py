#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alex Wang'

import tensorflow as tf
from object_detection.utils import dataset_util
import  xml.etree.cElementTree as et
import os


train_dir_path = "/home/wsf/Desktop/DHL_Project/DHL_Aug_Xmls/train"
train_output_path = "/home/wsf/Desktop/DHL_Project/images_tfrecords/train.tfrecords"
val_dir_path = "/home/wsf/Desktop/DHL_Project/DHL_Aug_Xmls/val"
val_output_path = "/home/wsf/Desktop/DHL_Project/images_tfrecords/val.tfrecords"

image_format = b'jpg'

def readXML(dir_path, output_path):
    dir = os.listdir(dir_path)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer = tf.python_io.TFRecordWriter(output_path)

    for item in dir:
        print(item)
        if item.endswith('.xml'):
            xmins = []
            xmaxs = []
            ymins = []
            ymaxs = []
            classes_text = []
            classes = []

            tree = et.parse(dir_path + '/' + item)
            root = tree.getroot()
            filename = root.find('filename').text + '.jpg'
            filename = filename.encode('utf8')
            path = root.find('path').text
            print(path)
            with tf.gfile.GFile(path , 'rb') as fid:
                encode_jpg = fid.read()
            for _ in root.findall('size'):
                width = _.find('width').text
                height = _.find('height').text
                depth = _.find('depth').text

            for _ in root.findall('object'):
                name = _.find('name').text.encode('utf8')
                bndbox = _.find('bndbox')
                xmin = bndbox.find('xmin').text
                ymin = bndbox.find('ymin').text
                xmax = bndbox.find('xmax').text
                ymax = bndbox.find('ymax').text
                xmins.append(float(xmin)/float(width))
                xmaxs.append(float(xmax)/float(width))
                ymins.append(float(ymin)/float(height))
                ymaxs.append(float(ymax)/float(height))
                classes_text.append(name)

                if name == 'DOX':
                    classes.append(1)
                elif name == 'WPX':
                    classes.append(2)

                tf_example = tf.train.Example(features=tf.train.Features(feature={
                    'image/height': dataset_util.int64_feature(int(height)),
                    'image/width': dataset_util.int64_feature(int(width)),
                    'image/filename': dataset_util.bytes_feature(filename),
                    'image/source_id': dataset_util.bytes_feature(filename),
                    'image/encoded': dataset_util.bytes_feature(encode_jpg),
                    'image/format': dataset_util.bytes_feature(image_format),
                    'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
                    'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
                    'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
                    'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
                    'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
                    'image/object/class/label': dataset_util.int64_list_feature(classes),
                }))
                writer.write(tf_example.SerializeToString())

    writer.close()

if __name__ == '__main__':
    readXML(train_dir_path, train_output_path)
    readXML(val_dir_path, val_output_path)

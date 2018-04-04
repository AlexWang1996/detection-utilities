#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alex Wang'


from sklearn.model_selection import train_test_split
import os
import shutil
import argparse

xmls = []
labels = []

def split_datasets(filepath):
    if(os.path.exists(filepath + 'train')):
        shutil.rmtree(filepath + 'train')
        os.mkdir(filepath + 'train')
    if(os.path.exists(filepath + 'val')):
        shutil.rmtree(filepath + 'val')
        os.mkdir(filepath + 'val')
    for file in os.listdir(filepath):
        if file.endswith('.xml'):
            xmls.append(file)
            labels.append(1)
    train_, test_, _,_ = train_test_split(xmls,labels, test_size=0.2,shuffle=True, random_state=1)
    for item in train_ :
        shutil.copyfile(filepath + item,filepath + 'train' + '/' + item)
    for item in test_ :
        shutil.copyfile(filepath + item,filepath + 'val' + '/' + item )

    print train_




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--filepath',
        type=str,
        default='',
        help='path to .xml files'
     )
    FLAGS, unparsed = parser.parse_known_args()

    split_datasets(FLAGS.filepath)
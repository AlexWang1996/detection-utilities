#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alex Wang'


import os
import argparse

def rename(image_path):
    i = 0
    n = 6
    files = os.listdir(image_path)
    for file in files:
        n = 6 - len(str(i))
        old_name = image_path + file
        new_name = image_path + str(0) * n + str(i) + '.jpg'
        os.rename(old_name, new_name)
        i += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image_path',
        type=str,
        default='',
        help='path to .jpg files'
     )
    FLAGS, unparsed = parser.parse_known_args()
    rename(FLAGS.image_path)
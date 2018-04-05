#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alex Wang'


import os
import xml.etree.cElementTree as et

path = "/home/wsf/Documents/data-xml/val/"


for item in os.listdir(path):
    output_file = open(path + 'val.txt', "a")
    if item.endswith(".xml"):
        tree = et.parse(path + item)
        root = tree.getroot()
        filename = root.find('filename').text
        output_file.write(filename + '\n')

    print(filename)

path = "/home/wsf/Documents/data-xml/train/"

for item in os.listdir(path):
    output_file = open(path + 'train.txt', "a")
    if item.endswith(".xml"):
        tree = et.parse(path + item)
        root = tree.getroot()
        filename = root.find('filename').text
        output_file.write(filename + '\n')

    print(filename)



'''
download the mnist through sklearn

'''
from sklearn.datasets import fetch_mldata
import sys
import os
from os import environ
from os.path import dirname, exists, expanduser, isdir, join, splitext
data_home = environ.get('SCIKIT_LEARN_DATA',join('~', 'scikit_learn_data'))


print(os.path.join(dirname(dirname(__file__)),'example'))
print(data_home)
# mnist = fetch_mldata('MNIST original',data_home="./")

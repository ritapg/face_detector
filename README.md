# Face detector
A face detector implementation of [opencv library](https://pypi.org/project/opencv-python/). 

# Overview
With the check_faces.py when given a a subset of images it will output the number of faces in each image and add a blue rectangle with a description around the identified face.

# Setup
Create a python3 virtualenv::

    python3 -m venv path

Install the libraries in the requirements.txt file::

    pip install -r requirements.txt

To use the check_faces.py add the images you need to check for faces to the data/test folder .
Run  check_faces.py::

    python -m check_faces.py
    
Check for faces in your images!


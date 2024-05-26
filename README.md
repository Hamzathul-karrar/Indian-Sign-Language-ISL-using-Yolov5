
# Real-Time Sign Language Detection Using Gesture Recognition And Natural Language Processing

## Overview

This project aims to develop a comprehensive system for sign language detection and translation by 
leveraging advancements in gesture recognition and natural language processing (NLP) 
technologies. The system integrates the YOLOv5 object detection framework with NLP techniques 
to enable real-time interpretation of sign language gestures and their conversion into understandable 
textual or spoken language. By bridging the communication gap between sign language users and 
non-signers, the system seeks to empower individuals with hearing impairments to express 
themselves more freely and engage with the broader community on a level playing field

## Installation 

1. Clone the repository.
2. Pycharm (Recommended Code Editor).
3. Install requirements.txt in a Python>=3.8.0 environment, including PyTorch>=1.8  (Python 3.10 Recommended).

## Setup

1. cd to the repository.
2. pip install -r requirements.txt

## Usage

1. Run detect_isl for Indian Sign Language.
2. Run detect_isl_with_speech for Indian Sign Language with speech output.
3. Run detect_kannada for Kannada Sign Language.

## Images

Reference images for ISL and KSL are in images folder.</br>
In KSL, Image K1 is ಅ, ... K15 is ಅಃ.</br>

A in ISL:
![A (ISL)](https://github.com/Hamzathul-karrar/Indian-Sign-Language-ISL-using-Yolov5/blob/main/images/Indian%20Signs%20(ISL)/A.jpg?raw=true "A in ISL")
</br>
ಅ in KSL:
![ಅ (KSL)](https://github.com/Hamzathul-karrar/Indian-Sign-Language-ISL-using-Yolov5/blob/main/images/Kannada%20Signs%20(KSL)/K1__MG20240403144719.jpg?raw=true "ಅ in KSL")

## Train Custom Sign Language

Here is the [documentation](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/) on training custom dataset.


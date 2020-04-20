import os

INPUT_DATASET = "F:/Neeraj/breast-cancer-classification/datasets/original"

BASE_PATH = "F:/Neeraj/breast-cancer-classification/datasets/idc"
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1

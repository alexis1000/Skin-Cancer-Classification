# import the necessary packages
import os

# initialize the list of class label names
CLASSES = ["AKIEC", "BCC", "BKL", "DF", "MEL",
	"NV", "VASC"]

# define the minimum learning rate, maximum learning rate, batch size,
# step size, CLR method, and number of epochs
MIN_LR = 1e-6
MAX_LR = 1e-3
BATCH_SIZE = 32
STEP_SIZE = 8
CLR_METHOD = "exp_range"
NUM_EPOCHS = 50


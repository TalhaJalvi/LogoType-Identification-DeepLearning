''' For Ducumentation refer to Model Documentation.docx'''
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

# loading training data
train_datagen = ImageDataGenerator(
        rescale=1./255,

train_generator = train_datagen.        #Transform every pixel from range [0,255] to [o,1] so each pixel treated as same


        #Data preprocessing technique (augmentation technique) in which we produce further data by flipping, 
        #rotating images etc. Fore further reading and examples see: 
        #https://towardsdatascience.com/data-augmentation-techniques-in-python-f216ef5eed69
        shear_range=0.2,
        #Shifts one part of the image like parrallalogram. counterwise range
        zoom_range=0.2,
        #Defining zoom range
        horizontal_flip=True)flow_from_directory(
        'D:\FYPImplementation\DataSet\Training',
        target_size=(64, 64),

        

# The batch size defines the number of samples that will be propagated through the network.
# For instance, let's say you have 1050 training samples and you want to set up a batch_size equal 
# to 100. The algorithm takes the first 100 samples (from 1st to 100th) from the training dataset and 
# trains the network. Next, it takes the second 100 samples (from 101st to 200th) and trains the 
# network again. 
        batch_size=32,
        class_mode='categorical')

# loading testing data
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = train_datagen.flow_from_directory(
        'D:\FYPImplementation\DataSet\Testing',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')


# A model has a life-cycle, and this very simple knowledge provides the backbone for both modeling a dataset and understanding the tf.keras API.

# The five steps in the life-cycle are as follows:

#     Define the model.
#     Compile the model.
#     Fit the model.
#     Evaluate the model.
#     Make predictions.

# initialising sequential model and adding layers to it

#Defining model 
# The sequential model API is the simplest and is the API that I recommend, especially when getting started.
# It is referred to as “sequential” because it involves defining a Sequential class and adding 
# layers to the model one by one in a linear manner, from input to output.

cnn = tf.keras.models.Sequential()
# A convolution multiplies a matrix of pixels with a filter matrix or ‘kernel’ 
# and sums up the multiplication values. Then the convolution slides over to the
# next pixel and repeats the same process until all the image pixels have been covered. 
#Kernal is also called filter, Also kernal size is also called filtersize.

#Stride:
# The filter is moved accross the imageleft to right, top to bottomwith one pixel column change on the 
# horizontal movements, then one pixel row change on the vertical movements.
# The amount of movement between applications of the filter to the input image is reffered to as Stride
# Defualt is (1,1)


cnn.add(tf.keras.layers.Conv2D(filters=100, kernel_size=4, activation='relu', input_shape=[64, 64, 3]))
# The rectified linear activation function or ReLU for short is a piecewise linear function 
# that will output the input directly if it is positive, otherwise, it will output zero. 
# It has become the default activation function for many types of neural networks because
# a model that uses it is easier to train and often achieves better performance.

cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Conv2D(filters=100, kernel_size=4, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Conv2D(filters=100, kernel_size=4, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=4, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(128, activation='relu'))
cnn.add(tf.keras.layers.Dense(64, activation='relu'))
cnn.add(tf.keras.layers.Dense(4, activation='softfax'))

# finally compile and train the cnn
#For binary
#Adam algorithm for updation of weights in algorithm
#A loss function is something that tells us our algorithm cost. An optimization problem should minimize this
# Use this crossentropy loss function when there are two or more label classes. We expect labels to be 
# provided in a one_hot representation. If you want to provide labels as integers, please use
# SparseCategoricalCrossentropy loss. There should be # classes floating point values per feature.
cnn.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

#for multile classes
# cnn.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
cnn.fit(x=train_generator, validation_data=test_generator, epochs=35)


model = cnn
model.save("my_model.h5")
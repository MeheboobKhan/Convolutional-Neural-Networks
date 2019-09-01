#part 1 - Building deep learning model 
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Initialising the CNN
neuralnetwork = Sequential()

#step 1 Convolution
neuralnetwork.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation = 'relu'))

#pooling 
neuralnetwork.add(MaxPooling2D(pool_size = (2,2)))

#flattening
neuralnetwork.add(Flatten())

# Full connection
neuralnetwork.add(Dense(output_dim = 128, activation = 'relu'))
neuralnetwork.add(Dense(output_dim = 1, activation = 'sigmoid'))

#Compiling CNN
neuralnetwork.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#fitiing cnn to images
from keras.preprocessing.image import ImageDataGenerator

train_datagenerator = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagenerator = ImageDataGenerator(rescale=1./255)

training_set = train_datagenerator.flow_from_directory('dataset/training_set',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagenerator.flow_from_directory('dataset/test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

neuralnetwork.fit_generator(training_set,
                         steps_per_epoch=8000,
                         epochs=25,
                         validation_data=test_set,
                         validation_steps=2000)

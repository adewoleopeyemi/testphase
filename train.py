import numpy as np
import  os
from PIL import Image
import tensorflow as tf
from tensorflow.keras improt models
from tensorflow.keras.layers import Dense, Conv2D, Flatten
from tensorflow.keras.applications import VGG16
from tensorflow.keras.optimizers import Adam
import numpy as np




def open_and_preprocess(path_to_file, is_nude=False):
    listing = os.listdir(path=path_to_file)
    imgs = []
    for file in listing:
        try:
            img=Image.open(imgs+file)
            img=img.resize((124, 124))
            img = img.convert('L')
            img = np.array(img, dtype='float16') / 255.
            imgs.append(img)

        except:
            continue
    if is_nude:
        target = np.ones(len(imgs))
    else:
        target = np.zeros(len(imgs))

    return (imgs, target)

def preprocess_single_image(img):
    img = Image.open(img)
    img = img.resize((124, 124))
    image = np.array(img, dtype='float16') / 255.
    if image.shape == (124, 124, 3):
        return image
    else:
        return None


def build_model():
    conv_base=VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=(124, 124, 3)
    )
    model = models.Sequential()
    model.add(conv_base)
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer=Adam(lr=2e-5), loss='binary_crossentropy', metrics=['acc'])
    return model

def train(X, y, epochs, batch_size, validation_split):
    model = build_model()
    model.fit(X, y, epochs=epochs, batch_size=batch_size, validation_split=validation_split, shuffle=True)
    model.save('nudedetectionalgorithm.h5')
    return model

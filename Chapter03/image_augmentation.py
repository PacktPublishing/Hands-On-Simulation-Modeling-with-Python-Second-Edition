from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array 
from keras.preprocessing.image import ImageDataGenerator

image_generation = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        fill_mode='nearest')

source_img = load_img('colosseum.jpg') 
x = img_to_array(source_img)  
x = x.reshape((1,) + x.shape)  


i = 0
for batch in image_generation.flow(x, batch_size=1,
                          save_to_dir='AugImage', save_prefix='new_image', save_format='jpeg'):
    i += 1
    if i > 50:
        break  
        



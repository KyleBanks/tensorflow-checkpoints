import itertools
import os
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

pixels = 224

# Load the datasets 
seed = 1 
shuffle_value = True
validation_split = 0.3
directory = 'file://' + os.path.abspath("./training-images")

def get_dataset(subset):
  return tf.keras.preprocessing.image_dataset_from_directory(
    directory = directory,
    labels='inferred',
    image_size=(pixels, pixels),
    validation_split = validation_split,
    subset = subset,
    seed = seed,
    shuffle = shuffle_value
  )

train_ds = get_dataset('training')
val_ds = get_dataset('validation')

# Split out some test data from the validation set to be kept on the side
val_batches = tf.data.experimental.cardinality(val_ds)
test_ds = val_ds.take((2*val_batches) // 3)
val_ds = val_ds.skip((2*val_batches) // 3)

# Determine the class names (checkpoints) we're training for
class_names = train_ds.class_names
print('Class Names: {}'.format(class_names))
num_classes = len(class_names)

# Define the model
model = tf.keras.Sequential([
  tf.keras.layers.RandomFlip('horizontal'),
  tf.keras.layers.RandomRotation(0.2),
  tf.keras.layers.RandomZoom(0.1),
  tf.keras.layers.Rescaling(1./255, input_shape=(pixels, pixels, 3)),
  tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes)
])

base_learning_rate = 0.0001
model.compile(
  # only using Legacy as I was training on an M1 mac
  optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=base_learning_rate),
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy']
)

# Train over 5 epochs 
initial_epochs = 5
history = model.fit(
  train_ds,
  epochs=initial_epochs,
  validation_data=val_ds
)

# Evaluate predictions on the validation dataset
loss_val, accuracy_val = model.evaluate(val_ds)
print('Validation loss: {:.2f}'.format(loss_val))
print('Validation accuracy: {:.2f}'.format(accuracy_val))

# Evaluate predictions on the test dataset
loss_test, accuracy_test = model.evaluate(test_ds)
print('Test accuracy: {:.2f}'.format(accuracy_test))

# Run some final predictions  
def predict(filename): 
  path = tf.keras.utils.get_file(filename, origin='file://' + os.path.abspath("./test-images/" + filename))

  img = tf.keras.utils.load_img(
      path, target_size=(pixels, pixels)
  )
  img_array = tf.keras.utils.img_to_array(img)
  img_array = tf.expand_dims(img_array, 0) # Create a batch

  predictions = model.predict(img_array)
  score = tf.nn.softmax(predictions[0])

  print('{} belongs to {} with {:.2f}% confidence.'
      .format(filename, class_names[np.argmax(score)], 100 * np.max(score)))

predict('chk_barn.mp4_00001.jpg')
predict('chk_canoe.mp4_00001.jpg')
predict('chk_race.mp4_00001.jpg')
predict('test_screenshot.png')

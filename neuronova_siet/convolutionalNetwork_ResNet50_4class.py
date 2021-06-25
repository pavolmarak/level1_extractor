import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix


classes = {'Arch': 0, 'Left Loop': 1, 'Right Loop': 2, 'Whorl': 3}
class_num = len(classes.keys())

file_folder_arch = '/home/editav/Desktop/FVC2002_Db4_a_b/A/'
file_folder_left_loop = '/home/editav/Desktop/FVC2002_Db4_a_b/LeftLoop/'
file_folder_right_loop = '/home/editav/Desktop/FVC2002_Db4_a_b/RightLoop/'
file_folder_whorl = '/home/editav/Desktop/FVC2002_Db4_a_b/Whorl/'


data_files_arch = [f for f in glob.glob(file_folder_arch + "*.tif")]
data_files_left_loop = [f for f in glob.glob(file_folder_left_loop + "*.tif")]
data_files_right_loop = [f for f in glob.glob(file_folder_right_loop + "*.tif")]
data_files_whorl = [f for f in glob.glob(file_folder_whorl + "*.tif")]

data_arch = []
for i in range(len(data_files_arch)):
    data_arch.append(np.array(Image.open(data_files_arch[i])))

data_left_loop = []
for i in range(len(data_files_left_loop)):
    data_left_loop.append(np.array(Image.open(data_files_left_loop[i])))

data_right_loop = []
for i in range(len(data_files_right_loop)):
    data_right_loop.append(np.array(Image.open(data_files_right_loop[i])))

data_whorl = []
for i in range(len(data_files_whorl)):
    data_whorl.append(np.array(Image.open(data_files_whorl[i])))

data_arch_train = data_arch[:int(len(data_files_arch) * 0.7)]
data_arch_val = data_arch[int(len(data_files_arch) * 0.7): int(len(data_files_arch) * 0.8)]
data_arch_test = data_arch[int(len(data_files_arch) * -0.2):]

data_arch_train_labels = [classes['Arch']] * int(len(data_arch_train))
data_arch_val_labels = [classes['Arch']] * int(len(data_arch_val))
data_arch_test_labels = [classes['Arch']] * int(len(data_arch_test))

data_left_loop_train = data_left_loop[:int(len(data_files_left_loop) * 0.7)]
data_left_loop_val = data_left_loop[int(len(data_files_left_loop) * 0.7): int(len(data_files_left_loop) * 0.8)]
data_left_loop_test = data_left_loop[int(len(data_files_left_loop) * -0.2):]

data_left_loop_train_labels = [classes['Left Loop']] * int(len(data_left_loop_train))
data_left_loop_val_labels = [classes['Left Loop']] * int(len(data_left_loop_val))
data_left_loop_test_labels = [classes['Left Loop']] * int(len(data_left_loop_test))

data_right_loop_train = data_right_loop[:int(len(data_files_right_loop) * 0.7)]
data_right_loop_val = data_right_loop[int(len(data_files_right_loop) * 0.7): int(len(data_files_right_loop) * 0.8)]
data_right_loop_test = data_right_loop[int(len(data_files_right_loop) * -0.2):]

data_right_loop_train_labels = [classes['Right Loop']] * int(len(data_right_loop_train))
data_right_loop_val_labels = [classes['Right Loop']] * int(len(data_right_loop_val))
data_right_loop_test_labels = [classes['Right Loop']] * int(len(data_right_loop_test))


data_whorl_train = data_whorl[:int(len(data_files_whorl) * 0.7)]
data_whorl_val = data_whorl[int(len(data_files_whorl) * 0.7): int(len(data_files_whorl) * 0.8)]
data_whorl_test = data_whorl[int(len(data_files_whorl) * -0.2):]

data_whorl_train_labels = [classes['Whorl']] * int(len(data_whorl_train))
data_whorl_val_labels = [classes['Whorl']] * int(len(data_whorl_val))
data_whorl_test_labels = [classes['Whorl']] * int(len(data_whorl_test))

train_images = np.concatenate(
    (data_arch_train, data_left_loop_train, data_right_loop_train, data_whorl_train), axis=0)
test_images = np.concatenate(
    (data_arch_test, data_left_loop_test, data_right_loop_test, data_whorl_test), axis=0)
val_image = np.concatenate(
    (data_arch_val, data_left_loop_val, data_right_loop_val, data_whorl_val), axis=0)

train_labels = np.concatenate((data_arch_train_labels, data_left_loop_train_labels, data_right_loop_train_labels, data_whorl_train_labels), axis=0)
test_labels = np.concatenate((data_arch_test_labels, data_left_loop_test_labels, data_right_loop_test_labels, data_whorl_test_labels), axis=0)
val_labels = np.concatenate((data_arch_val_labels, data_left_loop_val_labels, data_right_loop_val_labels, data_whorl_val_labels), axis=0)

class_names = ['Arch', 'Left Loop', 'Right Loop', 'Whorl']

print(train_images.shape)
print(test_images.shape)
print(val_image.shape)


train_mean = np.mean(train_images)
train_std = np.std(train_images)

train_images = (train_images - train_mean) / train_std
val_image = (val_image - train_mean) / train_std
test_images = (test_images - train_mean) / train_std


model_resnet = tf.keras.applications.ResNet50(False, None, None, (384, 288, 1), 'avg', None)

model = keras.Sequential([model_resnet, keras.layers.Dense(4, 'softmax')])


early_stop = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    min_delta=0,
    patience=10,
    mode="min",
    restore_best_weights=True)

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

model.fit(train_images, train_labels,
          epochs=60,
          batch_size=10,
          validation_data=(val_image, val_labels),
          callbacks=[early_stop],
          class_weight={0: 9, 
                        1: len(train_labels)/len(data_left_loop_train_labels),
			2: len(train_labels)/len(data_right_loop_train_labels),
			3: len(train_labels)/len(data_whorl_train_labels)})

model.save('/home/editav/Desktop/model.h5')

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

predictions = model.predict(test_images)

print("Predictions shape: ")
print(predictions.shape)

print(predictions[0])
print(np.argmax(predictions[0]))
print(test_labels[0])




img = test_images[1]


img = (np.expand_dims(img, 0))


predictions_single = model.predict(img)

image_predictions = []
image_predict = []
for i in range(len(test_images)):
    image_predict.append(model.predict(np.expand_dims(test_images[i], 0)))
    image_predictions.append(np.argmax(model.predict(np.expand_dims(test_images[i], 0))))

conf = []
conf = confusion_matrix(test_labels, image_predictions)
print(conf)

#print(predictions_single)
#print(np.argmax(predictions_single[0]))
#print(image_predictions)

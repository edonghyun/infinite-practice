import matplotlib.pyplot as plt
import tensorflow as tf
import gzip
import pickle
import numpy as np

with gzip.open('mnist.pkl.gz', 'rb') as f:
    data = pickle.load(f, encoding='bytes')

(x_train, y_train), (x_test, y_test) = data

x_train, x_test = x_train/255.0, x_test/255.0
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'],
)
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=0)

predictions = model.predict(x_test, batch_size=128)
loss_list = []
for index, ground_truth_label in enumerate(y_test):
    prediction = np.argmax(predictions[index])
    if ground_truth_label != prediction:
        loss_list.append({
            'ground_truth_label': ground_truth_label,
            'prediction': prediction,
            'index': index,
        })

plt.figure(figsize=(9, 9))
for index, loss in enumerate(loss_list):
    if index > 48:
        break

    plt.subplot(7, 7, index+1, xticks=[], yticks=[])
    plt.imshow(x_train[index], cmap='Greys')
    plt.text(0, 16, str(loss['ground_truth_label']), color='green')
    plt.text(0, 24, str(loss['prediction']), color='red')
    plt.xlabel(str(loss['index']))

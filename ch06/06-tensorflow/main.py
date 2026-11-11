import tensorflow as tf

print("TensorFlow", tf.__version__)
print("GPUs:", tf.config.list_physical_devices("GPU"))

# A tiny model, trained for one epoch on random data
x = tf.random.normal((256, 4))
y = tf.reduce_sum(x, axis=1, keepdims=True)
model = tf.keras.Sequential([tf.keras.Input(shape=(4,)), tf.keras.layers.Dense(1)])
model.compile(optimizer="adam", loss="mse")
history = model.fit(x, y, epochs=1, verbose=0)
print("Loss after one epoch:", round(history.history["loss"][0], 3))

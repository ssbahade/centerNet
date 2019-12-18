def br_pooling(x):
  left, top = tf.shape(x)[-3], tf.shape(x)[-2]

  t1 = tf.keras.layers.ZeroPadding2D(((0,0), (left-1,0)))(x)
  t1 = tf.keras.layers.MaxPool2D((1, left), 1)(t1)
  
  #NON-CASCADE
  t2 = tf.image.rot90(x, 2)
  t2 = tf.keras.layers.ZeroPadding2D(((0,top-1), (0,0)))(t2)
  t2 = tf.keras.layers.MaxPool2D((top, 1), 1)(t2)
  t2 = tf.image.rot90(t2, 2)
  
  return t1 + t2

def tl_pooling(x):
  x_ = conv_module(x)
  right, bottom = tf.shape(x_)[-3], tf.shape(x_)[-2]

  t1 = tf.keras.layers.ZeroPadding2D(((0,0), (0,right-1)))(x_)
  t1 = tf.keras.layers.MaxPool2D((1, right), 1)(t1)
  
  #NON-CASCADE
  x_ = conv_module(x)
  t2 = tf.keras.layers.ZeroPadding2D(((0, bottom-1), (0,0)))(x_)
  t2 = tf.keras.layers.MaxPool2D((bottom, 1), 1)(t2)
  
  return t1 + t2

def conv_module(x, f=32, size=(3,3)):
  t = tf.keras.layers.Conv2D(f, size, padding="same")(x)
  t = tf.keras.layers.BatchNormalization()(t)
  t = tf.keras.layers.ReLU()(t)
  
  return t

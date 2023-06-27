from keras.models import Sequential
from keras.layers import Dense, Lambda
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import seaborn as sns
import pandas as pd
np.random.seed(0)

model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(3,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  
# this is so i get an whole number as output (0-9) the same as the difficulty i set
model.add(Lambda(lambda x: x * 9))  

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

X_train = np.random.randint(1, high=101, size=(1000, 1))
X_train = np.hstack((X_train, np.random.randint(1, high=21, size=(1000, 1))))
X_train = np.hstack((X_train, np.random.randint(1, high=13, size=(1000, 1))))
y_train = (X_train[:, 0] / 10) - (X_train[:, 1] * 2) + (X_train[:, 2] * 3)
y_train = y_train / 9  

history = model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)

X_test = np.random.randint(1, high=101, size=(100, 1))
X_test = np.hstack((X_test, np.random.randint(1, high=21, size=(100, 1))))
X_test = np.hstack((X_test, np.random.randint(1, high=13, size=(100, 1))))
y_test = (X_test[:, 0] / 10) - (X_test[:, 1] * 2) + (X_test[:, 2] * 3)
y_test = y_test / 9  

y_pred = model.predict(X_test)

print(y_pred[:5] * 9) 

score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
data = np.hstack((X_train, y_train.reshape(-1,1))) 
df = pd.DataFrame(data, columns=['Current Health', 'Level', 'Time', 'Difficulty'])
sns.pairplot(df)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=1, verbose=1)

plt.figure(figsize=[10,5])
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.tight_layout()
plt.show()






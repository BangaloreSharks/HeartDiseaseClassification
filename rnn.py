from keras.models import Sequential
from keras.layers import Dense,LSTM
import pickle
import numpy as np
data = pickle.load(open('data/processed_data/cleveland.pickle'))

Y = []
for line in data:
    l = [0,0,0,0,0]
    l[int(line[13])]=1
    Y.append(l)

X = [ line[:-1] for line in data]

print len(X)
print len(Y)

X_train = np.array(X)
X_train = np.reshape(X_train, X_train.shape + (1,))
print X_train.shape



model = Sequential()
model.add(Dense(13, input_shape=X_train.shape[1:], activation='relu'))
model.add(LSTM(13))
model.add(Dense(5, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# Fit the model
model.fit(X_train, Y, epochs=150, batch_size=10)

# evaluate the model
scores = model.evaluate(X_train, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

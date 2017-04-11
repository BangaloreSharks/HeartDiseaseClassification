from keras.models import Sequential
from keras.layers import Dense
import pickle

data = pickle.load(open('data/processed_data/cleveland.pickle'))

Y = []
for line in data:
    l = [0,0,0,0,0]
    l[int(line[13])]=1
    Y.append(l)

X = [ line[:-1] for line in data]

print len(X)
print len(Y)

model = Sequential()
model.add(Dense(20, input_dim=13, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(5, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

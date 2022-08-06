from keras.datasets import mnist
(train_x,train_y),(test_x,test_y)=mnist.load_data()
X=[z.ravel()for z in train_x]
y=[z.ravel for z in test_x]

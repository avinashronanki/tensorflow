# scaler is a rank zero tensor 
# vector is a rank one tensor (1d)
# matrix is a rank two tensor (2d)

import tensorflow as tf

# # print(tf.constant(3)) # scaler 

# scaler = tf.constant(4) # assiging it to a variable 
# # print(scaler)

# scalerflot = tf.constant(4, tf.float32) # change the datatype 
# # print(scalerflot)

# print(scaler.numpy())

# rank_1 = tf.constant([1,2,3]) # 1d vector 
# print(rank_1)

# rank_2 = tf.constant([[1,2,3],[4,5,6]]) # 2d matrix
# print(rank_2)

# rank_3 = tf.constant ([[[1,2,3],[4,5,6]],[[6,7,8],[9,0,1]]]) # 3d 
# print(rank_3)


# print(tf.ones([2,2])) # 2*2 ones 

# print (tf.zeros([2,2])) # 2*2 zeros 


# print(tf.eye(3,3)) # identity matrix with dignoal eliments as one 

# print(tf.fill([2,2],4)) # filling with desired eliments 

# print(tf.linspace(0,9,10))

# print(tf.range(0,9,2))

# x = tf.Variable(tf.constant([1,2,3])) # converting into a variable 

# x.assign(tf.constant([4,5,6])) # assing the new values to variable 
 
 
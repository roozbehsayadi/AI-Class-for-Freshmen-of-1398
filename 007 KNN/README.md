## KNN (k-nearest neighbors )
### What's in it?
* Why do we need KNN?
* What is KNN?
* When do we use KNN?

### Why KNN?
By now, we all know Machine Learning models makes predictionsby learning from the past data available

![KNN_picture1](./pictures/KNN_picture1.jpg | width=600)

Is this a dog?

![KNN_picture2](./pictures/KNN_picture2.jpg | width=200)
    
We can differentiate between a cat and a dog based on their characteristics

![KNN_picture3](./pictures/KNN_picture3.jpg | width=420)

We can evaluate some characteristics of them then we can usually sort out cats from dogs based on even these two characteristics

![KNN_picture4](./pictures/KNN_picture4.jpg | width=500)

now let's see if it is a cat or a dog

![KNN_picture5](./pictures/KNN_picture5.jpg | width=500)


It's features are more like cats, it must be a cat!

![KNN_picture6](./pictures/KNN_picture6.jpg | width=500)

Because KNN is based on feature similarity, we can do classification using KNN Classifier!

![KNN_picture7](./pictures/KNN_picture7.jpg | width=600)

### What is KNN?
KNN - K Nearest Neighbors, is one of the simplest **Supervised** Machine Learning algorithm mostly used for

It Classifies a data point based on how its neighbors are classified

KNN stores all available cases and classifies new cases based on a similarity measure

![KNN_picture8](./pictures/KNN_picture8.jpg | width=600)

*k* in KNN is a parameter that refers to the number of nearest neighbors to include in the **majority voting process**

A data point is classified by majority votes from its 5 nearest neighbors

![KNN_picture9](./pictures/KNN_picture9.jpg | width=600)

Here, the unknown point would be classified as red, since 4 out of 5 neighbors as red

![KNN_picture10](./pictures/KNN_picture10.jpg | width=600)

### When do we use KNN?
 1. Data is labeled
 2. Dataset is small


## Source
[SimpliLearn](https://www.slideshare.net/Simplilearn/knearest-neighbor-classification-algorithm-how-knn-algorithm-works-knn-algorithm-simplilearn)

[python-course.eu](https://www.python-course.eu/k_nearest_neighbor_classifier.php)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

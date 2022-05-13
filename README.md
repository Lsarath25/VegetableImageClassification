# VegetableImageClassification

Vegetables are one of the most widely consumed foods in the world. Vegetables are grown by people all around the world. According to a report , there are nearly hundreds of thousands of vegetable species on our planet. Picking and sorting veggies, for example. And distinguishing a vegetable in the market is difficult for the client because different veggies have similar characteristics. To address this problem, vegetable picking, sorting, and labeling must be automated using a vegetable image classifier to save time and money. Fundamental research activity in the field of agriculture nowadays is categorization and detection. There are many different types of veggies, and many people are unfamiliar with them. As a result, the design of a vegetable classifier will also give meaning to people's lives.

In addition, vegetable sorting is done by hand in supermarkets and distribution sites. As a result, this study is being done to address these issues. The goal of this work is to use CNN and pre-trained DCNN to more accurately classify vegetable photos with transfer learning. Convolutional neural networks are commonly utilized in classification, segmentation, and image recognition nowadays. Deep network design is CNN's most powerful feature, allowing it to learn mid-to high-level concepts from fresh data automatically. For vegetable picture classification, we provided a CNN model as well as four, fine-tuned state of the art CNN architectures InceptionV3. A comparison of the performance of CNN and its architectures is also carried out.



# DataSet Used
We have used an image data set containing 15 different types of vegetables.

We have 1000 different training images for each vegetable and 200 diferrent test images for each vegetable

Hence, this is a well balanced dataset

#Image Preprocessing
Image processing aims to improve graphical information for human comprehension. Basic manipulation and filtering can also lead to better feature extraction knowledge. We can pick any vegetable we like, and a random image from the class will be displayed alongside a processed image

#Data Visualization
We can start exploring the dataset and visualize any class label (for instance, Capsicum). You can choose any vegetable to visualize the images of that class. Changing rows and columns variable also results in different format positioning of matplotlib.


#Building the model
In this project, we have trained the vegetable image dataset with CNN and used transfer learning (InceptionV3); we have observed that CNN showed less accuracy when using transfer learning. In the CNN model, we have added hidden layers, max pool, and dropout layers with activation of Relu and softmax. In the case of the InceptionV3 model, we have to use transfer learning, a pre-trained model, to classify the vegetables..

CNN Model
Test_Data
Model with Transfer Learning
Total layers in the model : 315

First layer : input_2

InceptionV3 layers : Layer 2 to Layer 311

Our fine tuned layers : ['global_average_pooling2d_1', 'dense_2', 'dropout_1']

Final Layer : dense_3

Test_Data


#Conclusion
The false positives are really low as we have used transfer learning which has given us good accuracy!

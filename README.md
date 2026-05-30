# YogaRegNEvaNet
My Bachelor's Thesis: Recognition and Evaluation of Yoga Poses Based on Deep Learning
  - Collected and annotated a diverse dataset of 1,073 images across 10 distinct yoga pose classes;
  - Designed and implemented multi-modal deep learning models for yoga pose recognition, integrating Convolutional Neural Networks (VGG) and Multilayer Perceptrons (MLP) to jointly process RGB image data and human skeletal keypoint coordinates extracted via MediaPipe;
  - Conducted rigorous experiments to benchmark model performance; the best-performing classification model achieved a recognition accuracy of 99%, while pose evaluation models attained accuracy rates ranging from 69% to 80%.

The main code is divided into three parts: classification model experiment code, evaluation model experiment code, and image human skeleton extraction code.
  1. The classification model experiment code contains experiments corresponding to three data fusion schemes, as well as two unimodal control experiment codes. Running the code constitutes the training and testing process of the experimental models.
  2. The evaluation model experiment code covers five poses, each with its own folder, which in turn contains experiments corresponding to three data fusion schemes as well as two unimodal control experiment codes. Running the code constitutes the training and testing process of the experimental models.
  3. The image human skeleton extraction code is named poseEstimation.py. Given input raw image data files, it outputs skeleton coordinate data files and image data with the skeleton drawn onto them.

In the application form for my current Master's program, a writing sample of the thesis is shared.

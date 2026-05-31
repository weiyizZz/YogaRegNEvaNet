# YogaRegNEvaNet
My Bachelor's Thesis: Recognition and Evaluation of Yoga Poses Based on Deep Learning
  - Collected and annotated a diverse dataset of 1,073 images across 10 distinct yoga pose classes;
    <img width="799" height="182" alt="image" src="https://github.com/user-attachments/assets/bf8069be-2af4-42b6-8186-ac0b62d7c3be" />
  - Designed and implemented multi-modal deep learning models for yoga pose recognition, integrating Convolutional Neural Networks (VGG) and Multilayer Perceptrons   (MLP) to jointly process RGB image data and human skeletal keypoint coordinates extracted via MediaPipe;
   
    <img width="366" height="299" alt="image" src="https://github.com/user-attachments/assets/5523edf9-13cf-4d18-9858-973703bc6e0e" />
    <img width="452" height="293" alt="image" src="https://github.com/user-attachments/assets/15143e5e-210d-4f7f-8e98-a329c66feea6" />
    <img width="399" height="338" alt="image" src="https://github.com/user-attachments/assets/dc880951-1961-4bb8-a54f-1badbcac6d34" />
    
  - Conducted rigorous experiments to benchmark model performance; the best-performing classification model achieved a recognition accuracy of 99%, while pose evaluation models attained accuracy rates ranging from 69% to 80%.

The main code is divided into three parts: classification model experiment code, evaluation model experiment code, and image human skeleton extraction code.
  1. The classification model experiment code contains experiments corresponding to three data fusion schemes, as well as two unimodal control experiment codes. Running the code constitutes the training and testing process of the experimental models.
  2. The evaluation model experiment code covers five poses, each with its own folder, which in turn contains experiments corresponding to three data fusion schemes as well as two unimodal control experiment codes. Running the code constitutes the training and testing process of the experimental models.
  3. The image human skeleton extraction code is named poseEstimation.py. Given input raw image data files, it outputs skeleton coordinate data files and image data with the skeleton drawn onto them.

A writing sample of the thesis in English along with the content in the original language is shared.

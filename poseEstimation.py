import cv2
import mediapipe as mp
import numpy as np
import os
import pandas as pd
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
BG_COLOR = (192, 192, 192) # gray
for tt in ['test', 'train']:
    get_landmark = []
    for i in ['downdog', 'goddess', 'lowcobra', 'tree', 'warrior2']:
        for j in ['standard','nonstandard']:
            imgs_path = 'C:\\Users\ASUS\Desktop\毕设/yoga_pose_solo_evaluated_splited/'+ tt + '/' + i + '/' + j
            IMAGE_FILES = []
            for root, dirs, files in os.walk(imgs_path):
                for fileObj in files:
                    IMAGE_FILES.append(os.path.join(root, fileObj))
            with mp_pose.Pose(
                static_image_mode=True,
                model_complexity=2,
                enable_segmentation=True,
                min_detection_confidence=0.5) as pose:
              for iidx,file in enumerate(IMAGE_FILES):
                base = os.path.basename(file)
                idx = os.path.splitext(base)[0]
                image = cv2.imread(file)
                image_height, image_width, _ = image.shape
                # 处理前将图像模式转化为RBG
                results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                pose_landmarks = results.pose_landmarks
                # 保存标记点
                if pose_landmarks is not None:
                    assert len(pose_landmarks.landmark) == 33, 'Unexpected number of predicted pose landmarks: {}'.format(
                        len(pose_landmarks.landmark))
                    pose_landmarks = [[lmk.x, lmk.y, lmk.z] for lmk in pose_landmarks.landmark]
                    # 从图片的相对位置坐标转化为绝对位置坐标
                    pose_landmarks *= np.array([image_width, image_height, image_width])
                    pose_landmarks = np.around(pose_landmarks, 5).flatten().astype(np.str).tolist()
                    pose_landmarks = [i] + [j] + [idx] + pose_landmarks
                    get_landmark.append(pose_landmarks)
                if not results.pose_landmarks:
                  continue
                '''annotated_image = image.copy()
                # 对图像进行分割
                # 为了改善边界周围的分割，考虑应用一个关节
                # bilateral（双向的） filter to "results.segmentation_mask" with "image".
                condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
                bg_image = np.zeros(image.shape, dtype=np.uint8)
                bg_image[:] = BG_COLOR
                annotated_image = np.where(condition, annotated_image, bg_image)
                # 在图片上绘制动作标志
                mp_drawing.draw_landmarks(
                    annotated_image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                save_path = 'C:/datasets/annotated_image_evaluated_splited_uncut/' + tt + '/' + i + '/' + j + '/'
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                cv2.imwrite(save_path + str(idx) + '.png', annotated_image)
                # plot绘制关键点坐标和连线
                mp_drawing.plot_landmarks(
                    results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)'''
    train_landmark_df = pd.DataFrame(data=get_landmark)
    train_landmark_df.to_csv('C:\\Users\ASUS\Desktop\毕设/' + tt + '_landmarks.csv')

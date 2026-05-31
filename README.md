# YogaRegNEvaNet

**Bachelor's Thesis | Beijing Sport University

Recognition and Evaluation of Yoga Poses using multi-modal deep learning, combining RGB image data and human skeletal keypoints for both pose classification and quality scoring.

---

## Overview

This project addresses two sub-tasks:
- **Recognition**: classifying which yoga pose is being performed
- **Evaluation**: scoring how well the pose is being performed

Both tasks use a multi-modal fusion approach combining CNN-based image features (VGG) and MLP-based skeletal keypoint features extracted via MediaPipe.


<img width="366" height="299" alt="image" src="https://github.com/user-attachments/assets/019c0353-b80e-4d3d-b030-c43d19938d98" />
<img width="452" height="293" alt="image" src="https://github.com/user-attachments/assets/d91f1932-b55a-4be4-8a01-0edb82528aa5" />
<img width="399" height="338" alt="image" src="https://github.com/user-attachments/assets/c41b7db8-b744-4ade-a94d-b18f1c812298" />

---

## Dataset

- 1,073 images collected and manually annotated across 10 yoga pose classes
  <img width="787" height="175" alt="image" src="https://github.com/user-attachments/assets/a1561794-4567-435e-a569-dc1e3730285d" />

- Skeletal keypoint coordinates extracted using `poseEstimation.py` (MediaPipe)

---

## Results

| Task | Best Accuracy |
|---|---|
| Pose Recognition | 99% |
| Pose Evaluation | 69% – 80% (across 5 poses) |

---

## Repository Structure

```
classification_models/    # Recognition experiments (3 fusion schemes + 2 unimodal baselines)
scoring_models/           # Evaluation experiments per pose (same structure)
human skeleton data/      # Extracted keypoint coordinate data
poseEstimation.py         # MediaPipe-based skeleton extraction pipeline
WritingSample_Thesis.pdf  # English writing sample with original-language content
```

---

## How It Works

1. **Skeleton extraction** — `poseEstimation.py` takes raw images and outputs keypoint coordinate files and annotated images with skeletons drawn
2. **Classification** — models in `classification_models/` train and evaluate pose recognition across three data fusion schemes
3. **Scoring** — models in `scoring_models/` evaluate pose quality, with a separate folder per pose

---

## Tech Stack

MediaPipe · VGG · MLP · Python · Jupyter Notebook

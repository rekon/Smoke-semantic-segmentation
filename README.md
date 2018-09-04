### Smoke detection via semantic segmentation using _Baseline U-Net model_ and image augmentation

This repo is a partial implementation from [Kaggle](https://www.kaggle.com/kmader/baseline-u-net-model-part-1/)

The main purpose of this use-case is to detect smoke in any background. The smoke can also have variations regarding its source, color, environment etc. We should be able to semantically segment smoke to analyze it's various features like color, intensity, duration of ejection of smoke (from video feed), etc.

The master branch has implementation of **U-Net**, however another implemetation using **[LinkNet](https://arxiv.org/pdf/1707.03718.pdf)** is provided in different branch.

---
### U-Net
The U-Net is a convolutional neural network that was developed for biomedical image segmentation at the Computer Science Department of the University of Freiburg, Germany. The network is based on the fully convolutional network and its architecture was modified and extended to work with fewer training images and to yield more precise segmentations.

_Architecture_
![U-Net architecture](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/u-net-architecture.png "U-Net")
_Image source: Computer Science Department of the University of Freiburg, Germany_

---

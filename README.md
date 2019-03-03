# Handwritten address localization & recognition

*[TD] (Text Detection) Detect text area from input image*

*[TR] (Text Recognition) Recognize text content*

*[Overview] Summary, overview, survey papers*

## 1. Books
- [2018] Deep Learning with Python, F. Chollet [`book`](http://faculty.neu.edu.cn/yury/AAI/Textbook/Deep%20Learning%20with%20Python.pdf)

## 1. Papers & Code

#### 2018
- [2018] FAQ: Build a Handwritten Text Recognition System using TensorFlow (Harald Scheidl)
[`blog`](https://towardsdatascience.com/faq-build-a-handwritten-text-recognition-system-using-tensorflow-27648fb18519)

#### 2017
- [2017-CVPR] [TD] EAST: An Efficient and Accurate Scene Text Detector [`paper`](https://arxiv.org/abs/1704.03155) [`implementation`](https://github.com/argman/EAST) [`example`](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/)

#### 2015
- [2015-PAMI] [TR] An End-to-End Trainable Neural Network for Image-based SequenceRecognition and Its Application to Scene Text Recognition [`paper`](https://arxiv.org/abs/1507.05717) [`implementation`](https://github.com/qjadud1994/CRNN-Keras)

## 2. Datasets

#### CEDAR

|Dataset| Description | Competition Paper |
|---|---|----|
|[CEDAR]( http://www.cedar.buffalo.edu/Databases/ ) | handwritten words, ZIP Codes, Digits and Alphabetic characters | `paper` [![link](https://www.lds.org/bc/content/shared/content/images/gospel-library/manual/10735/paper-icon_1150845_tmb.jpg)](https://cedar.buffalo.edu/~srihari/papers/JFS-2002.pdf)|

#### IAM Handwriting Database  

|Dataset| Description | Competition Paper |
|---|---|----|
|[IAM](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database) | forms of handwritten English text | `paper` [![link](https://www.lds.org/bc/content/shared/content/images/gospel-library/manual/10735/paper-icon_1150845_tmb.jpg)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.33.5886&rep=rep1&type=pdf)|

#### `ICDAR Benchmark Datasets`

|Dataset| Description | Competition Paper |
|---|---|----|
|[ICDAR 2017](http://rrc.cvc.uab.es/)| over 173,589 labeled text regions in over 63,686 images |`paper`  [![link](https://www.lds.org/bc/content/shared/content/images/gospel-library/manual/10735/paper-icon_1150845_tmb.jpg)](https://arxiv.org/abs/1601.07140)|
|[ICDAR 2015](http://rrc.cvc.uab.es/)| 1000 training images and 500 testing images|`paper`  [![link](https://www.lds.org/bc/content/shared/content/images/gospel-library/manual/10735/paper-icon_1150845_tmb.jpg)](http://rrc.cvc.uab.es/files/Robust-Reading-Competition-Karatzas.pdf)|
|[ICDAR 2013](http://dagdata.cvc.uab.es/icdar2013competition/)| 229 training images and 233 testing images |`paper`  [![link](https://www.lds.org/bc/content/shared/content/images/gospel-library/manual/10735/paper-icon_1150845_tmb.jpg)](http://dagdata.cvc.uab.es/icdar2013competition/files/icdar2013_competition_report.pdf)|
|[ICDAR 2011](http://robustreading.opendfki.de/trac/)| 229 training images and 255 testing images |`paper`  [![link](https://www.lds.org/bc/content/shared/content/images/gospel-library/manual/10735/paper-icon_1150845_tmb.jpg)](http://www.iapr-tc11.org/archive/icdar2011/fileup/PDF/4520b491.pdf)|
|[ICDAR 2005](http://www.iapr-tc11.org/mediawiki/index.php/ICDAR_2005_Robust_Reading_Competitions)| 1001 training images and 489 testing images |`paper`  [![link](https://www.lds.org/bc/content/shared/content/images/gospel-library/manual/10735/paper-icon_1150845_tmb.jpg)](http://www.academia.edu/download/30700479/10.1.1.96.4332.pdf)|
|[ICDAR 2003](http://www.iapr-tc11.org/mediawiki/index.php/ICDAR_2003_Robust_Reading_Competitions)| 181 training images and 251 testing images(word level and character level) |`paper`  [![link](https://www.lds.org/bc/content/shared/content/images/gospel-library/manual/10735/paper-icon_1150845_tmb.jpg)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.332.3461&rep=rep1&type=pdf)|

## 3. Online OCR Service

| Name | Description |
|---|----
|[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)| API，free |
|[Online OCR](https://www.onlineocr.net/)| API，free |
|[Free OCR](http://www.free-ocr.com/)| API，free |
|[New OCR](http://www.newocr.com/)| API，free |
|[ABBYY FineReader Online](https://finereaderonline.com)| No API，Not free |
|[Super Online Transfer Tools (Chinese)](http://www.wdku.net/)| API，free |

## 4. Blogs
- [Recurrent Neural Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [An Intuitive Explanation of Connectionist Temporal Classification](https://towardsdatascience.com/intuitively-understanding-connectionist-temporal-classification-3797e43a86c)
- [Sequence Modeling With CTC](https://distill.pub/2017/ctc/)
- [Keras github](https://github.com/keras-team/keras)
- [Keras image_ocr](https://github.com/keras-team/keras/blob/master/examples/image_ocr.py)
- [Handwritten numbers detection and recognition](https://medium.com/@o.kroeger/recognize-your-handwritten-numbers-3f007cbe46ff#.8hg7vl6mo)
- [Applying OCR Technology for Receipt Recognition](http://rnd.azoft.com/applying-ocr-technology-receipt-recognition/)
- [Convolutional Neural Networks for Object(Car License) Detection](http://rnd.azoft.com/convolutional-neural-networks-object-detection/)

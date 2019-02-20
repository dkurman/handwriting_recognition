# Handwritten address localization & recognition
## Tasks
0. Data collection and augmentation
	- envelops
	- handwritings
1. Detect the region of the envelop
2. Detect the regions of the sender and the receiver
3. Segment these regions to lines
4. Segment the lines to words
5. Text recognition
6. Recognized text enchancement 
  - compare with the words in db 
  - metric: Levenshtein distance

Last update: Feb.20 2019

## 1. Papers & Code
#### 2018

#### 2017

#### 2016

#### 2015
- [2015-PAMI] An End-to-End Trainable Neural Network for Image-based SequenceRecognition and Its Application to Scene Text Recognition [`paper`](https://arxiv.org/abs/1507.05717) [`implementation`](https://github.com/qjadud1994/CRNN-Keras)

#### 2014

## 2. Datasets

#### [`SCUT-CTW1500`](https://github.com/Yuliang-Liu/Curve-Text-Detector) `2018`

Task: text location(with different style) and recognition

[`download`](https://github.com/Yuliang-Liu/Curve-Text-Detector)

#### [`Total Text Dataset`](https://github.com/cs-chan/Total-Text-Dataset) `2017`

1,555 images with more than 3 different text orientations: Horizontal, Multi-Oriented, and Curved, one of a kind

Task: text location(with different style) and recognition

[`download`](https://github.com/cs-chan/Total-Text-Dataset)

#### [`PowerPoint Text Detection and Recognition Dataset`](https://gitlab.com/rex-yue-wu/ISI-PPT-Dataset) `2017`

21,384 images, 21,384+ text instances

Task: text location and recognition

[`download`](https://gitlab.com/rex-yue-wu/ISI-PPT-Dataset)

#### [`COCO-Text (Computer Vision Group, Cornell)`](http://vision.cornell.edu/se3/coco-text/)   `2016`

63,686 images, 173,589 text instances, 3 fine-grained text attributes.

Task: text location and recognition

[`download`](https://github.com/andreasveit/coco-text)

#### [`Synthetic Word Dataset (Oxford, VGG)`](http://www.robots.ox.ac.uk/~vgg/data/text/)   `2014`

9 million images covering 90k English words

Task: text recognition, segmantation

[`download`](http://www.robots.ox.ac.uk/~vgg/data/text/mjsynth.tar.gz)

#### [`The Street View House Number Dataset (SVHN)`](http://ufldl.stanford.edu/housenumbers)   `2012`

Real-world street view number image with its position and classification tags.

Task: number location detection, text recognition

[`download`](http://ufldl.stanford.edu/housenumbers)

#### [`IIIT 5K-Words`](http://cvit.iiit.ac.in/projects/SceneTextUnderstanding/IIIT5K.html)   `2012`

5000 images from Scene Texts and born-digital (2k training and 3k testing images)

Each image is a cropped word image of scene text with case-insensitive labels

Task: text recognition

[`download`](http://cvit.iiit.ac.in/projects/SceneTextUnderstanding/IIIT5K-Word_V3.0.tar.gz)

#### [`StanfordSynth(Stanford, AI Group)`](http://cs.stanford.edu/people/twangcat/#research)   `2012`

Small single-character images of 62 characters (0-9, a-z, A-Z)

Task: text recognition

[`download`](http://cs.stanford.edu/people/twangcat/ICPR2012_code/syntheticData.tar)

#### [`MSRA Text Detection 500 Database (MSRA-TD500)`](http://www.iapr-tc11.org/mediawiki/index.php/MSRA_Text_Detection_500_Database_(MSRA-TD500))   `2012`

500 natural images(resolutions of the images vary from 1296x864 to 1920x1280)

Chinese, English or mixture of both

Task: text detection

#### [`Street View Text (SVT)`](http://tc11.cvc.uab.es/datasets/SVT_1)   `2010`

350 high resolution images (average size 1260 × 860) (100 images for training and 250 images for testing)

Only word level bounding boxes are provided with case-insensitive labels

Task: text location

#### [`KAIST Scene_Text Database`](http://www.iapr-tc11.org/mediawiki/index.php/KAIST_Scene_Text_Database)   `2010`

3000 images of indoor and outdoor scenes containing text

Korean, English (Number), and Mixed (Korean + English + Number)

Task: text location, segmantation and recognition

#### [`Chars74k`](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/)   `2009`

Over 74K images from natural images, as well as a set of synthetically generated characters

Small single-character images of 62 characters (0-9, a-z, A-Z)

Task: text recognition

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
|[Online Chinese Recognition](http://chongdata.com/ocr/)| API，free |

## 4. Blogs

- [Scene Text Detection with OpenCV 3](http://docs.opencv.org/3.0-beta/modules/text/doc/erfilter.html)
- [Handwritten numbers detection and recognition](https://medium.com/@o.kroeger/recognize-your-handwritten-numbers-3f007cbe46ff#.8hg7vl6mo)
- [Applying OCR Technology for Receipt Recognition](http://rnd.azoft.com/applying-ocr-technology-receipt-recognition/)
- [Convolutional Neural Networks for Object(Car License) Detection](http://rnd.azoft.com/convolutional-neural-networks-object-detection/)
- [Extracting text from an image using Ocropus](http://www.danvk.org/2015/01/09/extracting-text-from-an-image-using-ocropus.html)
- [Number plate recognition with Tensorflow](http://matthewearl.github.io/2016/05/06/cnn-anpr/) [`github`](https://github.com/matthewearl/deep-anpr)
- [Using deep learning to break a Captcha system](https://deepmlblog.wordpress.com/2016/01/03/how-to-break-a-captcha-system/) [`report`](http://web.stanford.edu/~jurafsky/burszstein_2010_captcha.pdf) [`github`](https://github.com/arunpatala/captcha)
- [Breaking reddit captcha with 96% accuracy](https://deepmlblog.wordpress.com/2016/01/05/breaking-reddit-captcha-with-96-accuracy/) [`github`](https://github.com/arunpatala/reddit.captcha)
- [文字检测与识别资源-1](http://blog.csdn.net/peaceinmind/article/details/51387367)
- [文字的检测与识别资源-2](http://blog.csdn.net/u010183397/article/details/56497303?locationNum=12&fps=1)
- Scene Text Recognition in iOS [`blog`](https://medium.com/@khurram.pak522/scene-text-recognition-in-ios-11-2d0df8412151) [`github`](https://github.com/khurram18/SceneTextRecognitioniOS)

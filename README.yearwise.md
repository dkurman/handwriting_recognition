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

#### [`COCO-Text (Computer Vision Group, Cornell)`](http://vision.cornell.edu/se3/coco-text/)   `2016`

63,686 images, 173,589 text instances, 3 fine-grained text attributes.

Task: text location and recognition

[`download`](https://github.com/andreasveit/coco-text)

#### [`Synthetic Word Dataset (Oxford, VGG)`](http://www.robots.ox.ac.uk/~vgg/data/text/)   `2014`

9 million images covering 90k English words

Task: text recognition, segmantation

[`download`](http://www.robots.ox.ac.uk/~vgg/data/text/mjsynth.tar.gz)

#### [`StanfordSynth(Stanford, AI Group)`](http://cs.stanford.edu/people/twangcat/#research)   `2012`

Small single-character images of 62 characters (0-9, a-z, A-Z)

Task: text recognition

[`download`](http://cs.stanford.edu/people/twangcat/ICPR2012_code/syntheticData.tar)

#### [`MSRA Text Detection 500 Database (MSRA-TD500)`](http://www.iapr-tc11.org/mediawiki/index.php/MSRA_Text_Detection_500_Database_(MSRA-TD500))   `2012`

500 natural images(resolutions of the images vary from 1296x864 to 1920x1280)

Chinese, English or mixture of both

Task: text detection

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

- [Handwritten numbers detection and recognition](https://medium.com/@o.kroeger/recognize-your-handwritten-numbers-3f007cbe46ff#.8hg7vl6mo)
- [Applying OCR Technology for Receipt Recognition](http://rnd.azoft.com/applying-ocr-technology-receipt-recognition/)
- [Convolutional Neural Networks for Object(Car License) Detection](http://rnd.azoft.com/convolutional-neural-networks-object-detection/)

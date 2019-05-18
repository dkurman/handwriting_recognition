from PyQt5 import QtCore, QtWidgets, QtGui
from objects_detector import obj_detector
import collections
import cv2

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.file_ind = 0
        self.btn_sel = QtWidgets.QPushButton(u"Выбрать директорию")
        self.btn_next = QtWidgets.QPushButton(u"Следующее изображение")
        self.btn_prev = QtWidgets.QPushButton(u"Предыдущее изображение")
        self.btn_sr = QtWidgets.QPushButton(u"Начать распознавание")
        self.btn_mi = QtWidgets.QPushButton(u"Показать размеченное изображение")
        self.sel_dir = os.getcwd()
        self.grid = QtWidgets.QGridLayout()
        self.thresh = QtWidgets.QLineEdit("0.3")
        self.grid.addWidget(self.btn_sel,1,1,1,10,QtCore.Qt.AlignTop)
        self.grid.addWidget(self.btn_next,2,6,100,5,QtCore.Qt.AlignTop)
        self.grid.addWidget(self.btn_prev,2,1,100,5,QtCore.Qt.AlignTop)
        self.grid.addWidget(self.thresh,4,3,100,2,QtCore.Qt.AlignBottom)
        self.grid.addWidget(self.btn_sr,4,5,100,3,QtCore.Qt.AlignBottom)
        self.grid.addWidget(self.btn_mi,3,7,45,2,QtCore.Qt.AlignBottom)


        self.btn_sel.clicked.connect(self.select_directory)
        self.btn_next.clicked.connect(self.next_im)
        self.btn_prev.clicked.connect(self.prev_im)
        self.btn_sr.clicked.connect(self.start_recognition)
        self.btn_mi.clicked.connect(self.marked_image)

        self.setLayout(self.grid)
        pal = self.palette()
        pal.setColor(self.backgroundRole(),QtGui.QColor(0,150,0))
        self.setPalette(pal)
        self.type1 = '-'
        #self.type2 = '-'
        self.error = '' 
        self.lock = True
        self.img = None


    def paintEvent(self, e):
        painter = QtGui.QPainter()
        painter.begin(self)
        if self.lock:
            self.type1 = '-'
            #self.type2 = '-'
        try:
            painter.setPen(QtGui.QColor(255, 0, 0))
            painter.setFont(QtGui.QFont('Decorative', 14))
            painter.drawText(QtCore.QRectF(840,380,400,40),QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop, self.error)
            painter.setPen(QtGui.QColor(255, 255, 255))
            painter.setFont(QtGui.QFont('Decorative', 16))
            painter.drawText(QtCore.QRectF(100,762,300,40),QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop, "Threshold:")
            painter.drawText(QtCore.QRectF(840,170,300,40),QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop, u"Слов: " + str(self.type1))
            #painter.drawText(QtCore.QRectF(840,200,300,40),QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop, u"Проём: " + str(self.type2))
            painter.drawText(QtCore.QRectF(840,250,300,40),QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop, u"Текущий threshold: " + self.thresh.text())
            painter.drawImage(QtCore.QRect(5,90,800,650),QtGui.QImage(self.sel_dir + '/' + get_filename(self.sel_dir)[self.file_ind]))
            painter.setFont(QtGui.QFont('Decorative', 22))
            painter.drawText(QtCore.QRectF(840,90,300,40),QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop, u"Изображение: " + str(self.file_ind + 1))
 
        except:
            pass
        painter.end()
        self.error = ''


    def centralize(self):
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x,y)
        self.lock = True

    def select_directory(self):
        sel_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Open a folder", self.sel_dir, QtWidgets.QFileDialog.ShowDirsOnly)   
        if sel_dir == '':
            sel_dir = self.sel_dir
        self.img = None
        self.sel_dir = sel_dir
        self.file_ind = 0
        self.lock = True
        self.update()


    def next_im(self):
        self.file_ind += 1
        if len(get_filename(self.sel_dir))<=self.file_ind:
           self.file_ind = 0
        self.img = None
        self.lock = True
        self.update()

    def prev_im(self):
        self.file_ind -= 1
        if self.file_ind < 0:
           self.file_ind = len(get_filename(self.sel_dir))-1
        self.img = None
        self.lock = True
        self.update()
    
    def start_recognition(self):
        try:
            [result, self.img] = obj_detector(self.sel_dir + '/' + get_filename(self.sel_dir)[self.file_ind], float(self.thresh.text()))
            self.type1 = collections.Counter(str(result).split("'"))['word']
            #self.type2 = collections.Counter(str(result).split("'"))['empty']
        except Exception as ex:
            print(ex)
            pass
        self.lock = False
        self.update()  

    def marked_image(self):
        if self.img is not None:
            cv2.imshow("Marked image", cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR))
        else:
            self.error = u"Распознавание не было запущено!"
        self.lock = False
        self.update()


def get_filename(cur_dir):
    filenames = []
    files = os.listdir(cur_dir)
    for elem in files:
        if len(elem.split("."))>1 and elem.split(".")[1].capitalize() in ["Jpg","Jpeg"]:
            filenames.append(elem)          
    return filenames

if __name__ == "__main__":
    import sys
    import os
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("Object recognition")
    main_window.resize(1400,800)
    main_window.centralize()
    main_window.show()
    sys.exit(app.exec_())


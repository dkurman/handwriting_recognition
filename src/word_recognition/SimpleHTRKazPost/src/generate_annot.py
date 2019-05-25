import os
import shutil
from PIL import Image


classes = {
    0: 'Казахстан',
    1: 'Белоруссия',
    2: 'Киргизия',
    3: 'Таджикистан',
    4: 'Узбекистан',
    5: 'Астана',
    6: 'Алматы',
    7: 'Актау',
    8: 'Актобе',
    9: 'Атырау',
    10: 'Караганда',
    11: 'Костанай',
    12: 'Кызылорда',
    13: 'Павлодар',
    14: 'Петропавловск',
    15: 'Семей',
    16: 'Тараз',
    17: 'Уральск',
    18: 'Туркестан',
    19: 'Кокшетау',
    20: 'Шымкент',
    21: 'Россия',
    22: 'Украина',
    23: 'Абхазия',
    24: 'Южная Осетия',
    25: 'Молдавия',
    26: 'Акмолинская',
    27: 'Алматинская',
    28: 'Мангистауская',
    29: 'Актюбинская',
    30: 'Атырауская',
    31: 'Карагандинская',
    32: 'Костанайская',
    33: 'Кызылординская',
    34: 'Павлодарская',
    35: 'Северно-Казахстанская',
    36: 'Восточно-Казахстанская',
    37: 'Жамбыльская',
    38: 'Западно-Казахстанская',
    39: 'Туркестанская',
    40: 'Усть-Каменогорск',
    41: 'Южно-Казахстанская',
}

""" Open words text files """
words_txt = open("words.txt", "w")

wd = os.getcwd()
img_dir = os.path.join(wd, "words")

for filename in os.listdir(img_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"): 
        img_path = os.path.join(img_dir, filename)
        #os.rename(img_path, os.path.join(img_dir, filename.split('_')[0] + '_' + filename.split(' ')[-1]))
    else:
        continue 

    im=Image.open(img_path)
    w = int(im.size[0])
    h = int(im.size[1])

    class_id = filename.split('_')[0]
    name = os.path.splitext(filename)[0]
    status = "ok"
    graylevel = 154
    bbox = " ".join([str(x) for x in (0, 0, w, h)])
    tag = "NP"
    word = classes[int(class_id)]
    line = "{0} {1} {2} {3} {4} {5}".format(name, status, graylevel, bbox, tag, word)
    words_txt.write(line + '\n')
words_txt.close()
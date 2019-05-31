#!/bin/bash

for file in $(find /home/kairat/kazpost/SimpleHTR/data/words/ -type f); do
    ./DeslantImg ${file} /home/kairat/kazpost/SimpleHTRKazPost/data/words/$(basename $file);
    echo ${file} /home/kairat/kazpost/SimpleHTRKazPost/data/words/$(basename $file)
done

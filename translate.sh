#!/bin/bash


for file in data/train/*;
do
python3 ./m2m_100_418M.py --input "$file" >> librispeech_translated.txt &
done
wait

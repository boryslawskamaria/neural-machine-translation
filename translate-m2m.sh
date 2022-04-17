#!/bin/bash


for file in data/*;
do
python3 ./m2m_100_418M.py --input "$file" >> m2m_translated.txt &
done
wait

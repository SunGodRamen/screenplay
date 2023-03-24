#!/usr/bin/env sh
for s in ./*.fountain
do 
    screenplain --format pdf $s pdf/$s.pdf
done

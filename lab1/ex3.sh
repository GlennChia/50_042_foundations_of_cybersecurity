#! /usr/bin/bash

rm "$1".plaintext > /dev/null
k=-1
until [[ $(file --mime-type "$1".plaintext) == *"image/png" ]]; do
    k=$(echo $k + 1 | bc)
    if (( k > 255 )); then
        exit
    fi
    echo Trying key $k
    python3 ex2.py -i "$1" -k $k -m d
done

echo Obtained PNG file with key $k
xdg-open "$1".plaintext > /dev/null

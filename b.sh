#!/bin/bash

python3 vol_clear_file.py

for img in $(ls frames_output/*.png | sort -V); do
    python3 a.py "$img"
    python3 d.py
    python3 v.py
done

python3 v1.py



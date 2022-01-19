# studip_ziptool
This tool removes the "[x]_" at the beginning of StudIP zip Archives.
It also deletes the "archive_filelist.csv" file

#### Dependencies:

- python
- os
- regex / re

#### How to use

1. Download and unzip your StudIP .zip file and place the extracted folder where it belongs

2. Clone or download this repository and start the python file: <u>stupid.py</u>
3. Enter the complete folder location into the input field
4. thats it :)

#### How it works

This script uses the regex expression:  **^\\[\d+\\]** and just deletes that part of the filename.

archive_filelist.csv is also deleted if present

example:

| Original                 | After running this script |
| ------------------------ | ------------------------- |
| [0]_211125_annotated.pdf | 211125_annotated.pdf      |
| [1]_211111.pdf           | 211111.pdf                |
| [2]_ML_v5_3.m4v          | ML_v5_3.m4v               |
| archive_filelist.csv     | *deleted*                 |

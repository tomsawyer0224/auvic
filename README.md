# About
auvic (audio vidio converter) converts audio in a video to mp3 format.
# How to use
0. This project needs conda (or mamba) to run.
1. Clone this project.
```
git clone https://github.com/tomsawyer0224/auvic.git
cd auvic
```
2. Run bellow command to create and activate conda environment.
```
conda env create -f environment.yml
conda activate auvic
```
3. Run the following command to convert videos from 'source directory' and save them into 'target directory'.
```
python convert.py -s <source directory> -t <target directory>
```

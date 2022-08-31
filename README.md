# Translation API service based on [NVIDIA Nemo](https://developer.nvidia.cn/nvidia-nemo)
### Setup
```
$ conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
$ apt-get update && apt-get install -y libsndfile1 ffmpeg
$ pip install Cython
$ pip install nemo_toolkit['all']
$ pip install Flask
```
### How to use
```
$ flask --app index run
```

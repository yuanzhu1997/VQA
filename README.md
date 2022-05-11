# Visual question answering final project

This is a final project about [visual question answering][2] implemented through [PyTorch][1]. The code is written based on [github][0]. 



## Running the model

- Clone this repository with:
```
git clone https://github.com/yuanzhu1997/VQA --recursive
```
- Set the paths to your downloaded [questions, answers, and abstract-scene images][4] in `config.py`.
- Pre-process images with [ResNet18 weights ported from Caffe][3] and vocabularies for questions and answers with:
```
python preprocess-images.py
python preprocess-vocab.py

```
- Train the model in `model.py` with:
```
python train.py model-name
```
Here we provide four different models. 
| model-name      | Description |
| ----------- | ----------- |
| Base      | Baseline        |
| LSTM-Base | Baselien w/ 1layer LSTM question encoding |
| LSTM-3-Base | Baselien w/ 3layer GRU question encoding |
| LSTM-bi-Base | Baselien w/ bidirection LSTM question encoding |
| GRU-Base  | Baselien w/ 1layer GRU question encoding |
| GRU-3-Base  | Baselien w/ 3layer GRU question encoding |
| GRU-bi-Base | Baselien w/ bidirection GRU question encoding |
| SCA      | spatial-channel attention       |
| CSA      | channel-spatial attention       |
| C-Base      | channel attention       |
| S-Base      | spatial only attention       |


The process will alternate between training and validation process while preting out the current progress to stdout. After the training, the result will be automatically saved in the `logs` directory. 

The logs contain the name of the model, training statistics, contents of `config.py`,  model weights, evaluation information (per-question answer and accuracy), and question and answer vocabularies.



## Python 3 dependencies (tested on Python 3.6.2)

- torch
- torchvision
- h5py
- tqdm



[0]: https://github.com/Cyanogenoid/pytorch-vqa
[1]: https://github.com/pytorch/pytorch
[2]: http://visualqa.org/
[3]: https://github.com/ruotianluo/pytorch-resnet
[4]: http://visualqa.org/vqa_v1_download.html

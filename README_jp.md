# 事前学習済み拡散モデル
本リポジトリでは事前学習済みの拡散モデルを公開しております。本リポジトリの経緯については[ブログ](https://example.com)をご覧ください。

# 前提条件
## 実行環境

OS: Ubuntu, Mac, Windows (Git bash)

## 実行準備
以下のコマンドを実行してください。

``` install.sh
git clone https://github.com/alfredplpl/pretrained-diffusion-model-pytorch.git
cd pretrained-diffusion-model-pytorch
pip install -r requirements.txt
```

# テスト

``` sample.sh
python sample.py 
```

![cat](sample.png)
>>>>>>> 4f8898e1d086ebf8be4090cfde3a569296e0a0b6

# 参考文献

``` ddpm.bib
@inproceedings{NEURIPS2020_4c5bcfec,
    author      = {Ho, Jonathan and Jain, Ajay and Abbeel, Pieter},
    booktitle   = {Advances in Neural Information Processing Systems},
    editor      = {H. Larochelle and M. Ranzato and R. Hadsell and M.F. Balcan and H. Lin},
    pages       = {6840--6851},
    publisher   = {Curran Associates, Inc.},
    title       = {Denoising Diffusion Probabilistic Models},
    url         = {https://proceedings.neurips.cc/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf},
    volume      = {33},
    year        = {2020}
}
```

``` improve_ddpm.bib
@InProceedings{pmlr-v139-nichol21a,
    title       = {Improved Denoising Diffusion Probabilistic Models},
    author      = {Nichol, Alexander Quinn and Dhariwal, Prafulla},
    booktitle   = {Proceedings of the 38th International Conference on Machine Learning},
    pages       = {8162--8171},
    year        = {2021},
    editor      = {Meila, Marina and Zhang, Tong},
    volume      = {139},
    series      = {Proceedings of Machine Learning Research},
    month       = {18--24 Jul},
    publisher   = {PMLR},
    pdf         = {http://proceedings.mlr.press/v139/nichol21a/nichol21a.pdf},
    url         = {https://proceedings.mlr.press/v139/nichol21a.html},
}
```
``` cifar.bib
@article{CIFAR10,
    titl        = {Learning Multiple Layers of Features from Tiny Images},
    author      = {Alex Krizhevsky},
    year        = {2009},
    url         = {http://www.cs.toronto.edu/~kriz/cifar.html},
}
```
# 事前学習済み拡散モデル
本リポジトリでは事前学習済みの拡散モデルを公開しております。本リポジトリの経緯については[ブログ](https://example.com)をご覧ください。
本リポジトリのサンプルは[Google Colab](https://colab.research.google.com/drive/1T_8PvL85n7vwxDehcjpObVoGBDOlcPYr?usp=sharing)
にて試すことができます。まずはそちらをやってみてもよいでしょう。

# 前提条件
## 実行環境
実行の確認が取れているのは以下のとおりです。

OS: Ubuntu, Mac

おそらく動く環境は以下のとおりです。

OS: Windows (Git bash)

なお、CPUで生成するため、GPUは必ずしも必要ではありません。

## 実行準備
以下のコマンドを実行してください。

``` install.sh
git clone https://github.com/alfredplpl/pretrained-diffusion-model-pytorch.git
cd pretrained-diffusion-model-pytorch
pip install -r requirements.txt
```

#  画像生成テスト
以下のコマンドを実行してください。

``` sample.sh
python sample.py 
```
実行した結果、resultsフォルダにsample_0.pngと書かれた画像ファイルが生成されるはずです。
この画像は拡散モデルによって生成された猫画像になります。生成した例を以下に示します。

![cat](sample.png)

CIFAR-10から選ばれた100種類の猫がランダムに生成されるはずです。
あるいはただのノイズが出力されるかもしれません。何度も実行して遊んでみてください。

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
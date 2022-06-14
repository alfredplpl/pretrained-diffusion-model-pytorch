# Pretrained Diffusion Model 
([Japanese](README_jp.md))

Pretrained diffusion model for image generation.

You can also play the code by [Google Colab](https://colab.research.google.com/drive/1T_8PvL85n7vwxDehcjpObVoGBDOlcPYr?usp=sharing).

# Prerequisites
## Environment
OS: Ubuntu, Mac

You must not have a computer with GPU.

## Ready for test
Please run the command.

I am sorry to forget my presentation.
I am writing the first journal.
So, I will send the journal soon.
And I am researching about a part of gamification for robot remote control.
I am going to talk about a part of gamification next meeting.

``` install.sh
git clone https://github.com/alfredplpl/pretrained-diffusion-model-pytorch.git
cd pretrained-diffusion-model-pytorch
pip install -r requirements.txt
```

# Image generation test
Please run the command.

``` sample.sh
python sample.py 
```

You can see a cat image at ./results/sample_0.png.

![cat](sample.png)

Please try the test repeatedly.
You will be able to see another cat image.

# References
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


# OpenMixup

**News**
* OpenMixup v0.2.2 is released, which supports new self-supervised methods, backbones and losses as [#5](https://github.com/Westlake-AI/openmixup/issues/5).
* OpenMixup v0.2.1 is released, which supports new methods as [#4](https://github.com/Westlake-AI/openmixup/issues/4) (bugs fixed).
* OpenMixup v0.2.0 is released, which supports new features as [#3](https://github.com/Westlake-AI/openmixup/issues/3). We have reorganized configs and fixed bugs.
* OpenMixup v0.1.3 is released (finished code refactoring and fixed bugs), which steadily supports ViTs, self-supervised methods (e.g., MoCo.V3 and MAE), and online analysis (kNN metric and visualization). It requires the rebuilding of OpenMixup (install mmcv-full to support ViTs). More results are provided in Model Zoos.
* OpenMixup v0.1.1 is released, which supports various backbones (ConvNets and ViTs), various mixup methods (e.g., [PuzzleMix](https://arxiv.org/abs/2009.06962), [AutoMix](https://arxiv.org/pdf/2103.13027), [SAMix](https://arxiv.org/pdf/2111.15454), [DecoupleMix](https://arxiv.org/abs/2203.10761) etc.), various classification datasets, benchmarks (model_zoo), config files generation, FP16 training (Apex or MMCV).

## Introduction

The master branch works with **PyTorch 1.8** or higher (required by some self-supervised methods). You can still use **PyTorch 1.6** for supervised classification methods.

`OpenMixup` is an open-source supervised, self- and semi-unsupervised representation learning toolbox based on PyTorch, especially for mixup-related methods.

### What does this repo do?

Learning discriminative visual representation efficiently that facilitates downstream tasks is one of the fundamental problems in computer vision. Data mixing techniques largely improve the quality of deep neural networks (DNNs) in various scenarios. Since mixup techniques are used as augmentations or auxiliary tasks in a wide range of cases, this repo focuses on mixup-related methods for Supervised, Self- and Semi-Supervised Representation Learning. Thus, we name this repo `OpenMixp`.

### Major features

This repo will be continued to update in the next two months! Please watch us for latest update!

## Change Log

Please refer to [CHANGELOG.md](docs/CHANGELOG.md) for details and release history.

[2020-05-24] `OpenMixup` v0.2.2 is released.

[2020-04-19] `OpenMixup` v0.2.1 is released.

[2020-04-08] Configs reoriganized and new methods supported in `OpenMixup` v0.2.0.

## Installation

Please refer to [INSTALL.md](docs/INSTALL.md) for installation and dataset preparation.

## Get Started

Please see [Getting Started](docs/GETTING_STARTED.md) for the basic usage of OpenMixup (based on MMSelfSup).
Then, see [tutorials](docs/tutorials) for more tech details (based on MMClassification).

## Benchmark and Model Zoo

[Model Zoos](docs/model_zoos) and lists of [Awesome Mixups](docs/awesome_mixups) have been released, and will be updated in the next two months. Checkpoints and traning logs will be updated soon! 

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Acknowledgement

- OpenMixup is an open source project for mixup methods created by researchers in CAIRI AI LAB. We encourage researchers interested in mixup methods to contribute to OpenMixup!
- This repo borrows the architecture design and part of the code from [MMSelfSup](https://github.com/open-mmlab/mmselfsup) and [MMClassification](https://github.com/open-mmlab/mmclassification).

## Citation

If you find this project useful in your research, please consider cite our repo:

```BibTeX
@misc{2022openmixup,
    title={{OpenMixup}: Open Mixup Toolbox and Benchmark for Visual Representation Learning},
    author={Li, Siyuan and Liu, Zichen and Wu, Di, Stan Z. Li},
    howpublished = {\url{https://github.com/Westlake-AI/openmixup}},
    year={2022}
}
```

## Contributors

For now, the direct contributors include: Siyuan Li ([@Lupin1998](https://github.com/Lupin1998)), Zicheng Liu ([@pone7](https://github.com/pone7)), and Di Wu ([@wudi-bu](https://github.com/wudi-bu)). We thanks contributors for MMSelfSup and MMClassification.

## Contact

This repo is currently maintained by Siyuan Li (lisiyuan@westlake.edu.cn) and Zicheng Liu (liuzicheng@westlake.edu.cn).

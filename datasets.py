from pathlib import Path

import torch
import torch.nn.functional as F

from torchvision import transforms, datasets

n_bits = 8


def preprocess(x):
    # Follows:
    # https://github.com/tensorflow/tensor2tensor/blob/e48cf23c505565fd63378286d9722a1632f4bef7/tensor2tensor/models/research/glow.py#L78

    x = x * 255  # undo ToTensor scaling to [0,1]

    n_bins = 2**n_bits
    if n_bits < 8:
      x = torch.floor(x / 2 ** (8 - n_bits))
    x = x / n_bins - 0.5

    return x


def postprocess(x):
    x = torch.clamp(x, -0.5, 0.5)
    x += 0.5
    x = x * 2**n_bits
    return torch.clamp(x, 0, 255).byte()


def get_SVHN(augment, dataroot, download):
    image_shape = (32, 32, 3)
    num_classes = 10

    test_transform = transforms.Compose([transforms.ToTensor(), preprocess])

    if augment:
        transformations = [transforms.RandomAffine(0, translate=(0.1, 0.1)),
                           transforms.RandomHorizontalFlip()]
    else:
        transformations = []

    transformations.extend([transforms.ToTensor(), preprocess])

    train_transform = transforms.Compose(transformations)

    one_hot_encode = lambda target: F.one_hot(torch.tensor(target), num_classes)

    path = Path(dataroot) / 'data' / 'SVHN'
    train_dataset = datasets.SVHN(path, split="train",
                                     transform=train_transform,
                                     target_transform=one_hot_encode,
                                     download=download)

    test_dataset = datasets.SVHN(path, split="test",
                                    transform=test_transform,
                                    target_transform=one_hot_encode,
                                    download=download)

    return image_shape, num_classes, train_dataset, test_dataset


def get_CIFAR10(augment, dataroot, download):
    image_shape = (32, 32, 3)
    num_classes = 10

    test_transform = transforms.Compose([transforms.ToTensor(), preprocess])

    if augment:
        transformations = [transforms.RandomAffine(0, translate=(0.1, 0.1)),
                           transforms.RandomHorizontalFlip()]
    else:
        transformations = []

    transformations.extend([transforms.ToTensor(), preprocess])

    train_transform = transforms.Compose(transformations)

    one_hot_encode = lambda target: F.one_hot(torch.tensor(target), num_classes)

    path = Path(dataroot) / 'data' / 'CIFAR10'
    train_dataset = datasets.CIFAR10(path, train=True,
                                     transform=train_transform,
                                     target_transform=one_hot_encode,
                                     download=download)

    test_dataset = datasets.CIFAR10(path, train=False,
                                    transform=test_transform,
                                    target_transform=one_hot_encode,
                                    download=download)

    return image_shape, num_classes, train_dataset, test_dataset


def get_MNIST(augment, dataroot, download):
    image_shape = (28, 28, 1)
    num_classes = 10

    test_transform = transforms.Compose([transforms.Grayscale(), transforms.ToTensor(), preprocess])

    if augment:
        transformations = [transforms.RandomAffine(0, translate=(0.1, 0.1)),
                           transforms.RandomHorizontalFlip()]
    else:
        transformations = []

    transformations.extend([transforms.Grayscale(), transforms.ToTensor(), preprocess])

    train_transform = transforms.Compose(transformations)

    one_hot_encode = lambda target: F.one_hot(torch.tensor(target), num_classes)

    path = Path(dataroot) / 'data' / 'FashionMNIST'
    train_dataset = datasets.FashionMNIST(path, train=True,
                                     transform=train_transform,
                                     target_transform=one_hot_encode,
                                     download=download)

    test_dataset = datasets.FashionMNIST(path, train=False,
                                    transform=test_transform,
                                    target_transform=one_hot_encode,
                                    download=download)

    return image_shape, num_classes, train_dataset, test_dataset

def get_NOTFMNIST(augment, dataroot, download):
    image_shape = (28, 28, 1)
    num_classes = 10

    test_transform = transforms.Compose([transforms.Grayscale(), transforms.ToTensor(), preprocess])

    if augment:
        transformations = [transforms.RandomAffine(0, translate=(0.1, 0.1)),
                           transforms.RandomHorizontalFlip()]
    else:
        transformations = []

    transformations.extend([transforms.Grayscale(), transforms.ToTensor(), preprocess])

    train_transform = transforms.Compose(transformations)

    one_hot_encode = lambda target: F.one_hot(torch.tensor(target), num_classes)

    path = Path(dataroot) / 'data' / 'MNIST'
    train_dataset = datasets.MNIST(path, train=True,
                                     transform=train_transform,
                                     target_transform=one_hot_encode,
                                     download=download)

    test_dataset = datasets.MNIST(path, train=False,
                                    transform=test_transform,
                                    target_transform=one_hot_encode,
                                    download=download)

    return image_shape, num_classes, train_dataset, test_dataset

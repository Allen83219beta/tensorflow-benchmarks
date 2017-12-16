# ResNets for ImageNet on TensorFlow

To train a ResNet, run,

```bash
./scripts/train-resnet50-imagenet
```

This command produces model checkpoints written after every epoch. To evaluate
each of these checkpoints, run,

```bash
./scripts/eval-resnet50-imagenet
```

Other example command lines are available in the `scripts/` directory (for
example, training and evaluating ResNet152 on 4 GPUs).

Make sure to first follow the instructions in the
[TensorFlow models repository](https://github.com/tensorflow/models/tree/master/research/inception#getting-started)
to get necessary data, etc.


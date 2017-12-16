# ResNets for ImageNet on TensorFlow

To train a ResNet, run,

```bash
python3 tf_cnn_benchmarks.py --model=resnet50 --data_dir=../../../../data/imagenet/
                             --checkpoint_dir=/lfs/1/deepak/checkpoints/resnet50_lr=0.05
                             --num_batches=1800000 --subset=train --learning_rate=0.05
                             --learning_rate_decay_factor=0.1 --num_epochs_per_decay=30
                             --optimizer=momentum --weight_decay=0.0001
```

This command produces model checkpoints written after every epoch. To evaluate
each of these checkpoints, run,

```bash
python3 eval_checkpoints.py -i /lfs/1/deepak/checkpoints/resnet50_lr=0.05/
                            -c "python tf_cnn_benchmarks.py --model=resnet50 --eval --data_dir=/lfs/1/deepak/data/imagenet/ --eval_subset=validation --num_batches=100 --batch_size=500"
```

Other example command lines are available in the `scripts/` directory (for
example, training and evaluating ResNet152 on 4 GPUs).

Make sure to first follow the instructions in the
[TensorFlow models repository](https://github.com/tensorflow/models/tree/master/research/inception#getting-started)
to get necessary data, etc.


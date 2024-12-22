#!/usr/bin/env bash

CONFIG=$1
shift
python -m torch.distributed.run --nproc_per_node=8 --master_port=4321 basicsr/train.py -opt "$CONFIG" --launcher pytorch "$@"
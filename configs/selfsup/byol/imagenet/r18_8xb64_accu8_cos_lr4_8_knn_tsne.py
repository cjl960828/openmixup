_base_ = '../../_base_/datasets/imagenet/byol_sz224_bs64.py'

# model settings
model = dict(
    type='BYOL',
    base_momentum=0.99,
    backbone=dict(
        type='ResNet_mmcls',
        depth=18,
        num_stages=4,
        out_indices=(3,),  # no conv-1, x-1: stage-x
        norm_cfg=dict(type='SyncBN'),
        style='pytorch'),
    neck=dict(
        type='NonLinearNeck',
        in_channels=512, hid_channels=4096, out_channels=256,
        num_layers=2,
        with_bias=True, with_last_bn=False,
        with_avg_pool=True),
    head=dict(
        type='LatentPredictHead',
        predictor=dict(
            type='NonLinearNeck',
                in_channels=256, hid_channels=4096, out_channels=256,
                num_layers=2,
                with_bias=True, with_last_bn=False, with_avg_pool=False))
)

# dataset settings for SSL metrics
val_data_source_cfg = dict(type='ImageNet')
# ImageNet dataset for SSL metrics
val_data_train_list = 'data/meta/ImageNet/train_labeled_full.txt'
val_data_train_root = 'data/ImageNet/train'
val_data_test_list = 'data/meta/ImageNet/val_labeled.txt'
val_data_test_root = 'data/ImageNet/val/'

test_pipeline = [
    dict(type='Resize', size=256),
    dict(type='CenterCrop', size=224),
    dict(type='ToTensor'),
    dict(type='Normalize', mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
]
val_data = dict(
    train=dict(
        type='ClassificationDataset',
        data_source=dict(
            list_file=val_data_train_list, root=val_data_train_root,
            **val_data_source_cfg),
        pipeline=test_pipeline,
        prefetch=False,
    ),
    val=dict(
        type='ClassificationDataset',
        data_source=dict(
            list_file=val_data_test_list, root=val_data_test_root,
            **val_data_source_cfg),
        pipeline=test_pipeline,
        prefetch=False,
    ))

# interval for accumulate gradient
update_interval = 8  # total: 8 x bs64 x 8 accumulates = bs4096

# additional hooks
custom_hooks = [
    dict(type='CosineScheduleHook',  # update momentum
        end_momentum=1.0,
        adjust_scope=[0.01, 1.0],
        warming_up="constant",
        interval=update_interval),
    dict(type='SSLMetricHook',
        val_dataset=val_data['val'],
        train_dataset=val_data['train'],  # remove it if metric_mode is None
        forward_mode='vis',
        metric_mode='knn',  # linear metric (take a bit long time on imagenet)
        visual_mode='umap',  # 'tsne' or 'umap'
        save_val=False,  # whether to save results
        initial=True,
        interval=10,
        imgs_per_gpu=256,
        workers_per_gpu=6,
        eval_param=dict(topk=(1, 5))),
]

# optimizer
optimizer = dict(
    type='LARS',
    lr=4.8,  # lr=4.8 / bs4096 for 200ep and longer training
    momentum=0.9, weight_decay=1e-6,
    paramwise_options={
        '(bn|ln|gn)(\d+)?.(weight|bias)': dict(weight_decay=0., lars_exclude=True),
        'bias': dict(weight_decay=0., lars_exclude=True),
    })

# apex
use_fp16 = True
fp16 = dict(type='apex', loss_scale=dict(init_scale=512., mode='dynamic'))
# optimizer args
optimizer_config = dict(update_interval=update_interval, use_fp16=use_fp16, grad_clip=None)

# lr scheduler
lr_config = dict(
    policy='CosineAnnealing',
    by_epoch=False, min_lr=0.,
    warmup='linear',
    warmup_iters=10, warmup_by_epoch=True,
    warmup_ratio=1e-5,
)

# runtime settings
runner = dict(type='EpochBasedRunner', max_epochs=100)

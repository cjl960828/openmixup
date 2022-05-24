from .cls_head import ClsHead
from .cls_mixup_head import ClsMixupHead
from .contrastive_head import ContrastiveHead
from .latent_pred_head import LatentPredictHead, LatentClsHead, LatentCrossCorrelationHead, MoCoV3Head
from .mim_head import MAEPretrainHead, SimMIMHead, MIMHead
from .multi_cls_head import MultiClsHead
from .pmix_block import PixelMixBlock
from .swav_head import MultiPrototypes, SwAVHead
from .vision_transformer_head import VisionTransformerClsHead

__all__ = [
    'ContrastiveHead', 'ClsHead', 'ClsMixupHead',
    'LatentPredictHead', 'LatentClsHead', 'LatentCrossCorrelationHead',
    'MoCoV3Head', 'MAEPretrainHead', 'MultiClsHead', 'MultiPrototypes', 'MIMHead',
    'SwAVHead', 'SimMIMHead', 'VisionTransformerClsHead',
    'PixelMixBlock',
]

"""Training module initialization."""

from slmflow.training.trainer import SLMTrainer
from slmflow.training.data import (
    load_dataset,
    prepare_dataset,
    DataCollator,
    format_chat_template,
)
from slmflow.training.optimizations import (
    get_memory_stats,
    optimize_for_t4,
    enable_gradient_checkpointing,
)

__all__ = [
    "SLMTrainer",
    "load_dataset",
    "prepare_dataset",
    "DataCollator",
    "format_chat_template",
    "get_memory_stats",
    "optimize_for_t4",
    "enable_gradient_checkpointing",
]

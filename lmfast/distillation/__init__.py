"""Distillation module initialization."""

from lmfast.distillation.self_distillation import SelfDistillationTrainer
from lmfast.distillation.teacher_student import DistillationTrainer

__all__ = [
    "DistillationTrainer",
    "SelfDistillationTrainer",
]

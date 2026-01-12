"""Distillation module initialization."""

from slmflow.distillation.teacher_student import DistillationTrainer
from slmflow.distillation.self_distillation import SelfDistillationTrainer

__all__ = [
    "DistillationTrainer",
    "SelfDistillationTrainer",
]

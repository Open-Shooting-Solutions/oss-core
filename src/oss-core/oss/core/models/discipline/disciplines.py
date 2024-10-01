from dataclasses import dataclass

from oss.core.models.base.discipline import BaseDiscipline, BaseStage, BasePhase, BaseStep, BaseAction


@dataclass
class DisciplineAction(BaseAction):
    # No extra fields for now
    pass


@dataclass
class DisciplineStep(BaseStep):
    actions: list[DisciplineAction]


@dataclass
class DisciplinePhase(BasePhase):
    steps: list[DisciplineStep]


@dataclass
class DisciplineStage(BaseStage):
    phases: list[DisciplinePhase]


@dataclass
class MultiStageDiscipline(BaseDiscipline):
    stages: list[DisciplineStage]


@dataclass
class SingleStageDiscipline(BaseDiscipline):
    pass


@dataclass
class ServicePistool(MultiStageDiscipline):
    pass


@dataclass
class EPP(MultiStageDiscipline):
    pass

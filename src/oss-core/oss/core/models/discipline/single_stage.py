from dataclasses import dataclass

from oss.core.models.base.discipline import BaseDiscipline, BaseStage, BasePhase, BaseStep, BaseAction


@dataclass
class DisciplineAction(BaseAction):
    # No extra fields for now
    pass


@dataclass
class SingleStageStep(BaseStep):
    actions: list[DisciplineAction]


@dataclass
class SingleStagePhase(BasePhase):
    steps: list[SingleStageStep]


@dataclass
class SingleStageDiscipline(BaseDiscipline):
    stages: list[SingleStagePhase]

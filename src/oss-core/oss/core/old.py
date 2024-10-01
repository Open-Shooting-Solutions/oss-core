from __future__ import annotations
import pkgutil
import json
from enum import Enum
from oss.core.models.base.discipline import BaseDiscipline


class DisciplineFilename(Enum):
    SERVICE_PISTOOL: str = "servicepistool.json"
    EPP: str = "epp.json"


class Discipline(BaseDiscipline):
    discipline_package_name: str = "oss.core.models.discipline"

    def __init__(self, configuration: dict):
        pass

    @staticmethod
    def get(discipline: DisciplineFilename) -> Discipline:
        discipline_filename = discipline.value
        discipline_configuration = pkgutil.get_data(
            package=Discipline.discipline_package_name, resource=discipline_filename
        )
        if not discipline_configuration:
            raise FileNotFoundError(f"Discipline file not found: {discipline_filename}")

        return Discipline(**json.loads(discipline_configuration))


print(Discipline.get(DisciplineFilename.SERVICE_PISTOOL))

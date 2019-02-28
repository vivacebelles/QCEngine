import abc
from typing import Any, Dict, Optional

from pydantic import BaseModel


class ProgramExecutor(BaseModel, abc.ABC):

    name: str
    scratch: bool
    thread_safe: bool
    thread_parallel: bool
    node_parallel: bool
    managed_memory: bool

    class Config:
        allow_mutation: False
        extra: "forbid"

    @abc.abstractmethod
    def compute(self, input_data: 'ResultInput', config: 'JobConfig') -> 'Result':
        pass

    @abc.abstractmethod
    def found(self) -> bool:
        """
        Checks if the program can be found.
        """
        pass

## Utility

    @staticmethod
    def parse_version(version: str):
        from pkg_resources import parse_version
        if "undef" in version:
            raise TypeError(
                "Using custom build without tags. Please pull git tags with `git pull origin master --tags`.")

        return parse_version(version)


## Computers

    def build_input(self, input_model: 'ResultInput', config: 'JobConfig',
                    template: Optional[str] = None) -> Dict[str, Any]:
        raise ValueError("build_input is not implemented for {}.", self.__class__)

    def execute(self, inputs, extra_outfiles, extra_commands, scratch_name, timeout):
        raise ValueError("execute is not implemented for {}.", self.__class__)

    def parse_output(self, outfiles: Dict[str, str], input_model: 'ResultInput') -> 'Result':
        raise ValueError("parse_output is not implemented for {}.", self.__class__)

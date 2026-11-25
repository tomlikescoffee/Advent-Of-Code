import inspect 
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Solution(ABC):
    def get_puzzle_input(self, puzzle_input_path : str|None = None) -> list[str]:
        if not puzzle_input_path: 
            caller_file_path = Path(inspect.stack()[1][1])
            puzzle_input_path = caller_file_path.parent.parent / "puzzle_inputs" / (caller_file_path.stem + ".txt")

        if not os.path.exists(puzzle_input_path): 
            raise FileNotFoundError(f"Unable to load puzzle input file found at `{puzzle_input_path}`. Verify the path and try again.")
            
        with open(puzzle_input_path) as f: 
                return f.read().splitlines()

    @abstractmethod
    def task_one(self) -> Any: return

    @abstractmethod
    def task_two(self) -> Any: return
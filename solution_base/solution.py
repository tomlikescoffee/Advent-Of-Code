from __future__ import annotations
import inspect 
import os
import time
from abc import ABC, abstractmethod
from functools import wraps
from pathlib import Path
from typing import Any

MS_PRECISION = 2

def time_solution(solution_func) -> None:
    @wraps(solution_func)
    def timer_wrapper(self : Solution, *args, **kwargs) -> None: 
        s = time.perf_counter()
        result = solution_func(self, *args, **kwargs)
        # Execution time in milliseconds
        execution_time_ms = round((time.perf_counter() - s) * 1000, MS_PRECISION)
        self.execution_times[solution_func.__name__] = execution_time_ms
        return result
    return timer_wrapper

class Solution(ABC): 
    def __init__(self):
        self.execution_times = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for function_name in Solution.__abstractmethods__:
            method = cls.__dict__.get(function_name)
            if method: setattr(cls, function_name, time_solution(method)) 

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

    def get_execution_times(self) -> None:
        return self.execution_times 

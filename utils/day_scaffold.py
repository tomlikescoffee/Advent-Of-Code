from datetime import datetime
from pathlib import Path 
from string import Template


class DayScaffold():  
    number_to_word = {
        1 : "One",  2 : "Two",  3 : "Three", 4 : "Four", 5 : "Five", 
        6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine",  10 : "Ten", 
        11 : "Eleven", 12 : "Twelve", 13 : "Thirteen",  14 : "Fourteen", 15 : "Fifteen", 
        16 : "Sixteen", 17 : "Seventeen", 18 : "Eighteen", 19 : "Ninteen",  20 : "Twenty", 
        21 : "TwentyOne", 22 : "TwentyTwo", 23 : "TwentyThree", 24 : "TwentyFour", 25 : "TwentyFive"   
    } 

    min_aoc_day = 1
    max_aoc_day = 25

    @staticmethod
    def generate_file(file_path : Path, file_contents: str="") -> None:
        if file_path.exists(): 
            print(f"SKIPPING: {file_path.name} already exists in {file_path.parent}") 
            return
        try:  
            print(f"CREATING: `{file_path.name}` in `{file_path.parent}`.")  
            if file_contents: file_path.write_text(file_contents)
            else: file_path.touch()
            print(f"CREATED: File `{file_path.name}` has been created in {file_path.parent}")
        except FileNotFoundError:
            print(f"ERROR: `{file_path.name}` not created. One or more missing directories in `{file_path.parent}`.") 

    @staticmethod
    def build(day:int=None, year:int=None) -> None:  
        if not year: year = int(datetime.today().strftime("%Y"))
        if not day: day = int(datetime.today().strftime("%d"))
        
        if day < DayScaffold.min_aoc_day: 
            print("SKIPPING: No puzzle as date preceeds the 1st.")
            return
        elif day > DayScaffold.max_aoc_day: 
            print("SKIPPING: No puzzle as date exceeds the 25th.") 
            return   
        
        print(f"BUILDING: Creating scaffold for year {year} day {day}.")
        project_root = Path(__file__).parent.parent 

        day_file_path = project_root / str(year) / "code" / f"day_{day}.py" 
        day_template_path = project_root / "templates" / "day_template.txt" 
        
        day_template = Template(day_template_path.read_text()).substitute({"day" : DayScaffold.number_to_word[day]})  
        DayScaffold.generate_file(day_file_path, day_template)
        
        puzzle_input_path = project_root / str(year) / "puzzle_inputs" / f"day_{day}.txt" 
        DayScaffold.generate_file(puzzle_input_path)
        print(f"COMPLETE: Scaffolding has been created for year {year} day {day}.")

from datetime import datetime
from pathlib import Path
from string import Template


class YearScaffold():
    first_aoc_year = 2015
    
    @staticmethod
    def create_dir(dir_to_create : Path) -> None: 
        if dir_to_create.exists(): 
            print(f"SKIPPING: `{dir_to_create.name}` directory exists in `{dir_to_create.parent}`.")
        else:
            print(f"CREATING: `{dir_to_create.name}` directory in `{dir_to_create.parent}`.")
            dir_to_create.mkdir(exist_ok=True, parents=True)

    @staticmethod
    def generate_directory_structure(year:int=None) -> Path|None:  
        latest_aoc_year = int(datetime.today().strftime("%Y"))
        current_month = int(datetime.today().strftime("%m"))
        
        if current_month != 12: latest_aoc_year -= 1
        year_to_create = year if year is not None else latest_aoc_year

        if YearScaffold.first_aoc_year <= year_to_create <= latest_aoc_year:             
            print(f"GENERATING: Directory structure for {year_to_create}.")
            project_root = Path(__file__).parent.parent 
            year_dir = project_root / str(year_to_create)
            YearScaffold.create_dir(year_dir)
            YearScaffold.create_dir(year_dir / "code")
            YearScaffold.create_dir(year_dir / "puzzle_inputs")   
            return year_dir 
        else: 
            print(f"ERROR: {year_to_create} is an invalid year for Advent Of Code.\n"
                  f"Valid years are between {YearScaffold.first_aoc_year} and {latest_aoc_year}.")
            return None
        
    @staticmethod
    def generate_base_files(year_dir : Path) -> None: 
        print(f"GENERATING: Necessary base files.")
        init_path = year_dir / "code" / "__init__.py"
        if init_path.exists(): 
            print(f"SKIPPING: __init__.py exists in {year_dir / 'code'}")
        else: 
            print(f"CREATING: __init__.py in {str(year_dir / 'code')}") 
            init_path.touch()

        readme_template_path = year_dir.parent / "data" / "templates" / "README_template.txt"
        readme_path = year_dir / "README.md"
        if not readme_path.exists(): 
            print(f"CREATING: README.md in `{year_dir}`")
            readme_template = Template(readme_template_path.read_text()) 
            readme_path.write_text(readme_template.substitute({"year" : year_dir.name}))
        else:  
            print(f"SKIPPING: README.md exists in `{year_dir}`")

    @staticmethod
    def build(year:int=None) -> None: 
        print(f"BUILDING: Creating scaffold for AOC year {year}.")
        year_dir = YearScaffold.generate_directory_structure(year) 
        if year_dir: YearScaffold.generate_base_files(year_dir)
        print(f"COMPLETE: Scaffolding has been created for AOC year {year}.")

from conf import _parse_project_db
from commands_api import go_to

def open_project(name:str)->str:
    paths_dict = _parse_project_db()
    for k,v in paths_dict.items():
        if k == name:
            return go_to(v)
        else:
            print(f"Can't find the path for project: {name}. \n Make sure you have added it to the registry(see help docs).")
    


open_project('drop')
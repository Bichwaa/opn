from conf import _parse_project_db,store_project_path
from commands_api import go_to
import typer



def add_project(path:str, alias=None):
    '''
    takes a project directory path and an optional alias.
    Uses the conf module's function 'store_project_path' to persist the path.
    if an alias is not provided it uses the project's directory name as provided in the path.
    '''
    #initialize dictionary
    path_dict = {}
    if alias !=None:
        path_dict[alias] = path
    else:
        default_alias = path.split("/")[-1]#linux only
        path_dict[default_alias] = path
    store_project_path(path_dict)


def open_project(name:str)->str:
    paths_dict = _parse_project_db()
    for k,v in paths_dict.items():
        if k == name:
            return go_to(v)
        else:
            print(f"Can't find the path for project: {name}. \n Make sure you have added it to the registry(see help docs).")
    

def main():
    # add_project('/home/bichwaa/Desktop/testy/gitpractice', alias='gitp')
    pass


if __name__ == "__main__":
    typer.run(main)
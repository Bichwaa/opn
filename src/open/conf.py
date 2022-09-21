"""
Handels all matters configuration.
0. Maintains a database of project locations (directory paths).

1. processes the opn.json file in a project and scans through it to pick out useful information like:
    i. preffered IDE command
    ii. server starting commands
    iii. Automation level definitions (How much of the process do you want automated onthe first go?)

sample config json file:
    {
        "ide-command":"code .",
        "server-start": "npm run serve",
        "levels:{
            "one":"ide",
            "two":"ide+server"
        }
    }
"""
import json

def add_project(path_dict:dict)->None:
    """adds a new project path to json database"""
    with open("projects.json", "r+") as outfile:
        try: #if a database of paths already exists in projects.json
            file_data = json.load(outfile)
            file_data.update(path_dict)
            outfile.seek(0)
            json.dump(file_data, outfile)
        except json.JSONDecodeError: #then its a new json file
            json.dump(path_dict, outfile)


def _parse_project_db()->dict:
    """ 
    reads persistent project location json storage,  returns a dictionary of paths.
    If the json file is empty, an empty dictionary is returned.
    """
    with open("projects.json", "r+") as outfile:
        try: #if a database of paths already exists in projects.json
            file_data = json.load(outfile)
            return file_data
        except json.JSONDecodeError: #then its a new json file
            print("the json file is empty")
            return {}




def parse_cofig()->dict:
    """reads config file in project location"""
    pass
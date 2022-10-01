import os
import subprocess

def open_in_code()->None:
    """Opens cwd in vs-code"""
    return os.system()
    # return subprocess.run('code .', shell=True)

def go_to(path:str) -> None:
    """takes in path and opens it in terminal using os.chdir"""
    print(f'changing directory to: {path}')
    os.chdir(path)
    os.system("/bin/bash")
    subprocess.run(f"pwd")
    # open_in_code()

def open_in(ide:str)->None:
    """Opens cwd in named ide"""
    return os.system(f"{ide} .")


def start_server(commands:list[str])->None:
    """takes in a list of command strings required to start a project and runs them one by one"""
    for comm in commands:
        os.system([comm])
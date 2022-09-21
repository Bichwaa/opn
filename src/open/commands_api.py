import subprocess


def go_to(path:str) -> None:
    """takes in path and opens it in terminal using cd"""
    return subprocess.Popen('cd', cwd=path)

def open_in(ide:str)->None:
    """Opens cwd in named ide"""
    return subprocess.run([ide, "."])

def open_in_code()->None:
    """Opens cwd in vs-code"""
    return subprocess.run(['code .'])


def start_server(commands:list[str])->None:
    """takes in a list of command strings required to start a project and runs them one by one"""
    for comm in commands:
        subprocess.run([comm])
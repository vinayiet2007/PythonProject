import json
import os
from pathlib import Path

class FetchElement:

    def __init__(self,file_name):
        self.__file_name=file_name

    def fetch_element_from_json(self, locator_name:str):
        log_folder = FetchElement.__get_folder()
        log_file_path = os.path.join(log_folder, self.__file_name+".json")
        print(log_file_path)
        with open(log_file_path,"r") as json_file:
            json_object = json.load(json_file)
            print(json_object[locator_name])
            return json_object[locator_name]

    @staticmethod
    def __get_folder():
        project_root = Path(__file__).resolve().parent
        while project_root != project_root.root and not (project_root / ".git").exists():
            project_root = project_root.parent
        return os.path.join(project_root, "sampleProject/resources/")

if __name__=='__main__':
    fetch_element = FetchElement("login_page")
    fetch_element.fetch_element_from_json( "user_name")
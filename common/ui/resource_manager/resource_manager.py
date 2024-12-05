from common.ui.interfaces.iResourceManager import IResourceManager

class ResourceManager(IResourceManager):

    def fetchElement(self,resource_json):
        try:
            return resource_json["locator_type"], resource_json["locator_value"]
        except LookupError:
            print(f"Wrong Format Json")

if __name__=='__main__':
    test = {'locator_type': 'xpath', 'locator_value': "//[text()='username']"}

    rm = ResourceManager()
    print(rm.fetchElement(test))
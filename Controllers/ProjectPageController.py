class ProjectPageController:
    def __init__(self):
        pass

    def update(self, event:dict):
        for key, value in event.items():
            print(key, value)
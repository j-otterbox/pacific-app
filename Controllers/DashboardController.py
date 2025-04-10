from Events.EventManager import EventManager

class DashboardController:
    def __init__(self):
        print("creating dash controller")
        self.events = EventManager()
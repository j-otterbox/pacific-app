class EventManager:
    def __init__(self):
        self._listeners: dict[str, list] = {}
        
    def subscribe(self, event_type:str, listener):
        if event_type in self._listeners:
            self._listeners[event_type].append(listener)
        else:
            self._listeners.update({event_type: [listener]})

    def unsubcribe(self, event_type:str, listener):
        self._listeners[event_type].remove(listener)

    def emit(self, event:dict):
        print(f"emitting {event["type"]} event...")
        for listener in self._listeners[event["type"]]:
            listener.update(event) # every controller has a generic update function specifically for events
    

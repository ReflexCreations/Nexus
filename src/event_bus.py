import asyncio
from typing import Any, Callable, Dict

class EventBus: 
    def __init__(self):
        self._event_handlers: Dict[str, list] = {}

    def subscribe(self, event_type: str, handler: Callable):
        if event_type not in self._event_handlers:
            self._event_handlers[event_type] = []
        self._event_handlers[event_type].append(handler)

    async def publish(self, event_type: str, data: Any):
        if event_type in self._event_handlers:
            handlers = self._event_handlers[event_type]
            for handler in handlers:
                asyncio.create_task(handler(data))
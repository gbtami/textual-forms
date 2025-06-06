# widget.py
from typing import List

from textual import on
from textual.widgets import Input, Checkbox, Select, Static, Label
from textual.containers import Center
from textual.events import Blur


def ids():
    count = 0
    while True:
        count += 1
        yield f"id-{count}"

ids = ids()


class FieldWidget:
    """
    Mixin to provide requirements for forms support.
    """
    async def on_input_changed(self, e):
        container = self.parent
        await container.remove_children(".erm")
        if (vr := e.validation_result) is not None and not vr.is_valid:
            for msg in vr.failure_descriptions:
                container.mount(Center(Static(msg), classes="erm"))


class TextWidget(Input, FieldWidget):
    def __init__(self, field: "Field", **kwargs):  # Forward reference
        super().__init__(**kwargs)
        self.field = field


class IntegerWidget(Input, FieldWidget):
    def __init__(self, field: "Field",  **kwargs): # Forward reference
        super().__init__(type='integer', **kwargs)
        self.field = field


class BooleanWidget(Checkbox, FieldWidget):
    def __init__(self, field: "Field", **kwargs): # Forward reference
        super().__init__(**kwargs)
        self.field = field


class ChoiceWidget(Select, FieldWidget):
    def __init__(self, field: "Field", choices: List[tuple[str, str]], **kwargs): # Forward reference
        super().__init__(options=choices, **kwargs)
        self.field = field
from sylenium.command.command import Command


class Click(Command):
    def execute(self, **kwargs) -> None:
        kwargs.pop("element").wrapped_element.click()

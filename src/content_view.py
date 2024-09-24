from textual.widgets import Static


class ContentView(Static):
    """Displays currently highlighted dialogue node."""

    def on_mount(self) -> None:
        self.update_content("test")

    def on_click(self) -> None:
        self.update_content("test")

    def update_content(self, name: str) -> None:
        """Get a new hello and update the content area."""
        self.update(f"{name}, [b]World[/b]!")
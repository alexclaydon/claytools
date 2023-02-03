from datetime import datetime
from itertools import cycle

from textual import events, log
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Footer, Header, Label, ListItem, ListView, Static


class Clock(Widget):
    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        return datetime.now().strftime("%c")


hellos = cycle(
    [
        "Hola",
        "Bonjour",
        "Guten tag",
        "Salve",
        "Nǐn hǎo",
        "Olá",
        "Asalaam alaikum",
        "Konnichiwa",
        "Anyoung haseyo",
        "Zdravstvuyte",
        "Hello",
    ]
)


class Hello(Static):
    """Display a greeting."""

    def on_mount(self) -> None:
        self.next_word()

    def on_click(self) -> None:
        self.next_word()

    def next_word(self) -> None:
        """Get a new hello and update the content area."""
        hello = next(hellos)
        self.update(f"{hello}, [b]World[/b]!")


class ClaytoolsApp(App):
    """A Claytools TUI"""

    CSS_PATH = "CSS/global.css"
    TITLE = "Claytools TUI"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit the app"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(id="header")
        yield Horizontal(
            Static("Sidebar", id="sidebar"),
            Vertical(
                Label("Execute:"),
                ListView(
                    ListItem(Label("One"), id="goon"),
                    ListItem(Label("Two"), id="moon"),
                    ListItem(Label("Three"), id="out"),
                    id="body",
                ),
                Hello(),
            ),
        )
        yield Footer()

    def on_mount(self, event: events.Mount) -> None:
        self.query_one(ListView).focus()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        self.log(event.item.id)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.log(event.item.id)
        if event.item.id == "goon":
            self.action_set_background("red")
        elif event.item.id == "moon":
            self.action_set_background("blue")
        elif event.item.id == "out":
            self.action_set_background("green")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color

    def on_key(self, event: events.Key) -> None:
        if event.key == "r":
            self.action_set_background("red")

    def action_quit(self) -> None:
        """An action to quit the app."""
        self.exit()


if __name__ == "__main__":
    app = ClaytoolsApp()
    app.run()

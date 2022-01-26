from rich.prompt import Prompt

asking = True

while asking:
    answer = Prompt.ask("[green]What do you want?[/]", choices=["Create", "Fetch", "Update", "Delete", "Exit"])
    if answer == "Exit":
        asking = False
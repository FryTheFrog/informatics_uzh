from src.ui import UI

ui = UI()
inp = None

while inp != "q":
    inp = None
    ui.update_menu(inp)
    ui.print_ui()
    inp = input("> ")
    ui.update_menu(inp)
    ui.print_ui()
    if inp == "e":
        key = int(input("> "))
        ui.encrypt_message(key)
    elif inp == "d":
        key = int(input("> "))
        ui.decrypt_message(key)
    elif inp == "r":
        ui = UI()
    else:
        ui.change_message(inp)

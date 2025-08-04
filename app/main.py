def copy_file(command: str) -> None:
    command_parts = command.strip().split()

    if len(command_parts) != 3:
        return

    command_name, source_file_name, destination_file_name = command_parts

    if command_name != "cp":
        return

    if source_file_name == destination_file_name:
        return

    try:
        with (open(source_file_name, "r") as source_file,
              open(destination_file_name, "w") as destination_file
              ):
            destination_file.write(source_file.read())
    except FileNotFoundError:
        return

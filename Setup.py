import cx_Freeze

executables = [cx_Freeze.Executable("Main.py")]

cx_Freeze.setup(
    name="blockfudger",
    options={"build_exe": {"packages":["pygame"]}},
    executables = executables

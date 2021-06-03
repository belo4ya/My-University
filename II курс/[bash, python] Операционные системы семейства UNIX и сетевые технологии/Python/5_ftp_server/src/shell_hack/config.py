WIN = "win32"
LUX = "linux"

ALIAS = "alias"
ARGS = "args"
SHELL = "shell"

HELP_CMD = {WIN: {"--help": "/?", "/?": "/?"},
            LUX: {"--help": "--help", "/?": "--help"}}

COMMANDS = {
    "cd": {
        WIN: {ALIAS: "cd", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "cd", SHELL: True, ARGS: {**HELP_CMD[LUX]}}
    },
    "pwd": {
        WIN: {ALIAS: "cd", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "pwd", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "ls": {
        WIN: {ALIAS: "dir", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "ls", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "mkd": {
        WIN: {ALIAS: "mkdir", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "mkdir", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "mkf": {
        WIN: {ALIAS: "echo>", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "touch", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "rmd": {
        WIN: {ALIAS: "rmdir", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "rm -r", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "rmf": {
        WIN: {ALIAS: "del", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "rm", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "echo": {
        WIN: {ALIAS: "echo", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "echo", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "dog": {
        WIN: {ALIAS: "type", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "cat", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "cp": {
        WIN: {ALIAS: "copy", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "cp", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "mv": {
        WIN: {ALIAS: "move", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "mv", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "rn": {
        WIN: {ALIAS: "move", SHELL: True, ARGS: {**HELP_CMD[WIN]}},
        LUX: {ALIAS: "mv", SHELL: False, ARGS: {**HELP_CMD[LUX]}}
    },
    "root": {
        WIN: {ALIAS: "", SHELL: True, ARGS: {}},
        LUX: {ALIAS: "", SHELL: False, ARGS: {}}
    },
}

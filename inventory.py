default_positions = [
            [
                # column 0
                "fists",
                "",
                ""
            ],
            [
                # column 1
                "",
                "",
                ""
            ],
            [
                # column 2
                "",
                "",
                ""
            ],
            [
                # column 3
                "",
                "",
                ""
            ],
            [
                # column 4
                "",
                "",
                ""
            ]
        ]

positions = [
            [
                # column 0
                "",
                "",
                ""
            ],
            [
                # column 1
                "",
                "",
                ""
            ],
            [
                # column 2
                "",
                "",
                ""
            ],
            [
                # column 3
                "",
                "",
                ""
            ],
            [
                # column 4
                "",
                "",
                ""
            ]
        ]

function = None


def set_function(new_function):
    global function
    function = new_function


def update_item(item, addorremove):
    global positions
    if addorremove == 'add':
        for j in range(0, 5):
            for i in range(0, 3):
                if positions[j][i] == "":
                    if not any(item in x for x in positions):
                        positions[j][i] = item
    if addorremove == 'remove':
        for j1 in range(0, 5):
            for i1 in range(0, 3):
                if positions[j1][i1] == item:
                    positions[j1][i1] = ""

    if function is not None:
        function(positions)


def reset_items():
    global positions
    global default_positions
    positions = default_positions
    if function is not None:
        function(positions)

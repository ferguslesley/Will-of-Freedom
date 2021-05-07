function = None


def set_function(new_function):
    global function
    function = new_function


def clear_entry():
    global function
    if function is not None:
        function()
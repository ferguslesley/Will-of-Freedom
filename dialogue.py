text = ''
function = None


def set_function(new_function):
    global function
    function = new_function


def update_textbox(new_text):
    global text
    global function
    text += new_text + '\n'
    if function is not None:
        function(text)

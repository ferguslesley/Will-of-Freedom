import dialogue


class GraphNode:
    def __init__(self, node_text):
        self.parent = None
        self.children = None
        self.node_text = node_text
        self.arc_text = None
        self.outcome = None

    def set_parent(self, parent):
        self.parent = parent

    def set_children(self, children):
        self.children = children

    def set_arc_text(self, arc_text):
        self.arc_text = arc_text

    def set_outcome(self, outcome):
        self.outcome = outcome

    def print_question(self):
        dialogue.update_textbox("[Will Says] "+self.node_text+"\n")
        if self.arc_text is not None:
            for i in self.arc_text:
                dialogue.update_textbox(i)
        else:
            print("DEBUG: Node has no children.")
            return False

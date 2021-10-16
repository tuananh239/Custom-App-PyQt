class struct(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def new_menu(menu_bar = None, text = None, args = None):
    menu = None
    if menu_bar is not None and text is not None:
        menu = menu_bar.addMenu(text)
    if args is not None:
        for action in args:
            menu.addAction(action)
    return menu

def new_tool(parent = None, text=None, args=None):
    if text is not None:
        tool = ToolBar(text = text)
    else:
        tool = ToolBar()
    if parent is not None:
        parent.addToolBar(tool)
    if args is not None:
        for action in args:
            tool.addAction(action)
    return tool
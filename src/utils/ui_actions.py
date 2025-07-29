class UIActions:
    def __init__(self):
        self._drag_data = {"x" : 0, "y" : 0}

    def on_mousewheel(self, event, canvas):
        # if linux
        if hasattr(event, 'num'):
            if event.num == 4:
                direction = -1
            else:
                direction = 1
        # if windows
        elif hasattr(event, 'delta'):
            direction = -1 if event.delta > 0 else 1
        else:
            direction = 0

        # if shift scrolling
        if event.state & 0x0001:
            canvas.xview_scroll(direction, "units")
        else:
            canvas.yview_scroll(direction, "units")

    def start_drag(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def on_drag(self, event):
        widget = event.widget
        abs_x = widget.winfo_x() + event.x - self._drag_data["x"]
        abs_y = widget.winfo_y() + event.y - self._drag_data["y"]
        widget.place(x=abs_x, y=abs_y)
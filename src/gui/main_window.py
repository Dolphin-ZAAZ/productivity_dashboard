import tkinter as tk
from tkinter import ttk
from utils.config import *

class MainWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self._setup_window()
        self._create_styles()
        self._create_widgets()
        self._setup_layout()
    
    def _setup_window(self):
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.minsize(*MIN_WINDOW_SIZE)
        self.root.configure(bg=BG_COLOR1)

    def _create_styles(self):
        self.frame_style = ttk.Style()
        self.frame_style.configure("Custom.TFrame", background=BG_COLOR2)

    def _create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="10", style="Custom.TFrame")

        self.canvas = tk.Canvas(self.main_frame, height=250, bg=BG_COLOR1)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.canvas.bind("<Shift-MouseWheel>", self.on_mousewheel)
        self.canvas.bind("<Button-4>", self.on_mousewheel)
        self.canvas.bind("<Button-5>", self.on_mousewheel)

        self.h_scrollbar = tk.Scrollbar(self.main_frame, orient="horizontal", command=self.canvas.xview)
        self.v_scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(xscrollcommand=self.h_scrollbar.set)
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)

        self.inner_canvas_frame = tk.Frame(self.canvas)

        self.inner_canvas_frame_id = self.canvas.create_window((0,0), window=self.inner_canvas_frame, anchor="nw")
        self.inner_canvas_frame.bind("<Configure>", lambda e: self._on_frame_configure(self.canvas))

        self.textBoxes = {}
        for row in range(3):
            for column in range(3):
                self.textBoxes["text" + str(column) + str(row)] = tk.Text(self.inner_canvas_frame, padx="10", pady="10", bg=BG_COLOR2)
                self.textBoxes["text" + str(column) + str(row)].bind("<MouseWheel>", self.on_mousewheel)
                self.textBoxes["text" + str(column) + str(row)].bind("<Shift-MouseWheel>", self.on_mousewheel)
                self.textBoxes["text" + str(column) + str(row)].bind("<Button-4>", self.on_mousewheel)
                self.textBoxes["text" + str(column) + str(row)].bind("<Button-5>", self.on_mousewheel)

        self.draggable = tk.Label(self.main_frame, text="hi", bg='orange', padx=10, pady=5)
        self.draggable.bind("<ButtonPress-1>", self.start_drag)
        self.draggable.bind("<B1-Motion>", self.on_drag)
        self._drag_data = {"x": 0, "y": 0}

    def _setup_layout(self):
        self.main_frame.pack(fill="both", expand=True)
        self.h_scrollbar.pack(side="bottom", fill="x")
        self.v_scrollbar.pack(side="right", fill="y")
        self.canvas.pack(fill="both", expand=True)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        for row in range(3):
            self.inner_canvas_frame.grid_rowconfigure(row, weight=1)
        for column in range(3):
            self.inner_canvas_frame.grid_columnconfigure(column, weight=1)

        for row in range(3):
            for column in range(3):
                self.textBoxes["text" + str(column) + str(row)].grid(row=row, column=column, sticky="nsew")

    def _on_frame_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    def on_mousewheel(self, event):
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
            self.canvas.xview_scroll(direction, "units")
        else:
            self.canvas.yview_scroll(direction, "units")

    def start_drag(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def on_drag(self, event):
        widget = event.widget
        abs_x = widget.winfo_x() + event.x - self._drag_data["x"]
        abs_y = widget.winfo_y() + event.y - self._drag_data["y"]
        widget.place(x=abs_x, y=abs_y)
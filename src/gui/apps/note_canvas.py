import tkinter as tk
from tkinter import ttk
from utils.ui_actions import UIActions
from utils.config import *

class NoteCanvas:
    def __init__(self, root: ttk.Frame):
        self.ui_actions = UIActions()
        self.main_frame = root
        self._create_widgets()
        self._setup_layout()

    def _create_widgets(self):
        self.canvas = tk.Canvas(self.main_frame, height=250, bg=BG_COLOR1)
        self.canvas.bind("<MouseWheel>", lambda e: self.ui_actions.on_mousewheel(e, self.canvas))
        self.canvas.bind("<Shift-MouseWheel>", lambda e: self.ui_actions.on_mousewheel(e, self.canvas))
        self.canvas.bind("<Button-4>", lambda e: self.ui_actions.on_mousewheel(e, self.canvas))
        self.canvas.bind("<Button-5>", lambda e: self.ui_actions.on_mousewheel(e, self.canvas))

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
                self.textBoxes["text" + str(column) + str(row)].bind("<MouseWheel>", lambda e: self.ui_actions.on_mousewheel(e, self.canvas))
                self.textBoxes["text" + str(column) + str(row)].bind("<Shift-MouseWheel>", lambda e: self.ui_actions.on_mousewheel(e, self.canvas))
                self.textBoxes["text" + str(column) + str(row)].bind("<Button-4>", lambda e: self.ui_actions.on_mousewheel(e, self.canvas))
                self.textBoxes["text" + str(column) + str(row)].bind("<Button-5>", lambda e: self.ui_actions.on_mousewheel(e, self.canvas))

    def _setup_layout(self):
        self.main_frame.pack(fill="both", expand=True)
        self.h_scrollbar.pack(side="bottom", fill="x")
        self.v_scrollbar.pack(side="right", fill="y")
        self.canvas.pack(fill="both", expand=True)
        
        for row in range(3):
            self.inner_canvas_frame.grid_rowconfigure(row, weight=1)
        for column in range(3):
            self.inner_canvas_frame.grid_columnconfigure(column, weight=1)

        for row in range(3):
            for column in range(3):
                self.textBoxes["text" + str(column) + str(row)].grid(row=row, column=column, sticky="nsew")

    def _on_frame_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))
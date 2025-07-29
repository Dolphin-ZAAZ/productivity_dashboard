import tkinter as tk
from tkinter import ttk
from utils.config import *
from gui.apps.note_canvas import NoteCanvas

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

    def _setup_layout(self):
        self.main_frame.pack(fill="both", expand=True)
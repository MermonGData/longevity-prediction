import os
import warnings
import numpy as np
from IPython.display import HTML, display

def setup_notebook(seed: int = 42):
    warnings.filterwarnings("ignore")
    np.random.seed(seed)
    display(HTML("<style>.output_scroll { height: auto !important; }</style>"))

def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def resolve_project_path(*paths):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    return os.path.join(project_root, *paths)

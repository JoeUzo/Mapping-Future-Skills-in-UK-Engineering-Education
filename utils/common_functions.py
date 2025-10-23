import matplotlib.pyplot as plt
import os
from pathlib import Path
import glob
import pandas as pd

PLOT_FMT = "png"
PLOT_DPI = 900

repo_root = Path().resolve().parents[0]
PLOTS_DIR = os.path.join(repo_root, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

def _safe_name(s: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in str(s))

def save_or_show(fig, out_dir: str | None, filename: str, show: bool = True):
    if out_dir:
        dir = os.path.join(PLOTS_DIR, out_dir)
        os.makedirs(dir, exist_ok=True)
        path = os.path.join(dir, _safe_name(filename))
        fig.savefig(path + ".svg", dpi=PLOT_DPI, )
        fig.savefig(path + ".png", dpi=PLOT_DPI)
    if show:
        plt.show()
    else:
        plt.close(fig)

def load_df(files_dir: str, skip_rows: int):
    files = glob.glob(files_dir + "/*.csv")

    read_opts = dict(
    header=skip_rows, 
    engine="pyarrow",
    dtype_backend="pyarrow",
    )

    dfs = [pd.read_csv(f, **read_opts) for f in files]
    df = pd.concat(dfs, ignore_index=True)
    return df
import matplotlib.pyplot as plt
import os

PLOT_FMT = "png"
PLOT_DPI = 600

def _safe_name(s: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in str(s))

def save_or_show(fig, out_dir: str | None, filename: str, show: bool = True):
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, _safe_name(filename))
        fig.savefig(path + ".svg", dpi=PLOT_DPI, bbox_inches="tight")
        fig.savefig(path + ".png", dpi=PLOT_DPI, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close(fig)
import matplotlib.pyplot as plt

def get_pink_purple_cmap():
    """
    Returns the custom pink–purple colormap used across the project.
    Colors:
      - light pink → hot pink → dark magenta → purple
    """
    colors = ["#FFC0CB", "#FF69B4", "#C71585", "#8B008B"]
    cmap = plt.cm.colors.LinearSegmentedColormap.from_list("pink_purple", colors)
    return cmap

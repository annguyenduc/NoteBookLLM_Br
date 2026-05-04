Title: Quick start guide — Matplotlib 3.10.9 documentation
Source: https://matplotlib.org/stable/users/explain/quick_start.html

---

Matplotlib graphs your data on Figures, each of which can contain one or more Axes, an area where points can be specified in terms of x-y coordinates.

### Parts of a Figure
- **Figure**: The whole figure. Keeps track of child Axes and special Artists.
- **Axes**: The region for plotting data. Includes Axis objects, title, and labels.
- **Axis**: Set the scale and limits, generate ticks and ticklabels.
- **Artist**: Everything visible on the Figure (Text, Line2D, Patch, etc.).

### Coding Styles
- **OO Style (Explicit)**: Explicitly create Figures and Axes. Recommended for complicated plots and reusable scripts.
- **Pyplot Style (Implicit)**: Rely on pyplot to manage Figures and Axes. Convenient for quick interactive work.

### Types of inputs
Plotting functions expect numpy.array or objects that can be passed to numpy.asarray.

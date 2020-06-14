import matplotlib.pyplot as plt
import seaborn as sns

chart_colors = ['#54a1ff', '#7cd8bb', '#cee744', '#f6f964', '#c23cb5', '#7c15c6']

sns.set(rc={'axes.prop_cycle': plt.cycler(color=chart_colors),
            'axes.axisbelow': False,
            'axes.edgecolor': 'lightgrey',
            'axes.facecolor': 'None',
            'axes.grid': False,
            'axes.labelcolor': 'dimgrey',
            'axes.spines.right': False,
            'axes.spines.top': False,
            'figure.facecolor': 'white',
            'figure.figsize': (10, 5),
            'lines.solid_capstyle': 'round',
            'patch.edgecolor': 'w',
            'patch.force_edgecolor': True,
            'text.color': 'dimgrey',
            'xtick.bottom': False,
            'xtick.color': 'dimgrey',
            'xtick.direction': 'out',
            'xtick.top': False,
            'ytick.color': 'dimgrey',
            'ytick.direction': 'out',
            'ytick.left': False,
            'ytick.right': False})

sns.set_context("notebook", rc={"font.size": 16, "axes.titlesize": 20, "axes.labelsize": 18})

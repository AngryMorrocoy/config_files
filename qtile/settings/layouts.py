from libqtile import layout
from settings.themes import colors

layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": colors["color4"][0],
    "border_normal": colors["inactive"][0]
}

layouts = [
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.Stack(**layout_theme, num_stacks=2),
    # layout.Matrix(**layout_theme),
]

floating_layout = layout.Floating()


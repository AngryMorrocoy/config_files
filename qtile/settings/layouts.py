from libqtile import layout
from libqtile.config import Match
from settings.themes import colors

layout_theme = {
    "border_width": 3,
    "margin": 5,
    "border_focus": colors["focused"][0],
    "border_normal": colors["unfocused"][0]
}

layouts = [
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Stack(**layout_theme, num_stacks=2),
    layout.Matrix(**{key:value for key,value in layout_theme.items() if key != "margin"}, margin=0),
]

floating_layout = layout.Floating(float_rules=[
        *layout.Floating.default_float_rules,
        Match(title="Qalculate!"), Match(wm_class="gpick")
    ],
    **{key:value for key,value in layout_theme.items() if key != "margin"})


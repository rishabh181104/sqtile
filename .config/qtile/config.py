from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os

# --- MODIFIERS AND TERMINAL ---
mod = "mod4"  # Super key
mmod = "mod1"  # Alt key
terminal = guess_terminal()  # Default terminal
term = "ghostty"  # Preferred terminal
code = "pycharm-professional"  # Code editor
aicode = "void"  # AI code editor
filemanager = "thunar"  # File manager
music = "bash ~/.config/qtile/scripts/spotify-start.sh"
browser1 = "zen-browser --enable-accelerated-video-decode --enable-hardware-overlays --enable-gpu-rasterization --enable-webrender"  # Browser 1
browser2 = "google-chrome-stable --disable-gpu-vsync --enable-zero-copy --enable-gpu-rasterization --ignore-gpu-blocklist --use-vulkan"  # Browser 2

# --- LOAD PYWAL COLORS ---
colors = []
cache = os.path.expanduser('~/.cache/wal/colors')
with open(cache, 'r') as file:
    for i in range(16):  # Read 16 colors from pywal
        colors.append(file.readline().strip())

# --- KEYBINDINGS ---
keys = [
    # Custom keybinds
    Key([mod], "Return", lazy.spawn(term), desc="Launch preferred terminal"),
    Key([mod], "b", lazy.spawn(browser1), desc="Launch browser 1"),
    Key([mod], "s", lazy.spawn(music), desc="Launch music"),
    Key([mod], "e", lazy.spawn(filemanager), desc="Launch file manager"),
    Key([mod], "p", lazy.spawn(code), desc="Launch code editor"),
    Key([mod], "a", lazy.spawn(aicode), desc="Launch AI code editor"),
    Key([mod, "shift"], "b", lazy.spawn(browser2), desc="Launch browser 2"),
    Key([mod], "j", lazy.screen.prev_group(), desc="Move to left workspace"),
    Key([mod], "k", lazy.screen.next_group(), desc="Move to right workspace"),
    Key([mod, "control"], "w", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    Key([mod, "control"], "s", lazy.window.toggle_minimize(), desc="Toggle minimize"),
    Key([mmod, "control"], "l", lazy.spawn("betterlockscreen -l"), desc="Lock screen"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([], "XF86AudioMedia", lazy.spawn("pavucontrol")),

    # Focus and window movement
    Key([mmod], "h", lazy.layout.left(), desc="Focus left"),
    Key([mmod], "l", lazy.layout.right(), desc="Focus right"),
    Key([mmod], "j", lazy.layout.down(), desc="Focus down"),
    Key([mmod], "k", lazy.layout.up(), desc="Focus up"),
    Key([mod, "shift"], "space", lazy.layout.next(), desc="Focus next window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset window sizes"),
    Key([mod, "control"], "Return", lazy.layout.toggle_split(), desc="Toggle split"),

    # Default keybinds
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch default terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "r", lazy.reload_config(), desc="Reload config"),
    Key([mmod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.spawncmd(), desc="Spawn command prompt"),
]

# VT switching keybinds
for vt in range(1, 8):
    keys.append(
        Key(["control", "mod1"], f"f{vt}", lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"), desc=f"Switch to VT{vt}")
    )

# --- GROUPS WITH NERD FONT ICONS ---
groups = [
    Group("1", label=""),  # Terminal
    Group("2", label=""),  # Browser
    Group("3", label=""),  # Code
    Group("4", label=""),  # Tools
    Group("5", label=""),  # Files
    Group("6", label=""),  # Media
    Group("7", label=""),  # Chat
    Group("8", label=""),  # Containers
    Group("9", label=""),  # Docs
    Group("0", label=""),  # Settings
]

# Group keybindings
for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Move window to group {i.name}"),
        ]
    )

# --- LAYOUTS WITH PYWAL COLORS ---
layouts = [
    layout.Tile(
        border_focus=colors[5],  # Accent color for focused windows
        border_normal=colors[8],  # Gray-like for normal windows
        border_width=2,
        margin=0
    ),
    layout.Columns(
        border_focus=colors[5],  # Accent color for focused windows
        border_normal=colors[8],  # Gray-like for normal windows
        border_width=2,
        margin=0
    ),
]

# --- WIDGET DEFAULTS WITH PYWAL COLORS ---
widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=16,
    padding=8,
    foreground=colors[7],  # Foreground color
    background=colors[0],  # Background color
)
extension_defaults = widget_defaults.copy()

# --- BAR CONFIGURATION WITH PYWAL COLORS ---
screens = [
    Screen(
        bottom=bar.Bar(
            [
                # Left section
                widget.CurrentLayoutIcon(
                    scale=0.7,
                    foreground=colors[3],  # Accent color
                    background=colors[0],  # Background
                    padding=10,
                ),
                widget.Spacer(length=8),
                widget.GroupBox(
                    highlight_method="block",
                    block_highlight_text_color=colors[7],  # Foreground
                    inactive=colors[8],  # Gray-like
                    active=colors[7],  # Foreground
                    this_current_screen_border=colors[5],  # Accent
                    urgent_text=colors[1],  # Red-like
                    rounded=False,
                    padding=10,
                    margin_x=5,
                ),
                widget.Spacer(length=12),
                widget.Prompt(
                    foreground=colors[7],  # Foreground
                    background=colors[0],  # Background
                ),
                # Middle section
                widget.Spacer(length=12),
                widget.WindowName(
                    format="{name}",
                    max_chars=60,
                    foreground=colors[6],  # Accent color
                    padding=10,
                ),
                widget.Spacer(length=12),
                # Right section
                widget.Systray(
                    icon_size=20,
                    padding=10,
                    background=colors[0],  # Background
                ),
                widget.Spacer(length=8),
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    display_format=" {updates}",
                    no_update_string=" 0",
                    update_interval=1800,
                    foreground=colors[2],  # Accent color
                    padding=8,
                ),
                widget.Spacer(length=8),
                widget.CPU(
                    format=" {load_percent}%",
                    foreground=colors[3],  # Accent color
                    padding=8,
                ),
                widget.Spacer(length=8),
                widget.Memory(
                    format=" {MemPercent}%",
                    foreground=colors[5],  # Accent color
                    padding=8,
                ),
                widget.Spacer(length=8),
                widget.Net(
                    format=" {down:.1f}Mbps ↓↑ {up:.1f}Mbps",
                    foreground=colors[4],
                    padding=8,
                    use_bits=True,
                ),
                widget.Spacer(length=8),
                widget.Clock(
                    format=" %H:%M",
                    foreground=colors[6],  # Accent color
                    padding=8,
                ),
                widget.Spacer(length=8),
                widget.Clock(
                    format=" %a %d %b",
                    foreground=colors[2],  # Accent color
                    padding=8,
                ),
                widget.Spacer(length=8),
                widget.Battery(
                    format='{char} {percent:2.0%}',
                    discharge_char='',
                    charge_char='',
                    full_char='',
                    empty_char='',
                    low_percentage=0.15,
                    low_foreground=colors[1],
                    foreground=colors[9],
                    background=colors[0],
                    padding=8,
                    update_interval=10,
                ),
                widget.Spacer(length=8),
                widget.QuickExit(
                    default_text="",
                    countdown_format="{}",
                    foreground=colors[1],  # Red-like
                    padding=10,
                ),
                widget.Spacer(length=8),
            ],
            32,  # Bar height
            margin=[8, 8, 0, 8],  # Margins [top, right, bottom, left]
            background=colors[0],  # Background
            opacity=0.95,
        ),
    ),
]

# --- MOUSE CONFIGURATION ---
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# --- OTHER SETTINGS ---
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
ipc = True
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"

# --- AUTOSTART HOOK ---
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/scripts/autostart.sh"])

# credits to theova/base16-qutebrowser for the original template
# credits to https://github.com/leandwo/qutebrowser-themes/blob/master/themes/onedark.py for modified template

# Keybindings
config.bind("ge", "scroll-to-perc") # In order to be more similiar to helix keybindings
config.bind("l", "tab-next")
config.bind("h", "tab-prev")
config.bind("j", "scroll-px 0 200")
config.bind("k", "scroll-px 0 -200")

# Tabs options
c.tabs.show = "multiple"
c.tabs.position = "bottom"
c.tabs.favicons.scale = 0.8

# Font options
c.fonts.default_size = "12pt"
c.fonts.completion.category = "medium default-size default-family"
c.fonts.hints = "medium default-size default-family"

# Other options
config.load_autoconfig(False)
c.content.javascript.clipboard = "access-paste"
c.url.default_page = "qute://start"
c.url.start_pages = "qute://start"
c.messages.timeout = 4000
c.statusbar.widgets = ["keypress", "search_match", "url", "scroll", "history", "progress"]

##########
# COLORS #
##########

# base16 colors but with variable names that 
# reflect what the color is mainly used for

bg_default          = "#282c34" # main shade
bg_alt              = "#1e222b" # slightly darker than main shade
#bg_alt             = "#3e4451"
# "#545862"
fg_disabled         = "#565c64"
fg_default          = "#ffffff"
fg_faded            = "#abb2bf"
# "#b6bdca"
fg_error            = "#e06c75" # red
# "#d19a66"                     # orange
bg_hint             = "#e5c07b" # yellow
fg_matched_text     = "#98c379" # green
bg_passthrough_mode = "#56b6c2" # teal
bg_insert_mode      = "#61afef" # blue
bg_warning          = "#c678dd" # purple
# "#be5046"                     # dark red

############
# SETTINGS #
############

c.colors.webpage.preferred_color_scheme = "dark"

# Background color of comletion widget
c.colors.completion.even.bg = bg_alt
c.colors.completion.odd.bg = bg_alt
c.colors.completion.category.bg = bg_alt
c.colors.completion.category.border.top = bg_alt
c.colors.completion.category.border.bottom = bg_alt
c.colors.completion.scrollbar.bg = bg_alt

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column
c.colors.completion.fg = fg_faded

# Color of completion widget category headers
c.colors.completion.category.fg = bg_hint

# Colors of the selected completion item
c.colors.completion.item.selected.fg = fg_default
c.colors.completion.item.selected.bg = bg_default
c.colors.completion.item.selected.border.top = bg_default
c.colors.completion.item.selected.border.bottom = bg_default
c.colors.completion.item.selected.match.fg = fg_matched_text

# Foreground color of the matched text in the completion
c.colors.completion.match.fg = fg_matched_text

# Color of the scrollbar handle in the completion view
c.colors.completion.scrollbar.fg = bg_default

# Background color of disabled items in the context menu
c.colors.contextmenu.disabled.bg = bg_alt

# Foreground color of disabled items in the context menu
c.colors.contextmenu.disabled.fg = fg_disabled

# Background color of the context menu. If set to null, the Qt default is used
c.colors.contextmenu.menu.bg = bg_default

# Foreground color of the context menu. If set to null, the Qt default is used
c.colors.contextmenu.menu.fg =  fg_default

# Background color of the context menu’s selected item. If set to null, the Qt default is used
c.colors.contextmenu.selected.bg = bg_alt

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used
c.colors.contextmenu.selected.fg = fg_default

# Background color for the download bar
c.colors.downloads.bar.bg = bg_default

# Color gradient start for download text
c.colors.downloads.start.fg = bg_default

# Color gradient start for download backgrounds
c.colors.downloads.start.bg = bg_insert_mode

# Color gradient end for download text
c.colors.downloads.stop.fg = bg_default

# Color gradient stop for download backgrounds
c.colors.downloads.stop.bg = bg_passthrough_mode

# Foreground color for downloads with errors
c.colors.downloads.error.fg = fg_error

# Colors for hints. Note that you can use a `rgba(...)` value
# for transparency
c.colors.hints.bg = bg_alt
c.colors.hints.fg = fg_faded
c.colors.hints.match.fg = fg_default
c.hints.border = "none"

# Text color for the keyhint widget
c.colors.keyhint.fg = fg_default

# Highlight color for keys to complete the current keychain
c.colors.keyhint.suffix.fg = fg_default

# Background color of the keyhint widget
c.colors.keyhint.bg = bg_default

# Foreground color of an error message
c.colors.messages.error.fg = bg_default

# Background color of an error message
c.colors.messages.error.bg = fg_error

# Border color of an error message
c.colors.messages.error.border = fg_error

# Foreground color of a warning message
c.colors.messages.warning.fg = bg_default

# Background color of a warning message
c.colors.messages.warning.bg = bg_warning

# Border color of a warning message
c.colors.messages.warning.border = bg_warning

# Foreground color of an info message
c.colors.messages.info.fg = fg_default

# Background color of an info message
c.colors.messages.info.bg = bg_default

# Border color of an info message
c.colors.messages.info.border = bg_default

# Foreground color for prompts
c.colors.prompts.fg = fg_default

# Border used around UI elements in prompts
c.colors.prompts.border = bg_default

# Background color for prompts
c.colors.prompts.bg = bg_default

# Background color for the selected item in filename prompts
c.colors.prompts.selected.bg = bg_alt

# Foreground color for the selected item in filename prompts
c.colors.prompts.selected.fg = fg_default

# Normal mode statusbar colors
c.colors.statusbar.normal.fg = fg_default
c.colors.statusbar.normal.bg = bg_default

# Insert mode statusbar colors
c.colors.statusbar.insert.fg = bg_default

# Background color of the statusbar in insert mode
c.colors.statusbar.insert.bg = bg_insert_mode

# Foreground color of the statusbar in passthrough mode
c.colors.statusbar.passthrough.fg = bg_default

# Background color of the statusbar in passthrough mode
c.colors.statusbar.passthrough.bg = bg_passthrough_mode

# Foreground color of the statusbar in private browsing mode
c.colors.statusbar.private.fg = bg_default

# Background color of the statusbar in private browsing mode
c.colors.statusbar.private.bg = bg_default

# Foreground color of the statusbar in command mode
c.colors.statusbar.command.fg = fg_default

# Background color of the statusbar in command mode
c.colors.statusbar.command.bg = bg_default

# Foreground color of the statusbar in private browsing + command mode
c.colors.statusbar.command.private.fg = fg_default

# Background color of the statusbar in private browsing + command mode
c.colors.statusbar.command.private.bg = bg_default

# Foreground color of the statusbar in caret mode
c.colors.statusbar.caret.fg = bg_default

# Background color of the statusbar in caret mode
c.colors.statusbar.caret.bg = bg_warning

# Foreground color of the statusbar in caret mode with a selection
c.colors.statusbar.caret.selection.fg = bg_default

# Background color of the statusbar in caret mode with a selection
c.colors.statusbar.caret.selection.bg = bg_insert_mode

# Background color of the progress bar
c.colors.statusbar.progress.bg = bg_insert_mode

# Default foreground color of the URL in the statusbar
c.colors.statusbar.url.fg = fg_default

# Foreground color of the URL in the statusbar on error
c.colors.statusbar.url.error.fg = fg_error

# Foreground color of the URL in the statusbar for hovered links
c.colors.statusbar.url.hover.fg = fg_default

# Foreground color of the URL in the statusbar on successful load
# (http)
c.colors.statusbar.url.success.http.fg = bg_passthrough_mode

# Foreground color of the URL in the statusbar on successful load
# (https)
c.colors.statusbar.url.success.https.fg = fg_default

# Foreground color of the URL in the statusbar when there's a warning
c.colors.statusbar.url.warn.fg = bg_warning

# Background color of the tab bar
c.colors.tabs.bar.bg = bg_default

# Color gradient start for the tab indicator
c.colors.tabs.indicator.start = bg_insert_mode

# Color gradient end for the tab indicator
c.colors.tabs.indicator.stop = bg_passthrough_mode

# Color for the tab indicator on errors
c.colors.tabs.indicator.error = fg_error

# Background color of unselected tabs
c.colors.tabs.odd.bg = bg_alt
c.colors.tabs.even.bg = bg_alt

# Foreground color of unselected tabs
c.colors.tabs.even.fg = fg_faded
c.colors.tabs.odd.fg = fg_faded

# Background color of pinned unselected tabs
c.colors.tabs.pinned.even.bg = bg_passthrough_mode
c.colors.tabs.pinned.odd.bg = fg_matched_text

# Foreground color of pinned unselected tabs
c.colors.tabs.pinned.even.fg = bg_alt
c.colors.tabs.pinned.odd.fg = bg_alt

# Background color of pinned selected tabs
c.colors.tabs.pinned.selected.even.bg = bg_default
c.colors.tabs.pinned.selected.odd.bg = bg_default

# Foreground color of pinned selected tabs
c.colors.tabs.pinned.selected.even.fg = fg_default
c.colors.tabs.pinned.selected.odd.fg = fg_default

# Foreground color of selected tabs
c.colors.tabs.selected.odd.fg = fg_default
c.colors.tabs.selected.even.fg = fg_default

# Background color of selected tabs
c.colors.tabs.selected.odd.bg = bg_default
c.colors.tabs.selected.even.bg = bg_default

# Background color for webpages if unset (or empty to use the theme's
# color)
# c.colors.webpage.bg = bg_default
#

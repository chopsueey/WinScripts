# ----------------------------------------------------------------------------
# hook-ttkthemes.py
#
# This hook is necessary to bundle the data files (themes, images) used by
# the ttkthemes library, which are not automatically detected by PyInstaller.
# It uses the collect_data_files utility to find all non-code files in the
# ttkthemes package and adds them to the 'datas' list for bundling.
# ----------------------------------------------------------------------------

from PyInstaller.utils.hooks import collect_data_files

# Collect all data files from the 'ttkthemes' package.
# This includes the 'gif', 'png', and 'themes' directories, along with all
# their contents (.tcl, .gif, .png files, etc.).
datas = collect_data_files('ttkthemes')

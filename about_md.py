import flet as ft
from calibrations import *

about_md = f"""
# About

## Version
{TOOL_NAME} {MAJOR_VERSION}.{MINOR_VERSION}

## Release notes


### 0.2
- Another release!

### 0.1
- Second release

### 0.0
- First release of Bike Maintenance Tool
-
-
-
-
-
-
-
-
-
-



"""

about_md = ft.Markdown(
    about_md,
)
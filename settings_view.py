import flet as ft
from navigation_rail import *
from calibrations import *

def dropdown_changed(e):
    e.page.update()
    e.page.client_storage.set("distance_gain", 2)
    print('Unit changed')



metric_system = ft.Dropdown(
    on_change=dropdown_changed,
    value="km",
    label="Unit",
    options=[
        ft.dropdown.Option("km"),
        ft.dropdown.Option("miles"),
    ],
    width=200,
)



settings_row = ft.Column([ft.Text('Unit distance'), metric_system])




import flet as ft
from navigation_rail import *
from calibrations import *

def dropdown_changed(e):
    e.page.update()
    if distance_unit_dropdown.value == 'km':
        e.page.client_storage.set('bmt.distance_unit', 'km')
    elif distance_unit_dropdown.value == 'miles':
        e.page.client_storage.set('bmt.distance_unit', 'miles')


distance_unit_dropdown = ft.Dropdown(
    on_change=dropdown_changed,
    value="km",
    label="Unit",
    options=[
        ft.dropdown.Option("km"),
        ft.dropdown.Option("miles"),
    ],
    width=200,
)

def clear_database(e):
    alert_dialog = databaseDialog(e.page)
    e.page.dialog = alert_dialog
    alert_dialog.open = True
    e.page.update()


class databaseDialog(ft.AlertDialog):
    def __init__(self, page):
        super().__init__(
            modal=False,
            title=ft.Text("Warning"),
            content=ft.Text("Are you sure you want to clear the database??"),
            actions=[
                ft.TextButton("Yes", on_click=self.yes_clicked),
                ft.TextButton("No", on_click=self.no_clicked),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page = page
        self.download = False

    def yes_clicked(self, e):
        # Redirect to website to download new version
        print('databaseDialog: clear database')
        e.page.client_storage.clear()
        self.open = False
        self.page.update()

    def no_clicked(self, e):
        print("databaseDialog: don't clear database")
        self.open = False
        self.page.update()

settings_row = ft.Column([ft.Text('Unit distance'),
                          distance_unit_dropdown,
                          ft.Text('Clear database'),
                          ft.OutlinedButton("Clear database", on_click=clear_database)])




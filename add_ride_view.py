import flet as ft
import datetime


def change_date(e):
    date_field.value = f"Date: {date_picker.value.day:02}-{date_picker.value.month:02}-{date_picker.value.year}"
    e.page.update()

def date_picker_dismissed(e):
    print(f"Date picker dismissed, value is {date_picker.value}")

ride_name = ft.TextField(label="Ride name")
ride_distance = ft.TextField(label="Distance")
date_picker = ft.DatePicker(
    on_change=change_date,
    on_dismiss=date_picker_dismissed,
    first_date=datetime.datetime(2023, 10, 1),
    last_date=datetime.datetime(2024, 10, 1),
)

date_button = ft.ElevatedButton(
    "Pick date",
    icon=ft.icons.CALENDAR_MONTH,
    on_click=lambda _: date_picker.pick_date(),
)
date_field = ft.Text('Date: ', width = 150)
bike_dropdown = ft.Dropdown(
        label='Bike',
        options=[
            ft.dropdown.Option("Bike 1"),
            ft.dropdown.Option("Bike 2"),
            ft.dropdown.Option("Bike 3"),
        ],
    )

add_ride_button = ft.ElevatedButton("Add ride")
cancel_add_ride_button = ft.ElevatedButton("Cancel")


add_ride_row = ft.Column([ft.Text('Add bike ride', size=20),
                          ride_name,
                          ride_distance,
                          ft.Row([date_field, date_button]),
                          bike_dropdown,
                          ft.Row([add_ride_button, cancel_add_ride_button])])
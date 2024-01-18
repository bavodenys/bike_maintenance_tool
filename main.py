import flet as ft
from functions import *
from navigation_rail import *
from update_dialog import *
from calibrations import *
from about_md import *
from settings_view import *


AppBar = ft.AppBar(
        title=ft.Text(f"{TOOL_NAME} {MAJOR_VERSION}.{MINOR_VERSION}"),
        center_title=True,
        bgcolor=ft.colors.BLUE,
    )


def main(page: ft.Page):
    page.title = f"{TOOL_NAME} {MAJOR_VERSION}.{MINOR_VERSION}"
    page.client_storage.set("distance_gain", 1)
    rides_text = ft.Ref[ft.Text]()

    # Check for update of the tool
    if check_for_update(MAJOR_VERSION, MINOR_VERSION):
        alert_dialog = UpdateDialog(page)
        page.dialog = alert_dialog
        alert_dialog.open = True
        page.update()

    def route_changed(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",

                [
                    AppBar,
                    ft.Row(
                        [
                            MyNavigationRail(0),
                            ft.VerticalDivider(width=1),
                            ft.Column([ft.Text('Home')], alignment=ft.MainAxisAlignment.START, expand=True),
                        ],
                        expand=True,
                    ),
                ],
            )
        )
        if page.route == "/rides":
            page.views.append(
                ft.View(
                    "/rides",

                    [
                        AppBar,
                        ft.Row(
                            [
                                MyNavigationRail(1),
                                ft.VerticalDivider(width=1),
                                ft.Column([ft.Text(ref=rides_text, value=f'Rides: distance {distance_conversion(5, page.client_storage.get("distance_gain"))} {metric_system.value}')], alignment=ft.MainAxisAlignment.START, expand=True),
                            ],
                            expand=True,
                        ),
                    ],
                )
            )
        if page.route == "/bikes":
            page.views.append(
                ft.View(
                    "/bikes",

                    [
                        AppBar,
                        ft.Row(
                            [
                                MyNavigationRail(2),
                                ft.VerticalDivider(width=1),
                                ft.Column([ft.Text('Bikes')], alignment=ft.MainAxisAlignment.START, expand=True),
                            ],
                            expand=True,
                        ),
                    ],
                )
            )
        if page.route == "/help":
            page.views.append(
                ft.View(
                    "/help",

                    [
                        AppBar,
                        ft.Row(
                            [
                                MyNavigationRail(3),
                                ft.VerticalDivider(width=1),
                                ft.Column([ft.Text('Help')], alignment=ft.MainAxisAlignment.START, expand=True),
                            ],
                            expand=True,
                        ),
                    ],
                )
            )
        if page.route == "/settings":
            page.views.append(
                ft.View(
                    "/settings",

                    [
                        AppBar,
                        ft.Row(
                            [
                                MyNavigationRail(4),
                                ft.VerticalDivider(width=1),
                                ft.Column([settings_row], alignment=ft.MainAxisAlignment.START, expand=True),
                            ],
                            expand=True,
                        ),
                    ],
                )
            )
        if page.route == "/about":
            page.views.append(
                ft.View(
                    "/about",

                    [
                        AppBar,
                        ft.Row(
                            [
                                MyNavigationRail(5),
                                ft.VerticalDivider(width=1),
                                ft.Column([about_md], alignment=ft.MainAxisAlignment.START, scroll=True),
                            ],
                            expand=True,
                        ),
                    ],
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_changed
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
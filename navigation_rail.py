import flet as ft

class MyNavigationRail(ft.NavigationRail):
    def __init__(self, selected_index):
        super().__init__(
            selected_index=selected_index,
            label_type=ft.NavigationRailLabelType.ALL,
            extended=False,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME, label="HOME"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="RIDES",
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="BIKES",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.HELP_OUTLINE,
                    selected_icon_content=ft.Icon(ft.icons.HELP),
                    label_content=ft.Text("Help"),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),

                ft.NavigationRailDestination(
                    icon=ft.icons.INFO_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.INFO),
                    label_content=ft.Text("About"),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.EXIT_TO_APP,
                    selected_icon_content=ft.Icon(ft.icons.EXIT_TO_APP_OUTLINED),
                    label_content=ft.Text("Exit"),

                ),
            ],
            on_change=lambda e: self.menu_item_clicked(e.control.selected_index),
        )

    def menu_item_clicked(self, index):
        if index == 0:
            self.page.go("/")
        elif index == 1:
            self.page.go("/rides")
        elif index == 2:
            self.page.go("/bikes")
        elif index == 3:
            self.page.go("/help")
        elif index == 4:
            self.page.go("/settings")
        elif index == 5:
            self.page.go("/about")
        elif index == 6:
            self.page.go("/exit")
        else:
            pass
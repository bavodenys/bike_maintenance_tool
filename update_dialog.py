import flet as ft

class UpdateDialog(ft.AlertDialog):
    def __init__(self, page):
        super().__init__(
            modal=False,
            title=ft.Text("Update"),
            content=ft.Text("A new version is available! Download now?"),
            actions=[
                ft.TextButton("Yes", on_click=self.yes_clicked),
                ft.TextButton("No", on_click=self.no_clicked),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page = page

    def yes_clicked(self, e):
        # Redirect to website to download new version
        print('UpdateDialog: yes clicked')
        self.open = False
        self.page.update()

    def no_clicked(self, e):
        print('UpdateDialog: no clicked')
        self.open = False
        self.page.update()

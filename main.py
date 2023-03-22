#MUY IMPORTANTE
#https://github.com/flet-dev/flet/discussions/644


#Importing Libs
import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors



def main(page: ft.Page):
    def cambiar(self):
        if page.navigation_bar.selected_index == 0:
            print("Automatic")
        if page.navigation_bar.selected_index == 1:
            print("Album")
        if page.navigation_bar.selected_index == 2:
            print("manual")


    page.title = "MyTag"


    #The Navigation bar (It always be in the botton, no matter the position in code)
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=cambiar ,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Autom. Song Recognition"),
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Album Reconition"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Manual",
            ),
        ],
    )

    page.add(automaticDiv)

ft.app(target=main, port=8888)


""""
import flet as ft

def main(page: ft.Page):
    page.title = "MyTag"
    page.scroll = "adaptive"
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Automatic song recognition (Recommended)",
                icon=ft.icons.SETTINGS,
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Album recognition",
                icon=ft.icons.SETTINGS,
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Modify tags manually",
                icon=ft.icons.SEARCH,
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
        ],
        expand=1,
    )

    page.add(t)

ft.app(target=main, port=8888)
"""
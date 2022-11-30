import requests
import wikipedia
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("frontend.kv")


class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and first image url
        page = wikipedia.page(query, auto_suggest=False)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # Download the image (use browser header to avoid 403)
        headers = {"User-Agent": "Mozilla/5.0"}
        req = requests.get(self.get_image_link(), headers=headers, timeout=10)
        imagepath = "files/image.jpg"
        with open(imagepath, "wb") as file:
            file.write(req.content)
        return imagepath

    def set_image(self):
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()

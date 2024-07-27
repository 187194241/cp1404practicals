from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        labels = ["label1", "label2", "label3", "label4"]
        for label in labels:
            temp_label = Label(text=label)
            self.root.ids.main.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()

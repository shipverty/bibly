
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder 
from kivy.uix.widget import Widget
from datetime import datetime
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, Property, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.checkbox import CheckBox
from bs4 import BeautifulSoup
import sys
import requests
b = []
k = []
Builder.load_string('''
<Start>:
	BoxLayout:
		Button:
			padding:.2,.2
			size_hint:.5,.2
			text: "Бытие"
			on_press:root.manager.current = "bib"
<Biblia>:
	BoxLayout:
		id:glav
		orientation: "vertical"
		ScrollView:
			canvas.before:
		        Color:
		            rgba: .46,.44,.44,1
		        Rectangle:
		            pos: self.pos
		            size: self.size
			bar_width:4
			id: lab
			size:self.width, 1
			do_scroll_y:True
			do_scroll_x:False
			Label:
				text:root.t
				font_size:25
				size_hint_y:None
				size_hint_x: 1
				text_size: self.width, None
				height:self.texture_size[1]
		BoxLayout:
			size_hint_y:.2
			BoxLayout:
				orientation:"vertical"
				size_hint_x:.2
				Button:
					text:"Назад"
					on_release:root.back()
				Button:
					id:loads
					text:"Загрузить"
					on_release:root.scrop()
			BoxLayout:
				ScrollView:
					do_scroll_y:False
					do_scroll_x:True
					size_hint_y:.3
					size_hint_x:.8
					GridLayout:
						id:box
						rows:1
						size:self.width, .4
						width: self.minimum_width
						size_hint_x:None
				



	''')


class Start(Screen):
	def go():
		pass
class Biblia(Screen):
	t = StringProperty()
	def back(self):
		sm.current = "start"
	def t1(self, instance):
		a = instance.text

		self.t = str(k[int(a)-1])
	def scrop(self):
		self.ids.loads.disabled = True
		for i in range(len(b)):
			but = self.ids.box.add_widget(Button(text=str(i+1), id=str(i), on_press=self.t1, size_hint_x = None))


sm = ScreenManager()
sm.add_widget(Start(name="start"))
sm.add_widget(Biblia(name="bib"))
def scrosp():
	global b
	s = requests.Session()
	a = s.get("http://bibliya-online.ru/kniga-bytiya-chitat-onlayn/").text
	soup = BeautifulSoup(a, "html.parser")
	p = soup.find("table", id="chapter").findAll("a")
	for i in range(len(p)):
		c = p[i].get("href")
		b.append(c)
	for i in range(len(b)):
		n = ""
		a = s.get(b[i]).text
		soup = BeautifulSoup(a, "html.parser")
		p = soup.findAll("div")[8].findAll("p")
		for j in range(len(p)):
			if j==0:
				pass
			else:

				global n
				n = n + p[j].text + "\n"

		k.append(n)
scrosp()
class MyApp(App):
	def build(self):
		sm.current = "start"
		return(sm)
if __name__ == "__main__":
	MyApp().run() 
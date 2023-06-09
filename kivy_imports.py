import kivy
# kivy.require("1.9.1")
kivy.require("2.0.0")

from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

# basics
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.core.window import Window

# utlils
# from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.screenmanager import ScreenManager, Screen

# ui/ux
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from kivy.uix.actionbar import ActionBar
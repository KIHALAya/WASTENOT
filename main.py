
"""
This file contains the main application code for the WASTENOT app.

The WASTENOT app is built using the KivyMD framework and utilizes Firebase for authentication.

The main functionality of the app includes a sign-up screen, a login screen, and a home screen.

Classes:
- wastenotApp: The main application class that inherits from MDApp and builds the app.

Methods:
- build: Builds the app by creating and configuring the screen manager and adding the necessary screens.
- on_start: Initializes the Firebase Admin SDK and registers custom fonts.

"""

from kivymd.app import MDApp
from View.Screens.SignUp.signup import SignupScreen
from View.Screens.logIn.login import LoginScreen
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core.text import LabelBase
import firebase_admin
from firebase_admin import credentials

# Set the window size
Window.size = (310, 580)

# Load the kv files for the login and signup screens
Builder.load_file('View/Screens/logIn/login.kv')
Builder.load_file('View/Screens/SignUp/signup.kv')

class wastenotApp(MDApp):
    def build(self):
        """
        Builds the app by creating and configuring the screen manager and adding the necessary screens.

        Returns:
        screen_manager (ScreenManager): The configured screen manager for the app.
        """
        self.theme_cls.primary_palette = 'White'
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('View/Screens/Home/home.kv'))
        screen_manager.add_widget(Builder.load_file('View/Screens/Dashboard/dash.kv'))
        screen_manager.add_widget(SignupScreen(name='signup'))
        screen_manager.add_widget(LoginScreen(name='login'))
        return screen_manager
    
    def on_start(self):
        """
        Initializes the Firebase Admin SDK and registers custom fonts.
        """
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate("C:\\Users\\HP\\Documents\\WASTENOT\\credentials.json")  
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://wastenot-930c6-default-rtdb.firebaseio.com/'})
        
        # Register custom fonts
        LabelBase.register(name="BPoppins", fn_regular="assets\\fonts\\Poppins-SemiBold.ttf")
        LabelBase.register(name="MPoppins", fn_regular="assets\\fonts\\Poppins-Medium.ttf")

if __name__ == '__main__':
    wastenotApp().run()

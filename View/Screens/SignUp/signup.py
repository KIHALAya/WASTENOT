
import firebase_admin
from firebase_admin import credentials, auth
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton
from kivy.properties import ObjectProperty

class SignupScreen(Screen):
    """
    The SignupScreen class represents the screen for user sign up.

    Attributes:
        email (ObjectProperty): ObjectProperty for the email text field.
        password (ObjectProperty): ObjectProperty for the password text field.
        SU_error_label (ObjectProperty): ObjectProperty for the error label.

    Methods:
        create_user(email, password): Creates a new user with the given email and password.
        signup(): Handles the sign up process when the sign up button is pressed.
    """

    email = ObjectProperty(None)
    password = ObjectProperty(None)
    SU_error_label = ObjectProperty(None)

    def create_user(self, email, password):
        """
        Creates a new user with the given email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the user is created successfully, False otherwise.
        """
        try:
            user = auth.create_user(email=email, password=password)
            return True
        except Exception as e:
            return False

    def signup(self):
        """
        Handles the sign up process when the sign up button is pressed.
        Checks if the email and password fields are not empty.
        Calls the create_user method to create a new user.
        Updates the screen based on the result of the sign up process.
        """
        if self.ids.email.text != "" and self.ids.password.text != "":
            email = self.ids.email.text
            password = self.ids.password.text
            result = self.create_user(email, password)
            print(result)
            if result:
                self.manager.transition.direction = "left"
                self.manager.current = "dashboard"
                self.ids.SU_error_label.text = "Signed up successfully!"
            else:
                self.ids.SU_error_label.text = "Invalid email or password"
        else:
            self.ids.SU_error_label.text = "Please fill in all fields"







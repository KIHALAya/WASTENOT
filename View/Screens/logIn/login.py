
import firebase_admin
from firebase_admin import credentials, auth
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton
from kivy.properties import ObjectProperty


class LoginScreen(Screen):
    """
    The LoginScreen class represents the screen for user login.

    Attributes:
        email (ObjectProperty): ObjectProperty for the email text field.
        password (ObjectProperty): ObjectProperty for the password text field.
        error_label (ObjectProperty): ObjectProperty for the error label.

    Methods:
        verify_credentials: Verifies the user's credentials by checking if the email and password are valid.
        login: Handles the login process by checking the entered credentials and transitioning to the dashboard screen if valid.
    """

    email = ObjectProperty(None)
    password = ObjectProperty(None)
    SI_error_label = ObjectProperty(None)

    def verify_credentials(self, email, password):
        """
        Verifies the user's credentials by checking if the email and password are valid.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        try:
            user = auth.get_user_by_email(email)
            user = auth.get_user_by_email_and_password(email, password)
            return True
        
        except Exception as e:
            return False

    def login(self):
        """
        Handles the login process by checking the entered credentials and transitioning to the dashboard screen if valid.
        Displays an error message if the credentials are invalid or if any field is empty.
        """
        if self.ids.email.text != "" and self.ids.password.text != "":
            email = self.ids.email.text
            password = self.ids.password.text
            result = self.verify_credentials(email, password)

            if result:
                self.manager.transition.direction = "left"
                self.manager.current = "dashboard"
            else:
                self.ids.SI_error_label.text = "Invalid email or password"
        else:
            self.ids.SI_error_label.text = "Please fill in all fields"






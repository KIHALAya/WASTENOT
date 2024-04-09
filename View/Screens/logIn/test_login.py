import unittest
from unittest.mock import patch
from login import LoginScreen

class TestLoginScreen(unittest.TestCase):
    def setUp(self):
        self.login_screen = LoginScreen()

    def test_verify_credentials_valid(self):
        # Mock the auth.get_user_by_email method to return a user
        with patch('firebase_admin.auth.get_user_by_email') as mock_get_user:
            mock_get_user.return_value = True
            result = self.login_screen.verify_credentials("test@example.com", "password")
            self.assertTrue(result)

    def test_verify_credentials_invalid(self):
        # Mock the auth.get_user_by_email method to raise an exception
        with patch('firebase_admin.auth.get_user_by_email') as mock_get_user:
            mock_get_user.side_effect = Exception("Invalid email")
            result = self.login_screen.verify_credentials("test@example.com", "password")
            self.assertFalse(result)

    def test_login_valid_credentials(self):
        # Mock the verify_credentials method to return True
        with patch.object(LoginScreen, 'verify_credentials', return_value=True):
            self.login_screen.ids.email.text = "test@example.com"
            self.login_screen.ids.password.text = "password"
            self.login_screen.login()
            self.assertEqual(self.login_screen.manager.transition.direction, "left")
            self.assertEqual(self.login_screen.manager.current, "dashboard")

    def test_login_invalid_credentials(self):
        # Mock the verify_credentials method to return False
        with patch.object(LoginScreen, 'verify_credentials', return_value=False):
            self.login_screen.ids.email.text = "test@example.com"
            self.login_screen.ids.password.text = "password"
            self.login_screen.login()
            self.assertEqual(self.login_screen.ids.error_label.text, "Invalid email or password")

    def test_login_empty_fields(self):
        self.login_screen.ids.email.text = ""
        self.login_screen.ids.password.text = ""
        self.login_screen.login()
        self.assertEqual(self.login_screen.ids.error_label.text, "Please fill in all fields")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from kivy.uix.screenmanager import ScreenManager
from login import LoginScreen

class TestLoginScreen(unittest.TestCase):
    def setUp(self):
        self.screen_manager = ScreenManager()
        self.login_screen = LoginScreen()
        self.screen_manager.add_widget(self.login_screen)

    def test_verify_credentials_valid(self):
        with patch('firebase_admin.auth.get_user_by_email') as mock_get_user_by_email, \
             patch('firebase_admin.auth.get_user_by_email_and_password') as mock_get_user_by_email_and_password:
            mock_get_user_by_email.return_value = True
            mock_get_user_by_email_and_password.return_value = True

            result = self.login_screen.verify_credentials("test@example.com", "password")

            self.assertTrue(result)

    def test_verify_credentials_invalid(self):
        with patch('firebase_admin.auth.get_user_by_email') as mock_get_user_by_email, \
             patch('firebase_admin.auth.get_user_by_email_and_password') as mock_get_user_by_email_and_password:
            mock_get_user_by_email.side_effect = Exception("Invalid email")

            result = self.login_screen.verify_credentials("test@example.com", "password")

            self.assertFalse(result)

    def test_login_valid_credentials(self):
        self.login_screen.ids.email.text = "test@example.com"
        self.login_screen.ids.password.text = "password"

        with patch.object(self.login_screen.manager, 'transition') as mock_transition:
            self.login_screen.login()

            self.assertEqual(mock_transition.direction, "left")
            self.assertEqual(self.login_screen.manager.current, "dashboard")
            self.assertEqual(self.login_screen.ids.error_label.text, "")

    def test_login_invalid_credentials(self):
        self.login_screen.ids.email.text = "test@example.com"
        self.login_screen.ids.password.text = "wrong_password"

        with patch.object(self.login_screen.manager, 'transition') as mock_transition:
            self.login_screen.login()

            self.assertNotEqual(mock_transition.direction, "left")
            self.assertNotEqual(self.login_screen.manager.current, "dashboard")
            self.assertEqual(self.login_screen.ids.error_label.text, "Invalid email or password")

    def test_login_empty_fields(self):
        self.login_screen.ids.email.text = ""
        self.login_screen.ids.password.text = ""

        with patch.object(self.login_screen.manager, 'transition') as mock_transition:
            self.login_screen.login()

            self.assertNotEqual(mock_transition.direction, "left")
            self.assertNotEqual(self.login_screen.manager.current, "dashboard")
            self.assertEqual(self.login_screen.ids.error_label.text, "Please fill in all fields")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from login import LoginScreen

class TestLoginScreen(unittest.TestCase):
    def setUp(self):
        self.login_screen = LoginScreen()

    def test_verify_credentials_valid(self):
        with patch('firebase_admin.auth.get_user_by_email') as mock_get_user_by_email:
            mock_get_user_by_email.return_value = True
            result = self.login_screen.verify_credentials("test@example.com", "password")
            self.assertTrue(result)

    def test_verify_credentials_invalid(self):
        with patch('firebase_admin.auth.get_user_by_email') as mock_get_user_by_email:
            mock_get_user_by_email.side_effect = Exception("Invalid email")
            result = self.login_screen.verify_credentials("test@example.com", "password")
            self.assertFalse(result)

    def test_login_valid_credentials(self):
        self.login_screen.ids.email.text = "test@example.com"
        self.login_screen.ids.password.text = "password"
        with patch.object(self.login_screen.manager, 'transition') as mock_transition:
            self.login_screen.login()
            mock_transition.assert_called_once_with(direction="left")
            self.assertEqual(self.login_screen.manager.current, "dashboard")

    def test_login_invalid_credentials(self):
        self.login_screen.ids.email.text = "test@example.com"
        self.login_screen.ids.password.text = "wrong_password"
        self.login_screen.login()
        self.assertEqual(self.login_screen.ids.error_label.text, "Invalid email or password")

    def test_login_empty_fields(self):
        self.login_screen.login()
        self.assertEqual(self.login_screen.ids.error_label.text, "Please fill in all fields")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from login import LoginScreen

class TestLoginScreen(unittest.TestCase):
    def setUp(self):
        self.login_screen = LoginScreen()

    def test_verify_credentials_valid(self):
        with patch('firebase_admin.auth.get_user_by_email') as mock_get_user_by_email, \
             patch('firebase_admin.auth.get_user_by_email_and_password') as mock_get_user_by_email_and_password:
            mock_get_user_by_email.return_value = True
            mock_get_user_by_email_and_password.return_value = True

            result = self.login_screen.verify_credentials("test@example.com", "password")

            self.assertTrue(result)

    def test_verify_credentials_invalid(self):
        with patch('firebase_admin.auth.get_user_by_email') as mock_get_user_by_email, \
             patch('firebase_admin.auth.get_user_by_email_and_password') as mock_get_user_by_email_and_password:
            mock_get_user_by_email.side_effect = Exception("Invalid email")

            result = self.login_screen.verify_credentials("test@example.com", "password")

            self.assertFalse(result)

    def test_login_valid_credentials(self):
        self.login_screen.ids.email.text = "test@example.com"
        self.login_screen.ids.password.text = "password"

        with patch.object(self.login_screen.manager, 'transition') as mock_transition:
            self.login_screen.login()

            self.assertEqual(mock_transition.direction, "left")
            self.assertEqual(self.login_screen.manager.current, "dashboard")
            self.assertEqual(self.login_screen.ids.error_label.text, "")

    def test_login_invalid_credentials(self):
        self.login_screen.ids.email.text = "test@example.com"
        self.login_screen.ids.password.text = "wrong_password"

        with patch.object(self.login_screen.manager, 'transition') as mock_transition:
            self.login_screen.login()

            self.assertNotEqual(mock_transition.direction, "left")
            self.assertNotEqual(self.login_screen.manager.current, "dashboard")
            self.assertEqual(self.login_screen.ids.error_label.text, "Invalid email or password")

    def test_login_empty_fields(self):
        self.login_screen.ids.email.text = ""
        self.login_screen.ids.password.text = ""

        with patch.object(self.login_screen.manager, 'transition') as mock_transition:
            self.login_screen.login()

            self.assertNotEqual(mock_transition.direction, "left")
            self.assertNotEqual(self.login_screen.manager.current, "dashboard")
            self.assertEqual(self.login_screen.ids.error_label.text, "Please fill in all fields")

if __name__ == '__main__':
    unittest.main()
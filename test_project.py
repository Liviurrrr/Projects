import student_system
from student_system import dashboard, exit_codes, student_hand_book
from unittest.mock import patch
import unittest

class testStudetnSystem(unittest.TestCase):

    # Test startup
    @patch("student_system.input", side_effect=["1", "olivia.amos@myschool.edu"])
    def test_startup_choice_1_login(self, mock_input):
        login_email = student_system.startup()
        self.assertEqual(login_email, "olivia.amos@myschool.edu")

    @patch("student_system.input", side_effect=["2"])
    @patch("student_system.signup")
    def test_startup_choice_2_signup(self, mock_signup, mock_input):
        student_system.startup()
        mock_signup.assert_called_once()

    @patch("student_system.input", side_effect=["3"])
    def test_startup_choice_3_exit(self, mock_input):
        with self.assertRaises(SystemExit) as test:
            student_system.startup()
            self.assertEqual(test.exception, "Exiting the system...")

    # Test dashboard
    @patch("student_system.input", side_effect=["1"])
    @patch("student_system.student_info")
    def test_dashboard_choice_1_student_info(self, mock_student_info, mock_input):
        dashboard("first.last@myschool.edu")
        mock_student_info.assert_called_once_with("first.last@myschool.edu")

    @patch("student_system.input", side_effect=["2"])
    @patch("student_system.student_hand_book")
    def test_dashboard_choice_2_student_hand_book(self, mock_student_hand_book, mock_input):
        dashboard("first.last@myschool.edu")
        mock_student_hand_book.assert_called_once_with("first.last@myschool.edu")

    @patch("student_system.input", side_effect=["3"])
    @patch("student_system.main")
    def test_dashboard_choice_1_student_info(self, mock_main_redirect, mock_input):
        dashboard("first.last@myschool.edu")
        mock_main_redirect.assert_called_once()

    # Exit codes
    @patch("student_system.input", side_effect=["d"])
    @patch("student_system.dashboard")
    def test_exit_codes(self, mock_dashboard, mock_input):
        exit_codes("first.last@myschool.edu")
        mock_dashboard.assert_called_once_with("first.last@myschool.edu")

    @patch("student_system.input", side_effect=["x", "y"])
    def test_exit_codes(self, mock_input):
        with self.assertRaises(SystemExit) as test:
            student_system.exit_codes("first.last@myschool.edu")
            self.assertEqual(test.exception, "Exiting the system...")

    @patch("student_system.input", side_effect=["x", "y"])
    def test_student_hand_book(self, mock_input):
        try:
            self.assertRaises(FileNotFoundError, student_hand_book("first.last@myschool.edu"))
        except SystemExit:
            pass

if __name__ == "__main__":
    unittest.main()
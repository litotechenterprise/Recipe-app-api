from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # Test creating email a new user with an emilment successful
        email = 'Lito1314@gmail.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test The email for a new User is normalized """
        email = 'test@YAHOOO.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test Create New SuperUser """
        user = get_user_model().objects.create_superuser(
            'Pabs1314@gmail.com',
            'Dtgfu1314'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

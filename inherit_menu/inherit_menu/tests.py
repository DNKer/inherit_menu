from django.test import TestCase, Client


class TestStaticURL(TestCase):
    def test_homepage(self):
        """Тестирование главной страницы."""
        guest_client = Client()

    def setUp(self):
        """ Неавторизованый клиент. """
        self.guest_client = Client()

    def test_home_url_exists_at_desired_location(self):
        """Страница / доступна любому пользователю."""
        try:
            response = self.guest_client.get('/')
        except Exception as e:
            assert False, f'''Страница `/` работает неправильно. Ошибка: `{e}`'''
        if response.status_code in (301, 302):
            self.assertEqual(
                        response.status_code,
                        200,
                        'Страница `/posts/<post_id>/edit/` не найдена, '
                        'проверьте этот адрес в *urls.py*'
        )

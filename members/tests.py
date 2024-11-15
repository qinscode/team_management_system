from django.test import TestCase, Client
from django.urls import reverse
from .models import TeamMember

class TeamMemberTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.member = TeamMember.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            role="Developer",
            bio="Test bio"
        )

    def test_member_list_view(self):
        response = self.client.get(reverse('member-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")

    def test_member_detail_view(self):
        response = self.client.get(reverse('member-detail', args=[self.member.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "john@example.com")

    def test_member_create_view(self):
        response = self.client.get(reverse('member-create'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "version") 
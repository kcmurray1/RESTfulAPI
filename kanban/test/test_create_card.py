from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class CreateCardTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', password='johnpwd123')
    
    def post_card(self, url, title, desc, card_status):
        data = {
            "title" : title,
            "description" : desc,
            "status" : card_status
        }
        res = self.client.post(url, data, format='json')
        return res
    
    # Creat card anonymously receives 401
    def test_create_card_anonymously(self):
        url = reverse('card-collection')
        res = self.post_card(url, "Add test case", "Test that anonymous post receives 401", 0)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED
    
    # Create card with valid username and password receive 201 status
    def test_create_card_with_valid_credentials(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('card-collection')
        res = self.post_card(url, "Authenticated creation", "Allow this card to be created by valid user", 0)
        assert res.status_code == status.HTTP_201_CREATED

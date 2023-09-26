import pytest
from main import app
import unittest
from unittest.mock import patch
from role_application.applicationService import Application

class TestRoleApplication(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    @patch('role_listings.listingService.Listing.get_listing_by_index')
    @patch('models.db.session.query')
    def test_apply_for_application_successful(self, mock_query, mock_get_listing_by_index):
        listing_data = {
            'role_name': 'Manager',
            'skills': 'Leadership, Communication',
            'country': 'USA',
            'dept': 'Management',
            'is_open': True,
            'reporting_manager': None
        }
        application_data = None
        data = {
            'role_listing': 3,
            'staff_id': 2
        }
        mock_query.return_value.filter_by.return_value.first.return_value = application_data
        mock_get_listing_by_index.return_value = listing_data
        response, status_code = Application.apply_for_role(data)
        self.assertEqual(status_code, 201)
        self.assertEqual(response.get_json()['message'], 'Role application created successfully')

    @patch('role_listings.listingService.Listing.get_listing_by_index')
    def test_application_does_not_exist(self, mock_get_listing_by_index):
        listing_data = None
        data = {
            'role_listing': 3,
            'staff_id': 2
        }
        mock_get_listing_by_index.return_value = listing_data
        response, status_code = Application.apply_for_role(data)
        response_data = response.get_json()
        self.assertEqual(status_code, 404)
        self.assertEqual(response_data['message'], 'Role listing at index does not exist')

    @patch('role_listings.listingService.Listing.get_listing_by_index')
    def test_application_does_not_exist(self, mock_get_listing_by_index):
        listing_data = {
            'role_name': 'Manager',
            'skills': 'Leadership, Communication',
            'country': 'USA',
            'dept': 'Management',
            'is_open': False,
            'reporting_manager': None
        }
        data = {
            'role_listing': 3,
            'staff_id': 2
        }
        mock_get_listing_by_index.return_value = listing_data
        response, status_code = Application.apply_for_role(data)
        response_data = response.get_json()
        self.assertEqual(status_code, 400)
        self.assertEqual(response_data['message'], 'Application is closed')

    @patch('role_listings.listingService.Listing.get_listing_by_index')
    @patch('models.db.session.query')
    def test_application_does_not_exist(self, mock_query, mock_get_listing_by_index):
        listing_data = {
            'role_name': 'Manager',
            'skills': 'Leadership, Communication',
            'country': 'USA',
            'dept': 'Management',
            'is_open': True,
            'reporting_manager': None
        }
        application_data = {
            'application_date': '2023-09-15',
            'role_listing_id': 2,
            'staff_id': 2
        }
        data = {
            'role_listing': 3,
            'staff_id': 2
        }
        mock_query.return_value.filter_by.return_value.first.return_value = application_data
        mock_get_listing_by_index.return_value = listing_data
        response, status_code = Application.apply_for_role(data)
        response_data = response.get_json()
        self.assertEqual(status_code, 400)
        self.assertEqual(response_data['message'], 'You have already applied for this role listing')
    
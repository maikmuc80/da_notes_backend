from rest_framework.test import APITestCase

from .models import Note


class NoteApiTests(APITestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Einkauf', content='Milch')
        self.detail_url = f'/notes/{self.note.id}/'

    def test_list_returns_plain_array(self):
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {'id': self.note.id, 'title': 'Einkauf', 'content': 'Milch', 'marked': False, 'trash': False},
        ])

    def test_add_note(self):
        payload = {'title': 'Neu', 'content': 'Text', 'marked': False, 'trash': False}
        response = self.client.post('/notes/', payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Note.objects.count(), 2)

    def test_edit_mark_and_trash_via_put(self):
        # Das Frontend schickt bei jeder Änderung die ganze Notiz per PUT
        payload = {'id': self.note.id, 'title': 'Geändert', 'content': 'Brot', 'marked': True, 'trash': True}
        response = self.client.put(self.detail_url, payload, format='json')
        self.assertEqual(response.status_code, 200)
        self.note.refresh_from_db()
        self.assertEqual((self.note.title, self.note.marked, self.note.trash), ('Geändert', True, True))

    def test_delete_from_trash(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Note.objects.exists())

    def test_cors_allows_angular_dev_server(self):
        response = self.client.get('/notes/', HTTP_ORIGIN='http://localhost:4200')
        self.assertEqual(response['Access-Control-Allow-Origin'], 'http://localhost:4200')

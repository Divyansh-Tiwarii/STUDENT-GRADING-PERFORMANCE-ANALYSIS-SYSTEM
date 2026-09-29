import unittest, sys, tempfile
sys.path.insert(0,'.')
from database import Database

class TestDatabase(unittest.TestCase):
    def test_database_crud(self):
        with tempfile.NamedTemporaryFile(suffix='.db') as f:
            db=Database(f.name)
            db.add(1,'Test',[60,70,80])
            self.assertEqual(db.get(1)['name'], 'Test')
            db.update(1,'Updated',[90,90,90])
            self.assertEqual(db.get(1)['name'], 'Updated')
            db.delete(1)
            self.assertIsNone(db.get(1))

if __name__ == '__main__': unittest.main()

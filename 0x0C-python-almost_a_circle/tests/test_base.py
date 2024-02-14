import unittest
import json
from models.base import Base  # Assuming the Base class is in models/base.py


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_init(self):
        """Tests the initialization of Base objects."""

        # Test with ID provided
        obj1 = Base(id=10)
        self.assertEqual(obj1.id, 10)

        # Test without ID (auto-generate)
        obj2 = Base()
        self.assertEqual(obj2.id, 1)  # Assuming obj1 was the first instance

    def test_to_json_string(self):
        """Tests the to_json_string method."""

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(
            Base.to_json_string([{"a": 1}, {"b": 2}]), '[{"a": 1}, {"b": 2}]'
        )

    def test_save_to_file(self):
        """Tests the save_to_file method."""

        # Create some objects to save
        objs = [Base(42), Base(1337)]
        Base.save_to_file(objs)

        # Check if the file was created and contains correct data
        with open("Base.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [{"id": 42}, {"id": 1337}])

    def test_from_json_string(self):
        """Tests the from_json_string method."""

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(
            Base.from_json_string('[{"x": 1}, {"y": 2}]'), [{"x": 1}, {"y": 2}]
        )

    def test_create(self):
        """Tests the create method."""

        rect = Base.create(width=5, height=3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)

        square = Base.create(size=4)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)

    def test_load_from_file(self):
        """Tests the load_from_file method."""

        # Create some objects and save them to a file
        objs = [Base(10), Base(20)]
        Base.save_to_file(objs)

        # Load the objects from the file
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs[0].id, 10)
        self.assertEqual(loaded_objs[1].id, 20)


import unittest
from query_parser import QueryParser

class TestQueryParser(unittest.TestCase):
    def setUp(self):
        self.parser = QueryParser()

    def test_info_query(self):
        query = "What is AI?"
        expected_output = "AI, or artificial intelligence, is the simulation of human intelligence processes by machines, especially computer systems. These processes include learning, reasoning, problem-solving, perception, and language understanding."
        self.assertEqual(self.parser.parse_query(query), expected_output)

    def test_time_query(self):
        query = "What's the time?"
        response = self.parser.parse_query(query)
        self.assertIsNotNone(response)
        self.assertRegex(response, r'^\d{2}:\d{2} (AM|PM)$')

    def test_date_query(self):
        query = "What's the date?"
        response = self.parser.parse_query(query)
        self.assertIsNotNone(response)
        self.assertRegex(response, r'^\w+ \d{2}, \d{4}$')

    def test_calculation_query(self):
        query = "Calculate 3 + 2 * 2"
        expected_output = "7"
        self.assertEqual(self.parser.parse_query(query), expected_output)

    def test_unknown_query(self):
        query = "Who won the world cup in 2010?"
        expected_output = "Sorry, I don't have information on that topic. Please try another one."
        self.assertEqual(self.parser.parse_query(query), expected_output)

if __name__ == "__main__":
    unittest.main()


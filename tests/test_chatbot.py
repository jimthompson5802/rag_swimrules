import unittest
from src.chatbot import Chatbot

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.chatbot = Chatbot()

    def test_generate_response(self):
        response = self.chatbot.generate_response("Hello, how are you?")
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

    def test_load_model(self):
        model_loaded = self.chatbot.load_model("path/to/model")
        self.assertTrue(model_loaded)

    def test_preprocess_input(self):
        processed_input = self.chatbot.preprocess_input("   Hello!   ")
        self.assertEqual(processed_input, "Hello!")

if __name__ == '__main__':
    unittest.main()
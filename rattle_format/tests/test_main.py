import unittest

import prometheus_client

from chatter_bot import chatterbot


class AppTest(unittest.TestCase):
    """Very basic tests."""

    def setUp(self):
        # Use a custom registry per test to avoid duplicate metric declaration.
        self.registry = prometheus_client.CollectorRegistry(auto_describe=True)
        self.myapp = chatterbot.ChatterBot()
        args = self.myapp.gourde.get_argparser().parse_args([])
        self.myapp.gourde.setup(args)
        self.app = self.myapp.app.test_client()

    def test_views(self):
        rv = self.app.get("/")
        self.assertEqual(rv.status_code, 200)
        rv = self.app.get("/example")
        self.assertEqual(rv.status_code, 200)

    def test_gourde_views(self):
        """Test generic views, just for fun."""
        rv = self.app.get("/-/")
        self.assertEqual(rv.status_code, 200)
        rv = self.app.get("/-/threads")
        self.assertEqual(rv.status_code, 200)
        rv = self.app.get("/-/ready")
        self.assertEqual(rv.status_code, 200)


if __name__ == "__main__":
    unittest.main()

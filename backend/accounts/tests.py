from django.test import SimpleTestCase


class HealthAPITests(SimpleTestCase):
    def test_health_endpoint_returns_service_status(self):
        response = self.client.get("/api/v1/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"status": "ok", "service": "connectly-api"},
        )

    def test_health_endpoint_allows_configured_frontend_origins(self):
        for origin in ("http://localhost:5173", "http://127.0.0.1:5173"):
            with self.subTest(origin=origin):
                response = self.client.get(
                    "/api/v1/health/",
                    HTTP_ORIGIN=origin,
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(
                    response.headers["Access-Control-Allow-Origin"],
                    origin,
                )

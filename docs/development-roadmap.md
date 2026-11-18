# Development Roadmap

## Complete: Phase 1 — Project Foundation

Completed:
- Git and virtual environment initialized
- Django project and accounts app created
- Custom User model and initial migration created
- PostgreSQL and Redis Compose services prepared
- DRF, CORS, Simple JWT, and drf-spectacular configured
- Versioned health API and Swagger routes created
- React/Vite/TypeScript/Tailwind foundation created
- Frontend API client and initial backend health UI created

Verified:
- PostgreSQL and Redis are running through Docker Compose; PostgreSQL accepts connections and Redis responds to `PING`
- Django connects to PostgreSQL, migrations are applied, and no model migration changes are pending
- A Django superuser exists
- Django system checks pass
- Health, OpenAPI schema, and Swagger UI endpoints respond successfully
- Health endpoint allows both configured Vite development origins
- React loads in the browser and displays the successful Django health response
- Frontend TypeScript check and production build pass
- Backend health and CORS regression tests pass

## Next: Phase 2 — Authentication and Profiles

1. Implement and test registration and login APIs using the configured JWT authentication.
2. Add frontend registration/login forms, token handling, and protected routes.
3. Implement the profile model and authenticated profile read/update APIs and UI.
4. Add password reset and email verification after selecting and configuring a development email-delivery approach.

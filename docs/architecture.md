# Connectly Architecture

## Initial structure

Connectly is a modular monolith. Django owns authentication, database models, business rules, and versioned REST APIs. React is a separate browser application that communicates only through HTTP APIs.

## Backend modules

- `accounts`: custom user model and authentication
- `profiles`: public/private profile information
- `posts`: posts and media
- `comments`: comments and replies
- `social`: follows, likes, and saved posts
- `stories`: temporary stories
- `messaging`: conversations and real-time messages
- `notifications`: in-app notifications
- `moderation`: reports and moderation actions

## API contract

Versioned APIs begin at `/api/v1/`. The OpenAPI schema is generated with drf-spectacular and exposed at `/api/v1/docs/`.

## Phase 1 foundation

Django and React are initialized. The custom User model has been created before migrations. PostgreSQL is the intended database and Redis is reserved for cache, Celery, and Channels services.

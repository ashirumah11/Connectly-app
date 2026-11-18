# Database Design

## Custom user model

The `accounts.User` model extends Django's `AbstractUser` before the initial migration. It retains Django username and permission behavior while enforcing unique email addresses and indexes for username and email lookup.

## Initial migration

The migration `accounts/0001_initial.py` creates the custom User model and is based on Django's built-in authentication migration. Applying it requires a running PostgreSQL server.

## Intended core relationships

- Profile: one-to-one with User
- Post: many-to-one User; one-to-many PostMedia
- Comment: many-to-one Post/User; optional parent comment for replies
- Like: many-to-one Post/User with a unique Post/User constraint
- Follow: many-to-one follower/following Users with a unique relationship constraint and self-follow check
- SavedPost: many-to-one Post/User with uniqueness
- Story and StoryView: expire after 24 hours and track viewers
- Conversation: many-to-many Users through ConversationParticipant
- Message: many-to-one Conversation/User
- Notification: many-to-one recipient with polymorphic target references
- Report: many-to-one reporter and moderated target

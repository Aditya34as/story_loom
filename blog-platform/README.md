# StoryLoom Blog Platform

StoryLoom is a Laravel blog platform built for writers to publish articles, manage content, and engage with readers. It includes public article pages, comments, writer post management, and an admin interface for moderation.

## Features

- Public homepage with featured and latest articles
- Reader and writer registration
- Login and logout
- Writer dashboard for creating, editing, publishing, and deleting posts
- Article detail pages with comment support
- Admin dashboard for managing posts, comments, and user roles
- Seeded demo data for presentation or assignment review

## Tech Stack

- Laravel 12
- PHP 8.2
- MySQL database
- Blade templates

## Demo Accounts

- Admin
  - Email: `admin@storyloom.test`
  - Password: `password`
- Writer
  - Email: `writer@storyloom.test`
  - Password: `password`
- Reader
  - Email: `reader@storyloom.test`
  - Password: `password`

## Setup

1. Install dependencies:

```bash
composer install
```

2. Create the environment file if needed:

```bash
copy .env.example .env
```

3. Generate the app key:

```bash
php artisan key:generate
```

4. Run migrations and seed sample data:

```bash
php artisan migrate:fresh --seed
```

5. Start the local server:

```bash
php artisan serve
```

6. Open the application in your browser at `http://127.0.0.1:8000`

## Important Routes

- `/` - Homepage
- `/posts` - All published articles
- `/login` - Login page
- `/register` - Registration page
- `/dashboard/posts` - Writer dashboard
- `/admin` - Admin dashboard

## Testing

```bash
php artisan test
```

## Notes

- The project is configured for MySQL by default.
- For XAMPP, keep MySQL running and create a database named `storyloom` before migrating.
- Featured images are stored as image URLs to keep the first version simple and fully working.
- Admin users can hide or delete comments and change user roles.

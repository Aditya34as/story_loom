# StoryLoom

StoryLoom is a Laravel-based blog platform built for writers to publish articles, manage content, and engage with readers. It includes a public blog frontend, writer dashboard, comment system, and an admin panel for moderation and user management.

## Project Summary

This project was created around the following idea:

- Writers should be able to create, edit, and publish blog posts
- Readers should be able to browse articles and comment on them
- Admins should be able to manage posts, comments, and user roles
- The website should look like a proper working platform, not just a backend prototype

## Features

- Public homepage with featured and latest posts
- Public article listing page
- Single article detail page
- Reader comments on published posts
- User registration and login
- Role-based access: `reader`, `writer`, `admin`
- Writer dashboard for managing posts
- Admin dashboard for moderation and user management
- Tailwind CSS based UI
- MySQL database integration

## Roles

### Reader

- Register and log in
- Browse published blog posts
- Open article detail pages
- Add comments to published posts

### Writer

- Create blog posts
- Save drafts
- Publish posts
- Edit and delete own posts
- Manage posts from the writer dashboard

### Admin

- View platform overview
- Manage all posts
- Hide or delete comments
- Change user roles

## Tech Stack

- Laravel 12
- PHP 8.2
- MySQL
- Blade templates
- Tailwind CSS
- Vite

## Project Structure

- [app/Http/Controllers](C:\Users\adity\OneDrive\Documents\New project\blog-platform\app\Http\Controllers)  
  Application logic for public pages, authentication, dashboard, and admin panel

- [app/Models](C:\Users\adity\OneDrive\Documents\New project\blog-platform\app\Models)  
  Eloquent models such as `User`, `Post`, and `Comment`

- [database/migrations](C:\Users\adity\OneDrive\Documents\New project\blog-platform\database\migrations)  
  Database schema for users, posts, comments, jobs, cache, and sessions

- [database/seeders](C:\Users\adity\OneDrive\Documents\New project\blog-platform\database\seeders)  
  Demo data for admin, writer, reader, posts, and comments

- [resources/views](C:\Users\adity\OneDrive\Documents\New project\blog-platform\resources\views)  
  Blade templates for frontend, dashboard, and admin UI

- [routes/web.php](C:\Users\adity\OneDrive\Documents\New project\blog-platform\routes\web.php)  
  Main application routes

## Database

The project is configured to use MySQL.

Current environment defaults:

- `DB_CONNECTION=mysql`
- `DB_HOST=127.0.0.1`
- `DB_PORT=3306`
- `DB_DATABASE=storyloom`
- `DB_USERNAME=root`
- `DB_PASSWORD=`

For testing, the project uses a separate MySQL database:

- `storyloom_testing`

## Demo Accounts

These accounts are created by the database seeder:

- Admin
  - Email: `admin@storyloom.test`
  - Password: `password`

- Writer
  - Email: `writer@storyloom.test`
  - Password: `password`

- Reader
  - Email: `reader@storyloom.test`
  - Password: `password`

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd blog-platform
```

### 2. Install backend dependencies

```bash
composer install
```

### 3. Install frontend dependencies

```bash
npm install
```

### 4. Create the environment file

```bash
copy .env.example .env
```

If `.env` already exists, you can skip this.

### 5. Generate application key

```bash
php artisan key:generate
```

### 6. Start MySQL

Start MySQL from XAMPP Control Panel and make sure it is running on port `3306`.

### 7. Create the database

```bash
C:\xampp\mysql\bin\mysql.exe -u root -e "CREATE DATABASE IF NOT EXISTS storyloom CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

### 8. Run migrations and seed data

```bash
php artisan migrate:fresh --seed
```

Note:

- `migrate:fresh --seed` deletes existing tables and recreates them
- if you want to keep your existing data, use `php artisan migrate` instead

### 9. Build frontend assets

```bash
npm run build
```

### 10. Start the development server

```bash
php artisan serve
```

Open:

- [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Development Workflow

For normal backend usage:

```bash
php artisan serve
```

For live frontend updates while editing Tailwind/UI:

```bash
npm run dev
```

You can run both in separate terminals during development.

## Important Routes

### Public

- `/` - Homepage
- `/posts` - All published posts
- `/posts/{slug}` - Single post page

### Authentication

- `/login`
- `/register`
- `/logout`

### Writer Dashboard

- `/dashboard/posts`
- `/dashboard/posts/create`
- `/dashboard/posts/{post}/edit`

### Admin Panel

- `/admin`
- `/admin/posts`
- `/admin/comments`
- `/admin/users`

## Testing

Run the test suite with:

```bash
php artisan test
```

## Important Notes

- Only posts with `status = published` and a valid `published_at` date appear on the homepage and reader-facing article pages
- Draft posts will only appear in the writer dashboard
- If you run `php artisan migrate:fresh --seed`, any posts you created manually will be removed and replaced by seeded demo data
- The project uses MySQL now and is no longer dependent on SQLite

## GitHub Safety

The project includes:

- [.gitignore](C:\Users\adity\OneDrive\Documents\New project\blog-platform\.gitignore)
- [.env.example](C:\Users\adity\OneDrive\Documents\New project\blog-platform\.env.example)

This means:

- local `.env` secrets are not pushed
- `vendor`, `node_modules`, `public/build`, logs, and cache files are not pushed
- the repository is safe to upload after reviewing your own local changes

## Future Improvements

- Search and category filtering
- Rich text editor for blog writing
- Image upload instead of image URLs
- Pagination improvements in dashboard views
- Profile pages for writers
- Like/bookmark features

## Author

Built as a Laravel blog platform project with role-based publishing, comments, admin moderation, and Tailwind UI.

#!/bin/sh
set -e

# Cache configuration, routes, and views for production
echo "Caching configurations..."
php artisan config:cache
php artisan route:cache
php artisan view:cache

# Run migrations (automatically in production)
echo "Running database migrations..."
php artisan migrate --force

exec "$@"

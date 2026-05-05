<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ $title ?? 'StoryLoom' }}</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
    <div class="relative min-h-screen">
        <header class="sticky top-0 z-20 border-b border-amber-100/80 bg-[#fbf6ef]/90 backdrop-blur">
            <div class="site-container flex flex-col gap-4 py-4 md:flex-row md:items-center md:justify-between">
                <div class="flex items-center gap-6">
                    <a href="{{ route('home') }}" class="group inline-flex items-center gap-3">
                        <span class="grid h-11 w-11 place-items-center rounded-2xl bg-gradient-to-br from-orange-700 to-orange-400 text-lg font-bold text-white shadow-md transition group-hover:-translate-y-0.5">S</span>
                        <span class="text-xl font-semibold tracking-tight text-stone-900">StoryLoom</span>
                    </a>
                    <nav class="flex items-center gap-4 text-sm font-medium text-stone-600">
                        <a href="{{ route('posts.index') }}" class="hover:text-stone-900">Articles</a>
                    </nav>
                </div>

                <div class="flex flex-wrap items-center gap-3 text-sm">
                    @auth
                        @if(auth()->user()->isWriter())
                            <a href="{{ route('dashboard.posts.index') }}" class="hover:text-stone-900">Writer Dashboard</a>
                        @endif
                        @if(auth()->user()->isAdmin())
                            <a href="{{ route('admin.dashboard') }}" class="hover:text-stone-900">Admin</a>
                        @endif
                        <form action="{{ route('logout') }}" method="POST">
                            @csrf
                            <button type="submit" class="btn-secondary cursor-pointer">Logout</button>
                        </form>
                    @else
                        <a href="{{ route('login') }}" class="font-medium text-stone-700 hover:text-stone-900">Login</a>
                        <a href="{{ route('register') }}" class="btn-primary">Get Started</a>
                    @endauth
                </div>
            </div>
        </header>

        <main class="site-container py-6 md:py-8">
            <div class="space-y-3">
                @if (session('success'))
                    <div class="flash-success">{{ session('success') }}</div>
                @endif

                @if ($errors->any())
                    <div class="flash-error">{{ $errors->first() }}</div>
                @endif
            </div>

            @yield('content')
        </main>

        <footer class="site-container pb-10 pt-4">
            <div class="border-t border-stone-200 pt-6 text-sm text-stone-500">
                StoryLoom is a Laravel-powered publishing platform for writers, readers, and admins.
            </div>
        </footer>
    </div>
</body>
</html>

@extends('layouts.app', ['title' => 'Login'])

@section('content')
    <div class="grid min-h-[70vh] place-items-center">
        <div class="surface-card w-full max-w-xl p-8 md:p-10">
            <div class="eyebrow">Welcome back</div>
            <h1 class="mt-4 text-4xl font-semibold text-stone-900">Login to StoryLoom</h1>
            <form action="{{ route('login.store') }}" method="POST" class="mt-6 space-y-4">
                @csrf
                <div>
                    <label for="email" class="input-label">Email address</label>
                    <input type="email" id="email" name="email" value="{{ old('email') }}" required class="text-input">
                </div>
                <div>
                    <label for="password" class="input-label">Password</label>
                    <input type="password" id="password" name="password" required class="text-input">
                </div>
                <label class="flex items-center gap-3 text-sm text-stone-600">
                    <input type="checkbox" id="remember" name="remember" class="h-4 w-4 rounded border-stone-300 text-orange-700 focus:ring-orange-200">
                    <span>Remember me</span>
                </label>
                <button type="submit" class="btn-primary cursor-pointer">Login</button>
            </form>
            <p class="mt-5 text-sm text-stone-600">No account yet? <a href="{{ route('register') }}" class="font-semibold text-orange-700 hover:text-orange-800">Create one here</a>.</p>
        </div>
    </div>
@endsection

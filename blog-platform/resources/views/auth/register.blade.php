@extends('layouts.app', ['title' => 'Register'])

@section('content')
    <div class="grid min-h-[70vh] place-items-center">
        <div class="surface-card w-full max-w-2xl p-8 md:p-10">
            <div class="eyebrow">Create your account</div>
            <h1 class="mt-4 text-4xl font-semibold text-stone-900">Join StoryLoom</h1>
            <form action="{{ route('register.store') }}" method="POST" class="mt-6 space-y-4">
                @csrf
                <div>
                    <label for="name" class="input-label">Full name</label>
                    <input type="text" id="name" name="name" value="{{ old('name') }}" required class="text-input">
                </div>
                <div>
                    <label for="email" class="input-label">Email address</label>
                    <input type="email" id="email" name="email" value="{{ old('email') }}" required class="text-input">
                </div>
                <div>
                    <label for="role" class="input-label">Join as</label>
                    <select id="role" name="role" required class="select-input">
                        <option value="reader" @selected(old('role') === 'reader')>Reader</option>
                        <option value="writer" @selected(old('role') === 'writer')>Writer</option>
                    </select>
                </div>
                <div>
                    <label for="password" class="input-label">Password</label>
                    <input type="password" id="password" name="password" required class="text-input">
                </div>
                <div>
                    <label for="password_confirmation" class="input-label">Confirm password</label>
                    <input type="password" id="password_confirmation" name="password_confirmation" required class="text-input">
                </div>
                <button type="submit" class="btn-primary cursor-pointer">Create account</button>
            </form>
        </div>
    </div>
@endsection

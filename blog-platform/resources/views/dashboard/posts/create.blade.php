@extends('layouts.app', ['title' => 'Create Post'])

@section('content')
    <div class="my-8 grid gap-6 xl:grid-cols-[220px_minmax(0,1fr)]">
        @include('dashboard.partials.sidebar')

        <section class="surface-card p-6 md:p-8">
            <div class="eyebrow">New article</div>
            <h1 class="mt-4 text-4xl font-semibold text-stone-900">Create a blog post</h1>
            <form action="{{ route('dashboard.posts.store') }}" method="POST" class="mt-6 space-y-4">
                @csrf
                @include('dashboard.posts.form')
                <div class="flex flex-wrap gap-3 pt-2">
                    <button type="submit" class="btn-primary cursor-pointer">Save post</button>
                    <a href="{{ route('dashboard.posts.index') }}" class="btn-secondary">Cancel</a>
                </div>
            </form>
        </section>
    </div>
@endsection

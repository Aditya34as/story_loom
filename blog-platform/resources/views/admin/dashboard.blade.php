@extends('layouts.app', ['title' => 'Admin Dashboard'])

@section('content')
    <div class="my-8 grid gap-6 xl:grid-cols-[220px_minmax(0,1fr)]">
        @include('admin.partials.sidebar')

        <section>
            <div class="space-y-3">
                <div class="eyebrow">Admin overview</div>
                <h1 class="section-heading text-4xl">Platform management</h1>
            </div>

            <div class="my-6 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
                <div class="surface-card p-6">
                    <p class="text-sm font-semibold uppercase tracking-[0.16em] text-stone-500">Total posts</p>
                    <h2 class="mt-3 text-4xl font-semibold text-stone-900">{{ $totalPosts }}</h2>
                </div>
                <div class="surface-card p-6">
                    <p class="text-sm font-semibold uppercase tracking-[0.16em] text-stone-500">Published</p>
                    <h2 class="mt-3 text-4xl font-semibold text-stone-900">{{ $publishedPosts }}</h2>
                </div>
                <div class="surface-card p-6">
                    <p class="text-sm font-semibold uppercase tracking-[0.16em] text-stone-500">Drafts</p>
                    <h2 class="mt-3 text-4xl font-semibold text-stone-900">{{ $draftPosts }}</h2>
                </div>
                <div class="surface-card p-6">
                    <p class="text-sm font-semibold uppercase tracking-[0.16em] text-stone-500">Comments</p>
                    <h2 class="mt-3 text-4xl font-semibold text-stone-900">{{ $totalComments }}</h2>
                </div>
            </div>

            <div class="surface-card p-6 md:p-8">
                <div class="mb-5">
                    <h2 class="text-2xl font-semibold text-stone-900">Recent posts</h2>
                    <p class="mt-2 text-sm text-stone-600">{{ $writers }} writers are currently active on the platform.</p>
                </div>
                <div class="space-y-4">
                    @foreach($recentPosts as $post)
                        <div class="surface-panel p-5">
                            <strong class="text-stone-900">{{ $post->title }}</strong>
                            <p class="meta-text mt-2">{{ $post->author->name }} &middot; {{ ucfirst($post->status) }}</p>
                        </div>
                    @endforeach
                </div>
            </div>
        </section>
    </div>
@endsection

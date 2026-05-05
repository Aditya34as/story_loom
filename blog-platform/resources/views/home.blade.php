@extends('layouts.app', ['title' => 'StoryLoom | Home'])

@section('content')
    <section class="surface-card mb-12 overflow-hidden">
        <div class="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
            <div class="space-y-6 p-8 md:p-10">
                <div class="eyebrow">Publishing platform for writers</div>
                <h1 class="max-w-3xl text-4xl font-semibold leading-tight text-stone-900 md:text-6xl">Write boldly, publish cleanly, and grow a real reading community.</h1>
                <p class="max-w-2xl text-base leading-8 text-stone-600 md:text-lg">StoryLoom gives writers a focused space to publish articles, readers a smooth reading experience, and admins the tools to keep the platform healthy.</p>
                <div class="flex flex-wrap gap-3">
                    <a href="{{ route('posts.index') }}" class="btn-primary">Explore Articles</a>
                    <a href="{{ route('register') }}" class="btn-secondary">Join as Writer</a>
                </div>
            </div>

            <div class="space-y-4 p-8 pt-0 lg:p-8 lg:pl-0 lg:pt-8">
                <div class="surface-panel p-6">
                    <span class="pill">Built for the assignment brief</span>
                    <h2 class="mt-4 text-2xl font-semibold text-stone-900">Included modules</h2>
                    <p class="mt-3 text-sm leading-7 text-stone-600">Authentication, public article pages, comment system, writer dashboard, and admin content management.</p>
                </div>
                <div class="surface-panel p-6">
                    <span class="pill">Sharing ready</span>
                    <h2 class="mt-4 text-2xl font-semibold text-stone-900">Audience engagement</h2>
                    <p class="mt-3 text-sm leading-7 text-stone-600">Readers can comment, browse published stories, and share article links directly from each post page.</p>
                </div>
            </div>
        </div>
    </section>

    @if($featuredPost)
        <section class="mb-10">
            <div class="mb-5 flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
                <div class="space-y-3">
                    <div class="eyebrow">Featured story</div>
                    <h2 class="section-heading">{{ $featuredPost->title }}</h2>
                    <p class="body-copy">By {{ $featuredPost->author->name }} on {{ $featuredPost->published_at->format('d M Y') }}</p>
                </div>
                <a href="{{ route('posts.show', $featuredPost->slug) }}" class="btn-primary">Read article</a>
            </div>

            <div class="surface-card p-6 md:p-8">
                @if($featuredPost->featured_image)
                    <img src="{{ $featuredPost->featured_image }}" alt="{{ $featuredPost->title }}" class="mb-5 aspect-[16/9] w-full rounded-3xl object-cover">
                @endif
                <p class="body-copy">{{ $featuredPost->excerpt }}</p>
            </div>
        </section>
    @endif

    <section class="mb-8">
        <div class="mb-6 space-y-3">
            <div class="eyebrow">Latest articles</div>
            <h2 class="section-heading">Fresh writing from the platform</h2>
        </div>

        <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
            @forelse($latestPosts as $post)
                <article class="surface-card overflow-hidden p-6">
                    @if($post->featured_image)
                        <img src="{{ $post->featured_image }}" alt="{{ $post->title }}" class="mb-4 aspect-[16/9] w-full rounded-3xl object-cover">
                    @endif
                    <span class="pill">{{ ucfirst($post->status) }}</span>
                    <h3 class="mt-4 text-2xl font-semibold text-stone-900">{{ $post->title }}</h3>
                    <p class="mt-3 text-sm leading-7 text-stone-600">{{ $post->excerpt }}</p>
                    <p class="meta-text mt-4">By {{ $post->author->name }} &middot; {{ $post->published_at->format('d M Y') }}</p>
                    <a href="{{ route('posts.show', $post->slug) }}" class="btn-primary mt-5">Read more</a>
                </article>
            @empty
                <div class="surface-card col-span-full p-10 text-center text-stone-600">
                    No published posts yet. Writers can add articles from the dashboard.
                </div>
            @endforelse
        </div>
    </section>
@endsection

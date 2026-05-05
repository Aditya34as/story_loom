@extends('layouts.app', ['title' => 'All Articles'])

@section('content')
    <section class="mb-8 mt-2 space-y-3">
        <div class="eyebrow">Article archive</div>
        <h1 class="section-heading text-4xl md:text-5xl">Browse published stories</h1>
        <p class="max-w-3xl text-base leading-8 text-stone-600">Readers can discover all published articles here, while writers manage drafts and new posts inside the dashboard.</p>
    </section>

    <div class="mb-6 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        @forelse($posts as $post)
            <article class="surface-card overflow-hidden p-6">
                @if($post->featured_image)
                    <img src="{{ $post->featured_image }}" alt="{{ $post->title }}" class="mb-4 aspect-[16/9] w-full rounded-3xl object-cover">
                @endif
                <h2 class="text-2xl font-semibold text-stone-900">{{ $post->title }}</h2>
                <p class="mt-3 text-sm leading-7 text-stone-600">{{ $post->excerpt }}</p>
                <p class="meta-text mt-4">By {{ $post->author->name }} &middot; {{ $post->published_at->format('d M Y') }}</p>
                <a href="{{ route('posts.show', $post->slug) }}" class="btn-primary mt-5">Open story</a>
            </article>
        @empty
            <div class="surface-card col-span-full p-10 text-center text-stone-600">
                No published articles are available yet.
            </div>
        @endforelse
    </div>

    <div class="pb-4">
        {{ $posts->links() }}
    </div>
@endsection

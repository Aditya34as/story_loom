@extends('layouts.app', ['title' => $post->title])

@section('content')
    <section class="mb-6 mt-2 space-y-3">
        <div class="eyebrow">Published article</div>
        <h1 class="section-heading text-4xl md:text-5xl">{{ $post->title }}</h1>
        <p class="meta-text">By {{ $post->author->name }} &middot; {{ $post->published_at->format('d M Y') }}</p>
    </section>

    <div class="mb-8 grid gap-6 xl:grid-cols-[minmax(0,2fr)_minmax(320px,1fr)]">
        <article class="surface-card p-6 md:p-8">
            @if($post->featured_image)
                <img src="{{ $post->featured_image }}" alt="{{ $post->title }}" class="mb-5 aspect-[16/9] w-full rounded-3xl object-cover">
            @endif
            <p class="mb-6 text-base leading-8 text-stone-600">{{ $post->excerpt }}</p>
            <div class="whitespace-pre-line text-[15px] leading-8 text-stone-800 md:text-base">{{ $post->content }}</div>
        </article>

        <aside class="space-y-4">
            <div class="surface-panel p-6">
                <span class="pill">Share article</span>
                <p class="mt-4 text-sm leading-7 text-stone-600">Copy or share this article link with your audience.</p>
                <div class="mt-4 flex flex-wrap gap-3">
                    <a class="btn-primary" href="https://wa.me/?text={{ urlencode(url()->current()) }}" target="_blank" rel="noreferrer">WhatsApp</a>
                    <a class="btn-secondary" href="https://www.linkedin.com/sharing/share-offsite/?url={{ urlencode(url()->current()) }}" target="_blank" rel="noreferrer">LinkedIn</a>
                </div>
                <div class="mt-4">
                    <input type="text" value="{{ url()->current() }}" readonly class="text-input">
                </div>
            </div>

            <div class="surface-panel p-6">
                <span class="pill">More from StoryLoom</span>
                <div class="mt-4 space-y-4">
                    @forelse($relatedPosts as $relatedPost)
                        <div class="border-b border-amber-100 pb-4 last:border-b-0 last:pb-0">
                            <a href="{{ route('posts.show', $relatedPost->slug) }}" class="text-lg font-semibold text-stone-900 hover:text-orange-700">{{ $relatedPost->title }}</a>
                            <p class="meta-text mt-1">{{ $relatedPost->author->name }}</p>
                        </div>
                    @empty
                        <p class="text-sm text-stone-600">No related stories yet.</p>
                    @endforelse
                </div>
            </div>
        </aside>
    </div>

    <section class="surface-card mb-8 p-6 md:p-8">
        <div class="mb-5 space-y-3">
            <div class="eyebrow">Comments</div>
            <h2 class="section-heading text-3xl">Reader discussion</h2>
        </div>

        @auth
            <form action="{{ route('comments.store', $post) }}" method="POST" class="mb-6 space-y-4">
                @csrf
                <div>
                    <label for="comment" class="input-label">Add your comment</label>
                    <textarea id="comment" name="comment" placeholder="Share your thoughts about this article..." class="text-area">{{ old('comment') }}</textarea>
                </div>
                <button type="submit" class="btn-primary cursor-pointer">Post Comment</button>
            </form>
        @else
            <p class="mb-6 text-sm text-stone-600"><a href="{{ route('login') }}" class="font-semibold text-orange-700 hover:text-orange-800">Login</a> to join the discussion.</p>
        @endauth

        <div class="space-y-4">
            @forelse($post->comments as $comment)
                <div class="surface-panel p-6">
                    <strong class="text-stone-900">{{ $comment->user->name }}</strong>
                    <p class="meta-text mt-1">{{ $comment->created_at->format('d M Y, h:i A') }}</p>
                    <p class="mt-3 text-sm leading-7 text-stone-700">{{ $comment->comment }}</p>
                </div>
            @empty
                <p class="text-sm text-stone-600">No comments yet. Be the first one to respond.</p>
            @endforelse
        </div>
    </section>
@endsection

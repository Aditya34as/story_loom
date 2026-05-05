@extends('layouts.app', ['title' => 'Writer Dashboard'])

@section('content')
    <div class="my-8 grid gap-6 xl:grid-cols-[220px_minmax(0,1fr)]">
        @include('dashboard.partials.sidebar')

        <section>
            <div class="mb-5 flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
                <div class="space-y-3">
                    <div class="eyebrow">Writer dashboard</div>
                    <h1 class="section-heading text-4xl">Manage your posts</h1>
                </div>
                <a href="{{ route('dashboard.posts.create') }}" class="btn-primary">New Post</a>
            </div>

            <div class="surface-card overflow-hidden">
                <div class="overflow-x-auto">
                    <table class="min-w-full divide-y divide-amber-100">
                        <thead class="bg-amber-50/70">
                            <tr class="text-left text-sm font-semibold text-stone-700">
                                <th class="px-6 py-4">Title</th>
                                <th class="px-6 py-4">Status</th>
                                <th class="px-6 py-4">Published</th>
                                <th class="px-6 py-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-amber-100 text-sm text-stone-700">
                            @forelse($posts as $post)
                                <tr>
                                    <td class="px-6 py-4">
                                        <strong class="text-stone-900">{{ $post->title }}</strong>
                                        <div class="mt-1 text-stone-500">{{ $post->excerpt }}</div>
                                    </td>
                                    <td class="px-6 py-4"><span class="pill">{{ ucfirst($post->status) }}</span></td>
                                    <td class="px-6 py-4">{{ $post->published_at?->format('d M Y') ?? 'Not published' }}</td>
                                    <td class="px-6 py-4">
                                        <div class="flex flex-wrap gap-2">
                                            <a href="{{ route('dashboard.posts.edit', $post) }}" class="btn-secondary">Edit</a>
                                            @if($post->status === 'published')
                                                <a href="{{ route('posts.show', $post->slug) }}" class="btn-secondary">View</a>
                                            @endif
                                            <form action="{{ route('dashboard.posts.destroy', $post) }}" method="POST">
                                                @csrf
                                                @method('DELETE')
                                                <button type="submit" class="btn-primary cursor-pointer">Delete</button>
                                            </form>
                                        </div>
                                    </td>
                                </tr>
                            @empty
                                <tr>
                                    <td colspan="4" class="px-6 py-10 text-center text-stone-600">No posts yet. Start by creating your first article.</td>
                                </tr>
                            @endforelse
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="mt-4">
                {{ $posts->links() }}
            </div>
        </section>
    </div>
@endsection

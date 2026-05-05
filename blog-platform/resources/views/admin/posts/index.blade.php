@extends('layouts.app', ['title' => 'Admin Posts'])

@section('content')
    <div class="my-8 grid gap-6 xl:grid-cols-[220px_minmax(0,1fr)]">
        @include('admin.partials.sidebar')

        <section>
            <div class="mb-5 space-y-3">
                <div class="eyebrow">Admin posts</div>
                <h1 class="section-heading text-4xl">Manage all articles</h1>
            </div>

            <div class="surface-card overflow-hidden">
                <div class="overflow-x-auto">
                    <table class="min-w-full divide-y divide-amber-100">
                        <thead class="bg-amber-50/70">
                            <tr class="text-left text-sm font-semibold text-stone-700">
                                <th class="px-6 py-4">Title</th>
                                <th class="px-6 py-4">Author</th>
                                <th class="px-6 py-4">Status</th>
                                <th class="px-6 py-4">Action</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-amber-100 text-sm text-stone-700">
                            @forelse($posts as $post)
                                <tr>
                                    <td class="px-6 py-4">{{ $post->title }}</td>
                                    <td class="px-6 py-4">{{ $post->author->name }}</td>
                                    <td class="px-6 py-4">{{ ucfirst($post->status) }}</td>
                                    <td class="px-6 py-4">
                                        <form action="{{ route('admin.posts.destroy', $post) }}" method="POST">
                                            @csrf
                                            @method('DELETE')
                                            <button type="submit" class="btn-primary cursor-pointer">Delete</button>
                                        </form>
                                    </td>
                                </tr>
                            @empty
                                <tr>
                                    <td colspan="4" class="px-6 py-10 text-center text-stone-600">No posts found.</td>
                                </tr>
                            @endforelse
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="mt-4">{{ $posts->links() }}</div>
        </section>
    </div>
@endsection

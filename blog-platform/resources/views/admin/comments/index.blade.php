@extends('layouts.app', ['title' => 'Admin Comments'])

@section('content')
    <div class="my-8 grid gap-6 xl:grid-cols-[220px_minmax(0,1fr)]">
        @include('admin.partials.sidebar')

        <section>
            <div class="mb-5 space-y-3">
                <div class="eyebrow">Comment moderation</div>
                <h1 class="section-heading text-4xl">Manage reader comments</h1>
            </div>

            <div class="surface-card overflow-hidden">
                <div class="overflow-x-auto">
                    <table class="min-w-full divide-y divide-amber-100">
                        <thead class="bg-amber-50/70">
                            <tr class="text-left text-sm font-semibold text-stone-700">
                                <th class="px-6 py-4">Comment</th>
                                <th class="px-6 py-4">User</th>
                                <th class="px-6 py-4">Post</th>
                                <th class="px-6 py-4">Status</th>
                                <th class="px-6 py-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-amber-100 text-sm text-stone-700">
                            @forelse($comments as $comment)
                                <tr>
                                    <td class="px-6 py-4">{{ $comment->comment }}</td>
                                    <td class="px-6 py-4">{{ $comment->user->name }}</td>
                                    <td class="px-6 py-4">{{ $comment->post->title }}</td>
                                    <td class="px-6 py-4">{{ ucfirst($comment->status) }}</td>
                                    <td class="px-6 py-4">
                                        <div class="flex flex-wrap gap-2">
                                            <form action="{{ route('admin.comments.toggle', $comment) }}" method="POST">
                                                @csrf
                                                @method('PATCH')
                                                <button type="submit" class="btn-primary cursor-pointer">{{ $comment->status === 'visible' ? 'Hide' : 'Show' }}</button>
                                            </form>
                                            <form action="{{ route('admin.comments.destroy', $comment) }}" method="POST">
                                                @csrf
                                                @method('DELETE')
                                                <button type="submit" class="btn-secondary cursor-pointer">Delete</button>
                                            </form>
                                        </div>
                                    </td>
                                </tr>
                            @empty
                                <tr>
                                    <td colspan="5" class="px-6 py-10 text-center text-stone-600">No comments available.</td>
                                </tr>
                            @endforelse
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="mt-4">{{ $comments->links() }}</div>
        </section>
    </div>
@endsection

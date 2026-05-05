@extends('layouts.app', ['title' => 'Edit Post'])

@section('content')
    <div class="my-8 grid gap-6 xl:grid-cols-[220px_minmax(0,1fr)]">
        @include('dashboard.partials.sidebar')

        <section class="surface-card p-6 md:p-8">
            <div class="eyebrow">Update article</div>
            <h1 class="mt-4 text-4xl font-semibold text-stone-900">Edit your post</h1>
            <form action="{{ route('dashboard.posts.update', $post) }}" method="POST" class="mt-6 space-y-4">
                @csrf
                @method('PUT')
                @include('dashboard.posts.form', ['post' => $post])
                <div class="flex flex-wrap gap-3 pt-2">
                    <button type="submit" class="btn-primary cursor-pointer">Update post</button>
                    <a href="{{ route('dashboard.posts.index') }}" class="btn-secondary">Back</a>
                </div>
            </form>
        </section>
    </div>
@endsection

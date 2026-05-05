<?php

namespace App\Http\Controllers\Dashboard;

use App\Http\Controllers\Controller;
use App\Models\Post;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class PostController extends Controller
{
    public function index(Request $request): View
    {
        $user = $request->user();

        $posts = Post::with('author')
            ->when(! $user->isAdmin(), fn ($query) => $query->where('user_id', $user->id))
            ->latest()
            ->paginate(10);

        return view('dashboard.posts.index', compact('posts'));
    }

    public function create(): View
    {
        return view('dashboard.posts.create');
    }

    public function store(Request $request): RedirectResponse
    {
        $data = $this->validatedData($request);
        $data['user_id'] = $request->user()->id;
        $data['slug'] = $this->uniqueSlug($data['title']);
        $data['published_at'] = $data['status'] === 'published' ? now() : null;

        Post::create($data);

        return redirect()->route('dashboard.posts.index')->with('success', 'Post created successfully.');
    }

    public function edit(Post $post, Request $request): View
    {
        $this->authorizePost($post, $request);

        return view('dashboard.posts.edit', compact('post'));
    }

    public function update(Request $request, Post $post): RedirectResponse
    {
        $this->authorizePost($post, $request);

        $data = $this->validatedData($request);
        $data['slug'] = $this->uniqueSlug($data['title'], $post->id);
        $data['published_at'] = $data['status'] === 'published'
            ? ($post->published_at ?? now())
            : null;

        $post->update($data);

        return redirect()->route('dashboard.posts.index')->with('success', 'Post updated successfully.');
    }

    public function destroy(Post $post, Request $request): RedirectResponse
    {
        $this->authorizePost($post, $request);

        $post->delete();

        return redirect()->route('dashboard.posts.index')->with('success', 'Post deleted.');
    }

    private function validatedData(Request $request): array
    {
        return $request->validate([
            'title' => ['required', 'string', 'max:255'],
            'excerpt' => ['required', 'string', 'max:400'],
            'content' => ['required', 'string', 'min:50'],
            'featured_image' => ['nullable', 'url', 'max:500'],
            'status' => ['required', 'in:draft,published'],
        ]);
    }

    private function authorizePost(Post $post, Request $request): void
    {
        $user = $request->user();

        abort_unless($user->isAdmin() || $post->user_id === $user->id, 403);
    }

    private function uniqueSlug(string $title, ?int $ignoreId = null): string
    {
        $baseSlug = Str::slug($title);
        $slug = $baseSlug;
        $counter = 1;

        while (
            Post::where('slug', $slug)
                ->when($ignoreId, fn ($query) => $query->whereKeyNot($ignoreId))
                ->exists()
        ) {
            $slug = $baseSlug.'-'.$counter;
            $counter++;
        }

        return $slug;
    }
}

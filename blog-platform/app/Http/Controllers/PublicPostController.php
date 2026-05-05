<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\View\View;

class PublicPostController extends Controller
{
    public function index(): View
    {
        $posts = Post::with('author')
            ->published()
            ->latest('published_at')
            ->paginate(9);

        return view('posts.index', compact('posts'));
    }

    public function show(string $slug): View
    {
        $post = Post::with([
            'author',
            'comments' => fn ($query) => $query->where('status', 'visible')->latest(),
            'comments.user',
        ])
            ->published()
            ->where('slug', $slug)
            ->firstOrFail();

        $relatedPosts = Post::with('author')
            ->published()
            ->whereKeyNot($post->id)
            ->latest('published_at')
            ->take(3)
            ->get();

        return view('posts.show', compact('post', 'relatedPosts'));
    }
}

<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\View\View;

class HomeController extends Controller
{
    public function __invoke(): View
    {
        $featuredPost = Post::with('author')
            ->published()
            ->latest('published_at')
            ->first();

        $latestPosts = Post::with('author')
            ->published()
            ->when($featuredPost, fn ($query) => $query->whereKeyNot($featuredPost->id))
            ->latest('published_at')
            ->take(6)
            ->get();

        return view('home', compact('featuredPost', 'latestPosts'));
    }
}

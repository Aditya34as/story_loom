<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class CommentController extends Controller
{
    public function store(Request $request, Post $post): RedirectResponse
    {
        abort_unless($post->status === 'published', 404);

        $data = $request->validate([
            'comment' => ['required', 'string', 'min:5', 'max:1200'],
        ]);

        $post->comments()->create([
            'user_id' => $request->user()->id,
            'comment' => $data['comment'],
            'status' => 'visible',
        ]);

        return back()->with('success', 'Comment added successfully.');
    }
}

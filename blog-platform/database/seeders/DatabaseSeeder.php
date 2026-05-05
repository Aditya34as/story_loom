<?php

namespace Database\Seeders;

use App\Models\Comment;
use App\Models\Post;
use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    use WithoutModelEvents;

    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        $admin = User::updateOrCreate(
            ['email' => 'admin@storyloom.test'],
            [
                'name' => 'Platform Admin',
                'role' => 'admin',
                'password' => Hash::make('password'),
            ]
        );

        $writer = User::updateOrCreate(
            ['email' => 'writer@storyloom.test'],
            [
                'name' => 'Aarav Writer',
                'role' => 'writer',
                'password' => Hash::make('password'),
            ]
        );

        $reader = User::updateOrCreate(
            ['email' => 'reader@storyloom.test'],
            [
                'name' => 'Riya Reader',
                'role' => 'reader',
                'password' => Hash::make('password'),
            ]
        );

        $postOne = Post::updateOrCreate(
            ['slug' => 'building-a-writing-habit-that-lasts'],
            [
                'user_id' => $writer->id,
                'title' => 'Building a Writing Habit That Lasts',
                'excerpt' => 'A practical guide for writers who want consistency without burning out.',
                'content' => "Writing gets easier when it becomes routine, not when inspiration magically appears.\n\nStart small. Choose a fixed writing window, remove distractions, and focus on finishing one idea at a time.\n\nA sustainable habit is built through repetition, reflection, and honest revision.",
                'featured_image' => 'https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=1200&q=80',
                'status' => 'published',
                'published_at' => now()->subDays(3),
            ]
        );

        $postTwo = Post::updateOrCreate(
            ['slug' => 'how-blogs-create-real-reader-communities'],
            [
                'user_id' => $writer->id,
                'title' => 'How Blogs Create Real Reader Communities',
                'excerpt' => 'Great blogs do more than publish content. They create conversation and trust.',
                'content' => "A strong blog platform is not only about article publishing.\n\nIt should give readers space to respond, help writers manage their work comfortably, and give admins enough control to keep content clean and useful.\n\nWhen those parts work together, the website feels alive.",
                'featured_image' => 'https://images.unsplash.com/photo-1499750310107-5fef28a66643?auto=format&fit=crop&w=1200&q=80',
                'status' => 'published',
                'published_at' => now()->subDay(),
            ]
        );

        Post::updateOrCreate(
            ['slug' => 'draft-post-for-editorial-review'],
            [
                'user_id' => $writer->id,
                'title' => 'Draft Post for Editorial Review',
                'excerpt' => 'An unpublished draft to demonstrate writer workflow.',
                'content' => "This draft exists so the dashboard shows both published and draft states.\n\nWriters can edit this later and publish it when ready.",
                'featured_image' => null,
                'status' => 'draft',
                'published_at' => null,
            ]
        );

        Comment::updateOrCreate(
            ['post_id' => $postOne->id, 'user_id' => $reader->id],
            [
                'comment' => 'This is a clean example of how a reader can engage with a published article.',
                'status' => 'visible',
            ]
        );

        Comment::updateOrCreate(
            ['post_id' => $postTwo->id, 'user_id' => $admin->id],
            [
                'comment' => 'Admin moderation is ready too, which makes the platform practical for real use.',
                'status' => 'visible',
            ]
        );
    }
}

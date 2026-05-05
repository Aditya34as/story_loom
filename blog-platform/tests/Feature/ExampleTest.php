<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    use RefreshDatabase;

    protected bool $seed = true;

    /**
     * A basic test example.
     */
    public function test_the_application_returns_a_successful_response(): void
    {
        $response = $this->get('/');

        $response->assertStatus(200);
    }

    public function test_articles_page_renders_seeded_content(): void
    {
        $response = $this->get('/posts');

        $response->assertStatus(200);
        $response->assertSee('Building a Writing Habit That Lasts');
    }
}

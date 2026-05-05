<div>
    <label for="title" class="input-label">Post title</label>
    <input type="text" id="title" name="title" value="{{ old('title', isset($post) ? $post->title : '') }}" required class="text-input">
</div>

<div>
    <label for="excerpt" class="input-label">Short excerpt</label>
    <textarea id="excerpt" name="excerpt" required class="text-area min-h-32">{{ old('excerpt', isset($post) ? $post->excerpt : '') }}</textarea>
</div>

<div>
    <label for="content" class="input-label">Full article content</label>
    <textarea id="content" name="content" required class="text-area">{{ old('content', isset($post) ? $post->content : '') }}</textarea>
</div>

<div>
    <label for="featured_image" class="input-label">Featured image URL</label>
    <input type="url" id="featured_image" name="featured_image" value="{{ old('featured_image', isset($post) ? $post->featured_image : '') }}" class="text-input">
</div>

<div>
    <label for="status" class="input-label">Post status</label>
    <select id="status" name="status" required class="select-input">
        <option value="draft" @selected(old('status', isset($post) ? $post->status : 'draft') === 'draft')>Draft</option>
        <option value="published" @selected(old('status', isset($post) ? $post->status : 'draft') === 'published')>Published</option>
    </select>
</div>

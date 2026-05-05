<aside class="surface-card h-fit p-4">
    <a href="{{ route('admin.dashboard') }}" class="dashboard-link {{ request()->routeIs('admin.dashboard') ? 'dashboard-link-active' : '' }}">Overview</a>
    <a href="{{ route('admin.posts.index') }}" class="dashboard-link {{ request()->routeIs('admin.posts.*') ? 'dashboard-link-active' : '' }}">Posts</a>
    <a href="{{ route('admin.comments.index') }}" class="dashboard-link {{ request()->routeIs('admin.comments.*') ? 'dashboard-link-active' : '' }}">Comments</a>
    <a href="{{ route('admin.users.index') }}" class="dashboard-link {{ request()->routeIs('admin.users.*') ? 'dashboard-link-active' : '' }}">Users</a>
    <a href="{{ route('dashboard.posts.index') }}" class="dashboard-link">Writer Area</a>
</aside>

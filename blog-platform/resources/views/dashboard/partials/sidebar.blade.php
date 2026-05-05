<aside class="surface-card h-fit p-4">
    <a href="{{ route('dashboard.posts.index') }}" class="dashboard-link {{ request()->routeIs('dashboard.posts.*') ? 'dashboard-link-active' : '' }}">My Posts</a>
    @if(auth()->user()->isAdmin())
        <a href="{{ route('admin.dashboard') }}" class="dashboard-link">Admin Dashboard</a>
    @endif
</aside>

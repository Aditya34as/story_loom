@extends('layouts.app', ['title' => 'Admin Users'])

@section('content')
    <div class="my-8 grid gap-6 xl:grid-cols-[220px_minmax(0,1fr)]">
        @include('admin.partials.sidebar')

        <section>
            <div class="mb-5 space-y-3">
                <div class="eyebrow">User roles</div>
                <h1 class="section-heading text-4xl">Manage platform users</h1>
            </div>

            <div class="surface-card overflow-hidden">
                <div class="overflow-x-auto">
                    <table class="min-w-full divide-y divide-amber-100">
                        <thead class="bg-amber-50/70">
                            <tr class="text-left text-sm font-semibold text-stone-700">
                                <th class="px-6 py-4">Name</th>
                                <th class="px-6 py-4">Email</th>
                                <th class="px-6 py-4">Current role</th>
                                <th class="px-6 py-4">Change role</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-amber-100 text-sm text-stone-700">
                            @forelse($users as $user)
                                <tr>
                                    <td class="px-6 py-4">{{ $user->name }}</td>
                                    <td class="px-6 py-4">{{ $user->email }}</td>
                                    <td class="px-6 py-4">{{ ucfirst($user->role) }}</td>
                                    <td class="px-6 py-4">
                                        <form action="{{ route('admin.users.role', $user) }}" method="POST" class="flex flex-wrap items-center gap-2">
                                            @csrf
                                            @method('PATCH')
                                            <select name="role" class="select-input max-w-[180px]">
                                                <option value="reader" @selected($user->role === 'reader')>Reader</option>
                                                <option value="writer" @selected($user->role === 'writer')>Writer</option>
                                                <option value="admin" @selected($user->role === 'admin')>Admin</option>
                                            </select>
                                            <button type="submit" class="btn-primary cursor-pointer">Update</button>
                                        </form>
                                    </td>
                                </tr>
                            @empty
                                <tr>
                                    <td colspan="4" class="px-6 py-10 text-center text-stone-600">No users found.</td>
                                </tr>
                            @endforelse
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="mt-4">{{ $users->links() }}</div>
        </section>
    </div>
@endsection

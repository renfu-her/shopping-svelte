<script>
	import { onMount } from 'svelte';
	import { cartStore } from '$lib/stores/cart.js';

	onMount(() => {
		cartStore.load();
	});
</script>

<header>
	<nav>
		<a href="/">首頁</a>
		<a href="/cart">購物車</a>
		<a href="/news">新聞</a>
		<a href="/about">關於我們</a>
		<a href="/faq">FAQ</a>
	</nav>
</header>

<main>
	<slot />
</main>

<footer>
	<p>&copy; 2024 Shopping Cart System</p>
</footer>

<style>
	header {
		background-color: #333;
		color: white;
		padding: 1rem;
	}

	nav {
		display: flex;
		gap: 1rem;
	}

	nav a {
		color: white;
		text-decoration: none;
	}

	nav a:hover {
		text-decoration: underline;
	}

	main {
		min-height: calc(100vh - 200px);
		padding: 2rem;
	}

	footer {
		background-color: #333;
		color: white;
		text-align: center;
		padding: 1rem;
		margin-top: 2rem;
	}
</style>


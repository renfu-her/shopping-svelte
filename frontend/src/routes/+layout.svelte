<script>
	import { onMount } from 'svelte';
	import { cartStore } from '$lib/stores/cart.js';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';

	onMount(() => {
		cartStore.load();
	});
</script>

<Header />

<main>
	<slot />
</main>

<Footer />

<style>
	main {
		min-height: calc(100vh - 300px);
	}
</style>


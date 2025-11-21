<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	$: categorySlug = $page.params.slug;
	
	onMount(() => {
		// 重定向到新的商品列表頁面
		if (categorySlug) {
			goto(`/product?category=${categorySlug}`, { replaceState: true });
		} else {
			goto('/product', { replaceState: true });
		}
	});
</script>

<svelte:head>
	<title>產品列表 - Shopwise</title>
</svelte:head>

<div class="redirecting">
	<p>正在跳轉...</p>
</div>

<style>
	.redirecting {
		text-align: center;
		padding: 4rem;
	}
</style>


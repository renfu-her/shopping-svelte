<script>
	import { goto } from '$app/navigation';

	// 重定向到商品列表頁
	goto('/product', { replaceState: true });
</script>

<svelte:head>
	<title>商店 - Shopwise</title>
</svelte:head>

<div class="redirecting">
	<p>正在跳轉...</p>
</div>


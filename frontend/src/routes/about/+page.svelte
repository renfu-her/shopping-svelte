<script>
	import { onMount } from 'svelte';
	import { getAbout } from '$lib/api.js';

	let about = null;
	let loading = true;
	let error = '';

	onMount(async () => {
		try {
			about = await getAbout();
		} catch (err) {
			error = '無法載入內容';
		} finally {
			loading = false;
		}
	});
</script>

<svelte:head>
	<title>關於我們 - Shopping Cart</title>
</svelte:head>

<div class="about-page">
	{#if loading}
		<p>載入中...</p>
	{:else if error}
		<p>{error}</p>
	{:else if about}
		<h1>{about.title}</h1>
		{#if about.content}
			<div class="content">
				{@html about.content.replace(/\n/g, '<br>')}
			</div>
		{/if}
	{:else}
		<p>目前沒有內容</p>
	{/if}
</div>

<style>
	.about-page {
		max-width: 800px;
		margin: 0 auto;
	}

	h1 {
		margin-bottom: 2rem;
	}

	.content {
		line-height: 1.8;
		font-size: 1.1rem;
	}
</style>


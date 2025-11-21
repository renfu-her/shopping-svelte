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
	<title>關於我們 - Shopwise</title>
</svelte:head>

<div class="about-page">
	<div class="container">
		<div class="breadcrumb">
			<a href="/">首頁</a>
			<span> > </span>
			<span>關於我們</span>
		</div>

		{#if loading}
			<div class="loading">載入中...</div>
		{:else if error}
			<div class="error">
				<p>{error}</p>
			</div>
		{:else if about}
			<div class="about-content">
				<h1>{about.title}</h1>
				{#if about.content}
					<div class="content">
						{@html about.content.replace(/\n/g, '<br>')}
					</div>
				{/if}
			</div>
		{:else}
			<div class="empty-state">
				<p>目前沒有內容</p>
			</div>
		{/if}
	</div>
</div>

<style>
	.about-page {
		background-color: #f8f8f8;
		min-height: calc(100vh - 300px);
		padding: 2rem 0;
	}

	.container {
		max-width: 1000px;
		margin: 0 auto;
		padding: 0 2rem;
	}

	.breadcrumb {
		margin-bottom: 1rem;
		color: #666;
	}

	.breadcrumb a {
		color: #e74c3c;
		text-decoration: none;
	}

	.loading,
	.error,
	.empty-state {
		text-align: center;
		padding: 4rem;
		background-color: white;
		border-radius: 8px;
	}

	.about-content {
		background-color: white;
		padding: 3rem;
		border-radius: 8px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	h1 {
		margin-top: 0;
		margin-bottom: 2rem;
		font-size: 2.5rem;
		border-bottom: 3px solid #e74c3c;
		padding-bottom: 1rem;
	}

	.content {
		line-height: 2;
		font-size: 1.1rem;
		color: #333;
	}
</style>

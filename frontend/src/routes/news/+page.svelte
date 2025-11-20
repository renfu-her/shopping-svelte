<script>
	import { onMount } from 'svelte';
	import { getNews } from '$lib/api.js';

	let news = [];
	let loading = true;

	onMount(async () => {
		try {
			news = await getNews();
		} catch (error) {
			console.error('Failed to load news:', error);
		} finally {
			loading = false;
		}
	});
</script>

<svelte:head>
	<title>新聞 - Shopping Cart</title>
</svelte:head>

<div class="news-page">
	<h1>最新消息</h1>

	{#if loading}
		<p>載入中...</p>
	{:else if news.length === 0}
		<p>目前沒有新聞</p>
	{:else}
		<div class="news-list">
			{#each news as item}
				<article class="news-item">
					{#if item.image_url}
						<img src={item.image_url} alt={item.title} />
					{/if}
					<div class="news-content">
						<h2>{item.title}</h2>
						{#if item.published_at}
							<p class="date">{new Date(item.published_at).toLocaleDateString('zh-TW')}</p>
						{/if}
						{#if item.content}
							<p class="content">{item.content}</p>
						{/if}
					</div>
				</article>
			{/each}
		</div>
	{/if}
</div>

<style>
	.news-page {
		max-width: 1000px;
		margin: 0 auto;
	}

	h1 {
		margin-bottom: 2rem;
	}

	.news-list {
		display: flex;
		flex-direction: column;
		gap: 2rem;
	}

	.news-item {
		display: flex;
		gap: 2rem;
		padding: 2rem;
		border: 1px solid #ddd;
		border-radius: 8px;
	}

	.news-item img {
		width: 200px;
		height: 150px;
		object-fit: cover;
		border-radius: 4px;
		flex-shrink: 0;
	}

	.news-content {
		flex: 1;
	}

	.news-content h2 {
		margin-top: 0;
		margin-bottom: 0.5rem;
	}

	.date {
		color: #666;
		font-size: 0.9rem;
		margin-bottom: 1rem;
	}

	.content {
		line-height: 1.6;
	}

	@media (max-width: 768px) {
		.news-item {
			flex-direction: column;
		}

		.news-item img {
			width: 100%;
		}
	}
</style>


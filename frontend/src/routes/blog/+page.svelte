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
	<title>部落格 - Shopwise</title>
</svelte:head>

<div class="blog-page">
	<div class="container">
		<div class="breadcrumb">
			<a href="/">首頁</a>
			<span> > </span>
			<span>部落格</span>
		</div>

		<h1>部落格</h1>

		{#if loading}
			<div class="loading">載入中...</div>
		{:else if news.length === 0}
			<div class="empty-state">
				<p>目前沒有文章</p>
			</div>
		{:else}
			<div class="blog-grid">
				{#each news as item}
					<article class="blog-card">
						{#if item.image_url}
							<div class="blog-image">
								<img src={item.image_url} alt={item.title} />
							</div>
						{/if}
						<div class="blog-content">
							<h2>{item.title}</h2>
							{#if item.published_at}
								<p class="date">
									{new Date(item.published_at).toLocaleDateString('zh-TW')}
								</p>
							{/if}
							{#if item.content}
								<p class="excerpt">{item.content.substring(0, 150)}...</p>
							{/if}
							<a href="/news" class="read-more">閱讀更多 →</a>
						</div>
					</article>
				{/each}
			</div>
		{/if}
	</div>
</div>

<style>
	.blog-page {
		background-color: #f8f8f8;
		min-height: calc(100vh - 300px);
		padding: 2rem 0;
	}

	.container {
		max-width: 1400px;
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

	h1 {
		margin-bottom: 2rem;
		font-size: 2rem;
	}

	.loading,
	.empty-state {
		text-align: center;
		padding: 4rem;
		background-color: white;
		border-radius: 8px;
	}

	.blog-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
		gap: 2rem;
	}

	.blog-card {
		background-color: white;
		border-radius: 8px;
		overflow: hidden;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
		transition: transform 0.2s, box-shadow 0.2s;
	}

	.blog-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
	}

	.blog-image {
		width: 100%;
		height: 200px;
		overflow: hidden;
	}

	.blog-image img {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	.blog-content {
		padding: 1.5rem;
	}

	.blog-content h2 {
		margin-top: 0;
		margin-bottom: 0.5rem;
		font-size: 1.3rem;
	}

	.date {
		color: #666;
		font-size: 0.9rem;
		margin-bottom: 1rem;
	}

	.excerpt {
		color: #666;
		line-height: 1.6;
		margin-bottom: 1rem;
	}

	.read-more {
		color: #e74c3c;
		text-decoration: none;
		font-weight: 500;
	}

	.read-more:hover {
		text-decoration: underline;
	}
</style>


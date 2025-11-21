<script>
	import { onMount } from 'svelte';
	import { getFAQ } from '$lib/api.js';

	let faqs = [];
	let loading = true;
	let openIndex = null;

	onMount(async () => {
		try {
			faqs = await getFAQ();
		} catch (error) {
			console.error('Failed to load FAQ:', error);
		} finally {
			loading = false;
		}
	});

	function toggle(index) {
		openIndex = openIndex === index ? null : index;
	}
</script>

<svelte:head>
	<title>常見問題 - Shopwise</title>
</svelte:head>

<div class="faq-page">
	<div class="container">
		<div class="breadcrumb">
			<a href="/">首頁</a>
			<span> > </span>
			<span>常見問題</span>
		</div>

		<h1>常見問題</h1>

		{#if loading}
			<div class="loading">載入中...</div>
		{:else if faqs.length === 0}
			<div class="empty-state">
				<p>目前沒有常見問題</p>
			</div>
		{:else}
			<div class="faq-list">
				{#each faqs as faq, index}
					<div class="faq-item">
						<button class="faq-question" on:click={() => toggle(index)}>
							<span>{faq.question}</span>
							<span class="icon">{openIndex === index ? '−' : '+'}</span>
						</button>
						{#if openIndex === index}
							<div class="faq-answer">
								{faq.answer}
							</div>
						{/if}
					</div>
				{/each}
			</div>
		{/if}
	</div>
</div>

<style>
	.faq-page {
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

	.faq-list {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.faq-item {
		background-color: white;
		border-radius: 8px;
		overflow: hidden;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.faq-question {
		width: 100%;
		padding: 1.5rem;
		background-color: white;
		border: none;
		text-align: left;
		cursor: pointer;
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 1.1rem;
		font-weight: 500;
		transition: background-color 0.2s;
	}

	.faq-question:hover {
		background-color: #f8f8f8;
	}

	.icon {
		font-size: 1.5rem;
		font-weight: bold;
		color: #e74c3c;
		min-width: 30px;
		text-align: center;
	}

	.faq-answer {
		padding: 0 1.5rem 1.5rem 1.5rem;
		line-height: 1.8;
		color: #666;
		background-color: #f8f8f8;
	}
</style>

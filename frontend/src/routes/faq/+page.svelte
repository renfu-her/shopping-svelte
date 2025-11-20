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
	<title>常見問題 - Shopping Cart</title>
</svelte:head>

<div class="faq-page">
	<h1>常見問題</h1>

	{#if loading}
		<p>載入中...</p>
	{:else if faqs.length === 0}
		<p>目前沒有常見問題</p>
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

<style>
	.faq-page {
		max-width: 800px;
		margin: 0 auto;
	}

	h1 {
		margin-bottom: 2rem;
	}

	.faq-list {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.faq-item {
		border: 1px solid #ddd;
		border-radius: 8px;
		overflow: hidden;
	}

	.faq-question {
		width: 100%;
		padding: 1.5rem;
		background-color: #f9f9f9;
		border: none;
		text-align: left;
		cursor: pointer;
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 1.1rem;
		font-weight: 500;
	}

	.faq-question:hover {
		background-color: #f0f0f0;
	}

	.icon {
		font-size: 1.5rem;
		font-weight: bold;
		color: #3498db;
	}

	.faq-answer {
		padding: 1.5rem;
		line-height: 1.8;
		background-color: white;
	}
</style>


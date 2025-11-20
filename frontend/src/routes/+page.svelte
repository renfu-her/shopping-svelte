<script>
	import { onMount } from 'svelte';
	import { getAds, getFeaturedProducts, getCategories } from '$lib/api.js';
	import BannerCarousel from '$lib/components/BannerCarousel.svelte';
	import CategorySelector from '$lib/components/CategorySelector.svelte';
	import ProductCard from '$lib/components/ProductCard.svelte';

	let ads = [];
	let featuredProducts = [];
	let categories = [];
	let loading = true;

	onMount(async () => {
		try {
			[ads, featuredProducts, categories] = await Promise.all([
				getAds(),
				getFeaturedProducts(),
				getCategories(),
			]);
		} catch (error) {
			console.error('Failed to load data:', error);
		} finally {
			loading = false;
		}
	});

	function handleCategorySelect(category) {
		if (category && category.slug) {
			window.location.href = `/product/${category.slug}`;
		}
	}
</script>

<svelte:head>
	<title>首頁 - Shopping Cart</title>
</svelte:head>

{#if loading}
	<p>載入中...</p>
{:else}
	<div class="homepage">
		{#if ads.length > 0}
			<BannerCarousel {ads} />
		{/if}

		<div class="category-section">
			<h2>產品分類</h2>
			<CategorySelector {categories} on:select={handleCategorySelect} />
		</div>

		<div class="featured-section">
			<h2>特色產品</h2>
			<div class="products-grid">
				{#each featuredProducts as product}
					<ProductCard {product} />
				{/each}
			</div>
		</div>
	</div>
{/if}

<style>
	.homepage {
		max-width: 1200px;
		margin: 0 auto;
	}

	.category-section,
	.featured-section {
		margin: 3rem 0;
	}

	h2 {
		margin-bottom: 1.5rem;
		font-size: 2rem;
	}

	.products-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
		gap: 2rem;
	}
</style>


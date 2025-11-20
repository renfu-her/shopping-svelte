<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { getProducts, getCategories } from '$lib/api.js';
	import CategoryTree from '$lib/components/CategoryTree.svelte';
	import ProductCard from '$lib/components/ProductCard.svelte';

	let products = { items: [], total: 0, page: 1, pages: 0, per_page: 12 };
	let categories = [];
	let loading = true;
	let currentPage = 1;

	$: categorySlug = $page.params.slug;

	onMount(async () => {
		await loadData();
	});

	async function loadData() {
		loading = true;
		try {
			[categories, products] = await Promise.all([
				getCategories(),
				getProducts(currentPage, 12, categorySlug),
			]);
		} catch (error) {
			console.error('Failed to load data:', error);
		} finally {
			loading = false;
		}
	}

	$: if (categorySlug) {
		loadData();
	}

	function handlePageChange(page) {
		currentPage = page;
		loadData();
		window.scrollTo({ top: 0, behavior: 'smooth' });
	}
</script>

<svelte:head>
	<title>產品列表 - Shopping Cart</title>
</svelte:head>

<div class="product-list-page">
	<div class="sidebar">
		<CategoryTree {categories} currentSlug={categorySlug} />
	</div>

	<div class="content">
		{#if loading}
			<p>載入中...</p>
		{:else if products.items.length === 0}
			<p>沒有找到產品</p>
		{:else}
			<div class="products-grid">
				{#each products.items as product}
					<ProductCard {product} />
				{/each}
			</div>

			{#if products.pages > 1}
				<div class="pagination">
					<button
						disabled={currentPage === 1}
						on:click={() => handlePageChange(currentPage - 1)}
					>
						上一頁
					</button>
					<span>第 {currentPage} 頁 / 共 {products.pages} 頁</span>
					<button
						disabled={currentPage === products.pages}
						on:click={() => handlePageChange(currentPage + 1)}
					>
						下一頁
					</button>
				</div>
			{/if}
		{/if}
	</div>
</div>

<style>
	.product-list-page {
		display: flex;
		gap: 2rem;
		max-width: 1200px;
		margin: 0 auto;
	}

	.sidebar {
		width: 250px;
		flex-shrink: 0;
	}

	.content {
		flex: 1;
	}

	.products-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
		gap: 2rem;
		margin-bottom: 2rem;
	}

	.pagination {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 1rem;
		margin-top: 2rem;
	}

	.pagination button {
		padding: 0.5rem 1rem;
		border: 1px solid #ddd;
		background-color: white;
		cursor: pointer;
		border-radius: 4px;
	}

	.pagination button:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.pagination button:hover:not(:disabled) {
		background-color: #f0f0f0;
	}
</style>


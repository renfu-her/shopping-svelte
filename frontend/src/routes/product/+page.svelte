<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { getProducts, getCategories } from '$lib/api.js';
	import CategoryTree from '$lib/components/CategoryTree.svelte';
	import ProductCard from '$lib/components/ProductCard.svelte';
	import { goto } from '$app/navigation';

	let products = { items: [], total: 0, page: 1, pages: 0, per_page: 12 };
	let categories = [];
	let loading = true;
	let currentPage = 1;
	let sortBy = 'default';
	let viewMode = 'grid';

	$: categorySlug = $page.url.searchParams.get('category') || null;
	$: searchQuery = $page.url.searchParams.get('search') || '';

	onMount(async () => {
		await loadData();
	});

	async function loadData() {
		loading = true;
		try {
			[categories, products] = await Promise.all([
				getCategories(),
				getProducts(currentPage, 12, categorySlug, searchQuery || null),
			]);
		} catch (error) {
			console.error('Failed to load data:', error);
		} finally {
			loading = false;
		}
	}

	$: if (categorySlug || searchQuery) {
		currentPage = 1;
		loadData();
	}

	function handlePageChange(page) {
		currentPage = page;
		loadData();
		window.scrollTo({ top: 0, behavior: 'smooth' });
	}

	function handleCategoryClick(category) {
		if (category && category.level === 3) {
			goto(`/product?category=${category.slug}`);
		}
	}
</script>

<svelte:head>
	<title>商品列表 - Shopwise</title>
</svelte:head>

<div class="product-list-page">
	<!-- Breadcrumb Section -->
	<div class="breadcrumb-section">
		<div class="container">
			<div class="breadcrumb-content">
				<div class="page-title">
					<h1>Shop Left Sidebar</h1>
				</div>
				<ol class="breadcrumb">
					<li class="breadcrumb-item"><a href="/">Home</a></li>
					<li class="breadcrumb-item"><a href="/product">Pages</a></li>
					<li class="breadcrumb-item active">Shop Left Sidebar</li>
				</ol>
			</div>
		</div>
	</div>

	<div class="container">

		<div class="page-layout">
			<!-- Left Sidebar -->
			<aside class="sidebar">
				<div class="sidebar-section">
					<h3>分類</h3>
					<CategoryTree {categories} currentSlug={categorySlug} useQueryParam={true} on:click={handleCategoryClick} />
				</div>

				<div class="sidebar-section">
					<h3>篩選</h3>
					<div class="filter-group">
						<label for="price-range-min">價格範圍</label>
						<div class="price-range">
							<input type="range" id="price-range-min" min="0" max="10000" value="0" />
							<input type="range" id="price-range-max" min="0" max="10000" value="10000" />
							<div class="price-display">NT$ 0 - NT$ 10,000</div>
						</div>
					</div>
				</div>
			</aside>

			<!-- Main Content -->
			<main class="content">
				<!-- Toolbar -->
				<div class="toolbar">
					<div class="toolbar-left">
						<select bind:value={sortBy} class="sort-select">
							<option value="default">預設排序</option>
							<option value="price-asc">價格：低到高</option>
							<option value="price-desc">價格：高到低</option>
							<option value="name-asc">名稱：A-Z</option>
						</select>
					</div>
					<div class="toolbar-right">
						<div class="view-toggle">
							<button
								class="view-btn {viewMode === 'grid' ? 'active' : ''}"
								on:click={() => viewMode = 'grid'}
								title="Grid View"
							>
								⊞
							</button>
							<button
								class="view-btn {viewMode === 'list' ? 'active' : ''}"
								on:click={() => viewMode = 'list'}
								title="List View"
							>
								☰
							</button>
						</div>
						<select class="showing-select">
							<option value="12">Showing 12</option>
							<option value="24">Showing 24</option>
							<option value="36">Showing 36</option>
						</select>
					</div>
				</div>

				<!-- Products Grid -->
				{#if loading}
					<div class="loading">載入中...</div>
				{:else if products.items.length === 0}
					<div class="empty-state">
						<p>沒有找到商品</p>
						<a href="/product">瀏覽所有商品</a>
					</div>
				{:else}
					<div class="products-grid" class:list-view={viewMode === 'list'}>
						{#each products.items as product}
							<ProductCard {product} listView={viewMode === 'list'} />
						{/each}
					</div>

					<!-- Pagination -->
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
			</main>
		</div>
	</div>
</div>

<style>
	.product-list-page {
		background-color: #f8f8f8;
		min-height: calc(100vh - 300px);
	}

	.breadcrumb-section {
		background-color: #f8f8f8;
		padding: 1.5rem 0;
		border-bottom: 1px solid #eee;
	}

	.breadcrumb-content {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.page-title h1 {
		margin: 0;
		font-size: 1.75rem;
		font-weight: bold;
		color: #333;
	}

	.breadcrumb {
		display: flex;
		list-style: none;
		padding: 0;
		margin: 0;
		gap: 0.5rem;
		align-items: center;
	}

	.breadcrumb-item {
		color: #666;
	}

	.breadcrumb-item:not(:last-child)::after {
		content: '>';
		margin-left: 0.5rem;
		color: #999;
	}

	.breadcrumb-item a {
		color: #e74c3c;
		text-decoration: none;
	}

	.breadcrumb-item.active {
		color: #333;
	}

	.container {
		max-width: 1400px;
		margin: 0 auto;
		padding: 2rem;
	}

	.page-layout {
		display: flex;
		gap: 2rem;
	}

	.sidebar {
		width: 280px;
		flex-shrink: 0;
	}

	.sidebar-section {
		background-color: white;
		padding: 1.5rem;
		margin-bottom: 1.5rem;
		border-radius: 8px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.sidebar-section h3 {
		margin-top: 0;
		margin-bottom: 1rem;
		font-size: 1.2rem;
		border-bottom: 2px solid #e74c3c;
		padding-bottom: 0.5rem;
	}

	.filter-group {
		margin-top: 1rem;
	}

	.filter-group label {
		display: block;
		margin-bottom: 0.5rem;
		font-weight: 500;
	}

	.price-range {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.price-display {
		text-align: center;
		color: #e74c3c;
		font-weight: bold;
	}

	.content {
		flex: 1;
		background-color: white;
		padding: 2rem;
		border-radius: 8px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.toolbar {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 2rem;
		padding-bottom: 1rem;
		border-bottom: 1px solid #eee;
	}

	.sort-select {
		padding: 0.5rem 1rem;
		border: 1px solid #ddd;
		border-radius: 4px;
		cursor: pointer;
	}

	.toolbar-right {
		display: flex;
		align-items: center;
		gap: 1rem;
	}

	.view-toggle {
		display: flex;
		gap: 0.5rem;
	}

	.view-btn {
		padding: 0.5rem 1rem;
		border: 1px solid #ddd;
		background-color: white;
		cursor: pointer;
		border-radius: 4px;
		font-size: 1.2rem;
	}

	.view-btn.active {
		background-color: #e74c3c;
		color: white;
		border-color: #e74c3c;
	}

	.showing-select {
		padding: 0.5rem 1rem;
		border: 1px solid #ddd;
		border-radius: 4px;
		background-color: white;
		cursor: pointer;
		font-size: 0.9rem;
	}

	.products-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
		gap: 2rem;
	}

	.products-grid.list-view {
		grid-template-columns: 1fr;
	}

	.loading,
	.empty-state {
		text-align: center;
		padding: 4rem;
	}

	.empty-state a {
		color: #e74c3c;
		text-decoration: none;
	}

	.pagination {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 1rem;
		margin-top: 3rem;
		padding-top: 2rem;
		border-top: 1px solid #eee;
	}

	.pagination button {
		padding: 0.75rem 1.5rem;
		border: 1px solid #ddd;
		background-color: white;
		cursor: pointer;
		border-radius: 4px;
		transition: all 0.2s;
	}

	.pagination button:hover:not(:disabled) {
		background-color: #e74c3c;
		color: white;
		border-color: #e74c3c;
	}

	.pagination button:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	@media (max-width: 968px) {
		.page-layout {
			flex-direction: column;
		}

		.sidebar {
			width: 100%;
		}
	}
</style>


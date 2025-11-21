<script>
	import { onMount } from 'svelte';
	import { getAds, getFeaturedProducts, getCategories, getProducts } from '$lib/api.js';
	import BannerCarousel from '$lib/components/BannerCarousel.svelte';
	import ProductCard from '$lib/components/ProductCard.svelte';
	import { goto } from '$app/navigation';

	let ads = [];
	let featuredProducts = [];
	let categories = [];
	let loading = true;
	let activeTab = 'featured';
	let tabProducts = { featured: [], newArrival: [], bestSellers: [], specialOffer: [] };

	onMount(async () => {
		try {
			[ads, featuredProducts, categories] = await Promise.all([
				getAds(),
				getFeaturedProducts(),
				getCategories(),
			]);
			// Load products for different tabs
			await loadTabProducts();
		} catch (error) {
			console.error('Failed to load data:', error);
		} finally {
			loading = false;
		}
	});

	async function loadTabProducts() {
		try {
			// For now, use featured products for all tabs
			// In a real app, you'd have separate API endpoints for each tab
			const result = await getProducts(1, 8);
			tabProducts.featured = featuredProducts.slice(0, 8);
			tabProducts.newArrival = result.items.slice(0, 8);
			tabProducts.bestSellers = result.items.slice(0, 8);
			tabProducts.specialOffer = result.items.slice(0, 8);
		} catch (error) {
			console.error('Failed to load tab products:', error);
		}
	}

	function handleCategoryClick(category) {
		if (category && category.slug) {
			if (category.level === 3) {
				goto(`/product?category=${category.slug}`);
			} else {
				goto(`/product`);
			}
		}
	}

	function switchTab(tab) {
		activeTab = tab;
	}
</script>

<svelte:head>
	<title>首頁 - Shopwise</title>
</svelte:head>

<div class="homepage">
	{#if loading}
		<div class="loading">載入中...</div>
	{:else}
		<!-- Banner Section -->
		{#if ads.length > 0}
			<section class="banner-section">
				<BannerCarousel {ads} />
			</section>
		{/if}

		<!-- Promotional Banners -->
		<section class="promo-banners-section">
			<div class="container">
				<div class="promo-banners">
					<div class="promo-banner">
						<a href="/product" class="promo-link">
							<div class="promo-content">
								<h3>Headphone</h3>
								<h2>Music</h2>
								<span class="promo-link-text">View Collection</span>
							</div>
						</a>
					</div>
					<div class="promo-banner promo-banner-blue">
						<a href="/product" class="promo-link">
							<div class="promo-content">
								<h3>Up to 35% OFF</h3>
								<h2>Camera</h2>
								<span class="promo-link-text">Show Now</span>
							</div>
						</a>
					</div>
					<div class="promo-banner promo-banner-beige">
						<a href="/product" class="promo-link">
							<div class="promo-content">
								<h3>Sale Offer 20% OFF This Week</h3>
								<h2>Watch</h2>
								<span class="promo-link-text">View Collection</span>
							</div>
						</a>
					</div>
				</div>
			</div>
		</section>

		<!-- Top Categories Section -->
		{#if categories.length > 0}
			<section class="categories-section">
				<div class="container">
					<div class="section-header">
						<h2>Top Categories</h2>
						<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus blandit massa enim Nullam nunc varius.</p>
					</div>
					<div class="categories-slider">
						{#each categories.slice(0, 7) as category}
							<div 
								class="category-card" 
								role="button"
								tabindex="0"
								on:click={() => handleCategoryClick(category)}
								on:keydown={(e) => e.key === 'Enter' || e.key === ' ' ? handleCategoryClick(category) : null}
							>
								<div class="category-icon-large">📁</div>
								<span>{category.name}</span>
							</div>
						{/each}
					</div>
				</div>
			</section>
		{/if}

		<!-- Exclusive Products Section -->
		<section class="exclusive-products-section">
			<div class="container">
				<div class="section-header">
					<h2>Exclusive Products</h2>
				</div>
				<div class="tabs">
					<button 
						class="tab-btn {activeTab === 'newArrival' ? 'active' : ''}"
						on:click={() => switchTab('newArrival')}
					>
						New Arrival
					</button>
					<button 
						class="tab-btn {activeTab === 'bestSellers' ? 'active' : ''}"
						on:click={() => switchTab('bestSellers')}
					>
						Best Sellers
					</button>
					<button 
						class="tab-btn {activeTab === 'featured' ? 'active' : ''}"
						on:click={() => switchTab('featured')}
					>
						Featured
					</button>
					<button 
						class="tab-btn {activeTab === 'specialOffer' ? 'active' : ''}"
						on:click={() => switchTab('specialOffer')}
					>
						Special Offer
					</button>
				</div>
				<div class="tab-content">
					{#if activeTab === 'featured' && tabProducts.featured.length > 0}
						<div class="products-grid">
							{#each tabProducts.featured as product}
								<ProductCard {product} />
							{/each}
						</div>
					{:else if activeTab === 'newArrival' && tabProducts.newArrival.length > 0}
						<div class="products-grid">
							{#each tabProducts.newArrival as product}
								<ProductCard {product} />
							{/each}
						</div>
					{:else if activeTab === 'bestSellers' && tabProducts.bestSellers.length > 0}
						<div class="products-grid">
							{#each tabProducts.bestSellers as product}
								<ProductCard {product} />
							{/each}
						</div>
					{:else if activeTab === 'specialOffer' && tabProducts.specialOffer.length > 0}
						<div class="products-grid">
							{#each tabProducts.specialOffer as product}
								<ProductCard {product} />
							{/each}
						</div>
					{:else}
						<div class="empty-state">
							<p>暫無商品</p>
						</div>
					{/if}
				</div>
			</div>
		</section>
	{/if}
</div>

<style>
	.homepage {
		width: 100%;
		background-color: #f8f8f8;
	}

	.loading {
		text-align: center;
		padding: 4rem;
		font-size: 1.5rem;
	}

	.container {
		max-width: 1400px;
		margin: 0 auto;
		padding: 0 2rem;
	}

	/* Banner Section */
	.banner-section {
		margin-bottom: 2rem;
	}

	/* Promotional Banners */
	.promo-banners-section {
		padding: 2rem 0;
		background-color: #fff;
	}

	.promo-banners {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2rem;
	}

	.promo-banner {
		position: relative;
		height: 200px;
		border-radius: 8px;
		overflow: hidden;
		background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
		display: flex;
		align-items: center;
		justify-content: center;
		transition: transform 0.3s;
	}

	.promo-banner:hover {
		transform: translateY(-5px);
	}

	.promo-banner-blue {
		background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
	}

	.promo-banner-beige {
		background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
	}

	.promo-link {
		text-decoration: none;
		color: inherit;
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.promo-content {
		text-align: center;
		color: #333;
	}

	.promo-content h3 {
		margin: 0 0 0.5rem 0;
		font-size: 1rem;
		font-weight: 500;
	}

	.promo-content h2 {
		margin: 0 0 1rem 0;
		font-size: 2rem;
		font-weight: bold;
	}

	.promo-link-text {
		text-decoration: underline;
		font-size: 0.9rem;
	}

	/* Categories Section */
	.categories-section {
		padding: 3rem 0;
		background-color: #fff;
	}

	.section-header {
		text-align: center;
		margin-bottom: 2rem;
	}

	.section-header h2 {
		font-size: 2rem;
		font-weight: bold;
		margin-bottom: 0.5rem;
		color: #333;
	}

	.section-header p {
		color: #666;
		max-width: 600px;
		margin: 0 auto;
	}

	.categories-slider {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
		gap: 2rem;
	}

	.category-card {
		text-align: center;
		padding: 2rem 1rem;
		background-color: #f8f8f8;
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.3s;
	}

	.category-card:hover {
		background-color: #fff;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
		transform: translateY(-5px);
	}

	.category-icon-large {
		font-size: 3rem;
		margin-bottom: 1rem;
	}

	.category-card span {
		display: block;
		font-weight: 500;
		color: #333;
	}

	/* Exclusive Products Section */
	.exclusive-products-section {
		padding: 3rem 0;
		background-color: #fff;
	}

	.tabs {
		display: flex;
		justify-content: center;
		gap: 1rem;
		margin-bottom: 3rem;
		border-bottom: 2px solid #eee;
		position: relative;
	}

	.tab-btn {
		padding: 1rem 2rem;
		background: none;
		border: none;
		border-bottom: 3px solid transparent;
		cursor: pointer;
		font-size: 1rem;
		font-weight: 500;
		color: #666;
		transition: all 0.3s;
		position: relative;
		bottom: -2px;
	}

	.tab-btn:hover {
		color: #e74c3c;
	}

	.tab-btn.active {
		color: #e74c3c;
		border-bottom-color: #e74c3c;
	}

	.tab-content {
		min-height: 400px;
	}

	.products-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
		gap: 2rem;
	}

	.empty-state {
		text-align: center;
		padding: 4rem;
		color: #666;
	}

	@media (max-width: 992px) {
		.promo-banners {
			grid-template-columns: 1fr;
		}

		.categories-slider {
			grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
		}

		.tabs {
			flex-wrap: wrap;
		}

		.tab-btn {
			padding: 0.75rem 1rem;
			font-size: 0.9rem;
		}
	}
</style>

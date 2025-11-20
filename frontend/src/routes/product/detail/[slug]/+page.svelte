<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { getProduct } from '$lib/api.js';
	import { cartStore } from '$lib/stores/cart.js';

	let product = null;
	let loading = true;
	let error = '';

	$: slug = $page.params.slug;

	onMount(async () => {
		await loadProduct();
	});

	async function loadProduct() {
		loading = true;
		error = '';
		try {
			product = await getProduct(slug);
		} catch (err) {
			error = '產品不存在';
		} finally {
			loading = false;
		}
	}

	function handleAddToCart() {
		if (product) {
			cartStore.addItem(product.id, 1);
			alert('已加入購物車');
		}
	}
</script>

<svelte:head>
	<title>{product ? product.name : '產品詳情'} - Shopping Cart</title>
</svelte:head>

<div class="product-detail-page">
	{#if loading}
		<p>載入中...</p>
	{:else if error}
		<p>{error}</p>
		<a href="/">返回首頁</a>
	{:else if product}
		<div class="product-detail">
			<div class="product-image">
				{#if product.image_url}
					<img src={product.image_url} alt={product.name} />
				{:else}
					<div class="no-image">無圖片</div>
				{/if}
			</div>
			<div class="product-info">
				<h1>{product.name}</h1>
				<p class="price">NT$ {product.price.toLocaleString()}</p>
				<p class="stock">庫存: {product.stock}</p>
				{#if product.description}
					<div class="description">
						<h2>產品描述</h2>
						<p>{product.description}</p>
					</div>
				{/if}
				<button class="add-to-cart-btn" on:click={handleAddToCart} disabled={product.stock === 0}>
					{product.stock === 0 ? '已售完' : '加入購物車'}
				</button>
			</div>
		</div>
	{/if}
</div>

<style>
	.product-detail-page {
		max-width: 1200px;
		margin: 0 auto;
	}

	.product-detail {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 3rem;
	}

	.product-image {
		width: 100%;
	}

	.product-image img {
		width: 100%;
		height: auto;
		border-radius: 8px;
	}

	.no-image {
		width: 100%;
		aspect-ratio: 1;
		background-color: #f0f0f0;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #999;
		border-radius: 8px;
	}

	.product-info h1 {
		margin-top: 0;
		font-size: 2rem;
	}

	.price {
		font-size: 2rem;
		font-weight: bold;
		color: #e74c3c;
		margin: 1rem 0;
	}

	.stock {
		font-size: 1.2rem;
		margin: 1rem 0;
	}

	.description {
		margin: 2rem 0;
	}

	.description h2 {
		font-size: 1.5rem;
		margin-bottom: 1rem;
	}

	.add-to-cart-btn {
		width: 100%;
		padding: 1rem 2rem;
		background-color: #3498db;
		color: white;
		border: none;
		border-radius: 4px;
		font-size: 1.2rem;
		cursor: pointer;
		margin-top: 2rem;
	}

	.add-to-cart-btn:hover:not(:disabled) {
		background-color: #2980b9;
	}

	.add-to-cart-btn:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	@media (max-width: 768px) {
		.product-detail {
			grid-template-columns: 1fr;
		}
	}
</style>


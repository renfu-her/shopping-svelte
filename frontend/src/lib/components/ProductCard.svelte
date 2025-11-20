<script>
	import { cartStore } from '$lib/stores/cart.js';

	export let product;

	function handleAddToCart() {
		cartStore.addItem(product.id, 1);
		alert('已加入購物車');
	}
</script>

<div class="product-card">
	<a href="/product/detail/{product.slug}">
		{#if product.image_url}
			<img src={product.image_url} alt={product.name} />
		{:else}
			<div class="no-image">無圖片</div>
		{/if}
		<h3>{product.name}</h3>
		<p class="price">NT$ {product.price.toLocaleString()}</p>
	</a>
	<button on:click={handleAddToCart}>加入購物車</button>
</div>

<style>
	.product-card {
		border: 1px solid #ddd;
		border-radius: 8px;
		overflow: hidden;
		transition: transform 0.2s, box-shadow 0.2s;
	}

	.product-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
	}

	.product-card a {
		text-decoration: none;
		color: inherit;
		display: block;
	}

	.product-card img {
		width: 100%;
		height: 200px;
		object-fit: cover;
	}

	.no-image {
		width: 100%;
		height: 200px;
		background-color: #f0f0f0;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #999;
	}

	.product-card h3 {
		padding: 1rem;
		margin: 0;
		font-size: 1.2rem;
	}

	.price {
		padding: 0 1rem;
		font-size: 1.5rem;
		font-weight: bold;
		color: #e74c3c;
		margin: 0.5rem 0;
	}

	.product-card button {
		width: 100%;
		padding: 0.75rem;
		background-color: #3498db;
		color: white;
		border: none;
		cursor: pointer;
		font-size: 1rem;
		transition: background-color 0.2s;
	}

	.product-card button:hover {
		background-color: #2980b9;
	}
</style>


<script>
	import { cartStore } from '$lib/stores/cart.js';

	export let product;
	export let listView = false; // Add view mode prop

	function handleAddToCart(e) {
		e.preventDefault(); // Prevent navigation
		cartStore.addItem(product.id, 1);
		alert('已加入購物車');
	}
</script>

<div class="product-card {listView ? 'list-view' : ''}">
	<a href="/product/detail/{product.slug}" class="card-link">
		<div class="product-image-wrapper">
			{#if product.image_url}
				<img src={product.image_url} alt={product.name} />
			{:else}
				<div class="no-image">無圖片</div>
			{/if}
			{#if product.feature_product}
				<span class="badge">特色</span>
			{/if}
		</div>
		<div class="product-info">
			<div class="info-header">
				<h3>{product.name}</h3>
				{#if listView && product.description}
					<p class="description">{product.description}</p>
				{/if}
			</div>
			
			<div class="info-footer">
				<div class="price-section">
					<span class="current-price">NT$ {product.price.toLocaleString()}</span>
				</div>
				
				{#if listView}
					<div class="actions">
						<button class="add-to-cart-btn" on:click={handleAddToCart}>
							加入購物車
						</button>
						<button class="icon-btn" title="加入願望清單">❤️</button>
						<button class="icon-btn" title="比較">⇄</button>
					</div>
				{/if}
			</div>
		</div>
	</a>
	
	{#if !listView}
		<button class="add-to-cart-btn grid-btn" on:click={handleAddToCart}>
			加入購物車
		</button>
	{/if}
</div>

<style>
	.product-card {
		background-color: white;
		border: 1px solid #eee;
		border-radius: 8px;
		overflow: hidden;
		transition: transform 0.2s, box-shadow 0.2s;
		display: flex;
		flex-direction: column;
		height: 100%;
	}

	.product-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
	}

	.card-link {
		text-decoration: none;
		color: inherit;
		display: flex;
		flex-direction: column;
		flex: 1;
	}

	.product-image-wrapper {
		position: relative;
		width: 100%;
		height: 250px;
		overflow: hidden;
		background-color: #f8f8f8;
		flex-shrink: 0;
	}

	.product-image-wrapper img {
		width: 100%;
		height: 100%;
		object-fit: cover;
		transition: transform 0.3s;
	}

	.product-card:hover .product-image-wrapper img {
		transform: scale(1.05);
	}

	.no-image {
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #999;
		background-color: #f0f0f0;
	}

	.badge {
		position: absolute;
		top: 10px;
		left: 10px;
		background-color: #e74c3c;
		color: white;
		padding: 0.25rem 0.75rem;
		border-radius: 4px;
		font-size: 0.75rem;
		font-weight: bold;
	}

	.product-info {
		padding: 1.5rem;
		flex: 1;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}

	.product-info h3 {
		margin: 0 0 0.5rem 0;
		font-size: 1.1rem;
		font-weight: 500;
		color: #333;
		line-height: 1.4;
		/* Line clamping for grid view */
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}

	.price-section {
		margin-top: auto;
	}

	.current-price {
		font-size: 1.25rem;
		font-weight: bold;
		color: #e74c3c;
	}

	.add-to-cart-btn {
		background-color: #e74c3c;
		color: white;
		border: none;
		cursor: pointer;
		font-size: 1rem;
		font-weight: 500;
		transition: background-color 0.2s;
	}

	.add-to-cart-btn:hover {
		background-color: #c0392b;
	}

	.grid-btn {
		width: 100%;
		padding: 0.75rem;
		margin-top: auto;
	}

	/* List View Styles */
	.product-card.list-view {
		flex-direction: row;
		height: auto;
	}

	.product-card.list-view:hover {
		transform: none; /* Disable translation in list view */
	}

	.product-card.list-view .card-link {
		flex-direction: row;
	}

	.product-card.list-view .product-image-wrapper {
		width: 250px;
		height: 200px;
	}

	.product-card.list-view .product-info {
		padding: 1.5rem 2rem;
	}

	.product-card.list-view h3 {
		font-size: 1.4rem;
		margin-bottom: 1rem;
		-webkit-line-clamp: unset; /* Show full title */
	}

	.product-card.list-view .description {
		color: #666;
		line-height: 1.6;
		margin-bottom: 1.5rem;
		display: -webkit-box;
		-webkit-line-clamp: 3;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}

	.product-card.list-view .info-footer {
		display: flex;
		justify-content: space-between;
		align-items: center;
		border-top: 1px solid #eee;
		padding-top: 1rem;
		margin-top: 1rem;
	}

	.product-card.list-view .current-price {
		font-size: 1.5rem;
	}

	.product-card.list-view .actions {
		display: flex;
		gap: 1rem;
	}

	.product-card.list-view .add-to-cart-btn {
		padding: 0.5rem 1.5rem;
		border-radius: 4px;
	}

	.product-card.list-view .icon-btn {
		width: 40px;
		height: 40px;
		border: 1px solid #ddd;
		background-color: white;
		border-radius: 4px;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 1.2rem;
		color: #666;
		transition: all 0.2s;
	}

	.product-card.list-view .icon-btn:hover {
		background-color: #e74c3c;
		color: white;
		border-color: #e74c3c;
	}

	@media (max-width: 768px) {
		.product-card.list-view .card-link {
			flex-direction: column;
		}

		.product-card.list-view .product-image-wrapper {
			width: 100%;
			height: 200px;
		}

		.product-card.list-view .info-footer {
			flex-direction: column;
			gap: 1rem;
			align-items: flex-start;
		}
	}
</style>

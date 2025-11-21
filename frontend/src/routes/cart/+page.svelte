<script>
	import { onMount } from 'svelte';
	import { cartStore } from '$lib/stores/cart.js';
	import { goto } from '$app/navigation';

	let cart = { items: [], total_amount: 0 };

	cartStore.subscribe((value) => {
		cart = value;
	});

	onMount(() => {
		cartStore.load();
	});

	function handleUpdateQuantity(itemId, quantity) {
		if (quantity <= 0) {
			cartStore.removeItem(itemId);
		} else {
			cartStore.updateItem(itemId, quantity);
		}
	}

	function handleRemoveItem(itemId) {
		if (confirm('確定要移除這個商品嗎？')) {
			cartStore.removeItem(itemId);
		}
	}

	function handleCheckout() {
		if (cart.items.length === 0) {
			alert('購物車是空的');
			return;
		}
		goto('/checkout');
	}
</script>

<svelte:head>
	<title>購物車 - Shopwise</title>
</svelte:head>

<div class="cart-page">
	<!-- Breadcrumb Section -->
	<div class="breadcrumb-section">
		<div class="container">
			<div class="breadcrumb-content">
				<div class="page-title">
					<h1>Shopping Cart</h1>
				</div>
				<ol class="breadcrumb">
					<li class="breadcrumb-item"><a href="/">Home</a></li>
					<li class="breadcrumb-item"><a href="/product">Pages</a></li>
					<li class="breadcrumb-item active">Shopping Cart</li>
				</ol>
			</div>
		</div>
	</div>

	<div class="container">

		{#if cart.loading}
			<div class="loading">載入中...</div>
		{:else if cart.items.length === 0}
			<div class="empty-cart">
				<p>購物車是空的</p>
				<a href="/product" class="continue-shopping-btn">繼續購物</a>
			</div>
		{:else}
			<div class="cart-content">
				<div class="cart-items">
					<table class="cart-table">
						<thead>
							<tr>
								<th class="product-thumbnail">&nbsp;</th>
								<th class="product-name">Product</th>
								<th class="product-price">Price</th>
								<th class="product-quantity">Quantity</th>
								<th class="product-subtotal">Total</th>
								<th class="product-remove">Remove</th>
							</tr>
						</thead>
						<tbody>
							{#each cart.items as item}
								<tr>
									<td class="product-thumbnail">
										<a href="/product/detail/{item.product.slug}">
											{#if item.product.image_url}
												<img src={item.product.image_url} alt={item.product.name} />
											{:else}
												<div class="no-image">無圖片</div>
											{/if}
										</a>
									</td>
									<td class="product-name" data-title="Product">
										<a href="/product/detail/{item.product.slug}">{item.product.name}</a>
									</td>
									<td class="product-price" data-title="Price">NT$ {item.product.price.toLocaleString()}</td>
									<td class="product-quantity" data-title="Quantity">
										<div class="quantity">
											<button class="minus" on:click={() => handleUpdateQuantity(item.id, item.quantity - 1)}>-</button>
											<input type="text" value={item.quantity} readonly class="qty" size="4" />
											<button class="plus" on:click={() => handleUpdateQuantity(item.id, item.quantity + 1)}>+</button>
										</div>
									</td>
									<td class="product-subtotal" data-title="Total">NT$ {(item.product.price * item.quantity).toLocaleString()}</td>
									<td class="product-remove" data-title="Remove">
										<a href="#" class="item-remove" on:click|preventDefault={() => handleRemoveItem(item.id)}>×</a>
									</td>
								</tr>
							{/each}
						</tbody>
						<tfoot>
							<tr>
								<td colspan="6" class="px-0">
									<div class="cart-footer-actions">
										<div class="coupon-section">
											<input type="text" class="coupon-input" placeholder="Enter Coupon Code.." />
											<button class="apply-coupon-btn">Apply Coupon</button>
										</div>
										<button class="update-cart-btn">Update Cart</button>
									</div>
								</td>
							</tr>
						</tfoot>
					</table>
				</div>

				<div class="cart-summary">
					<div class="summary-card">
						<h3>訂單摘要</h3>
						<div class="summary-row">
							<span>小計</span>
							<span>NT$ {cart.total_amount.toLocaleString()}</span>
						</div>
						<div class="summary-row">
							<span>運費</span>
							<span>免費</span>
						</div>
						<div class="summary-row total">
							<span><strong>總計</strong></span>
							<span><strong>NT$ {cart.total_amount.toLocaleString()}</strong></span>
						</div>
						<div class="cart-buttons">
							<a href="/cart" class="view-cart-btn">View Cart</a>
							<button class="checkout-btn" on:click={handleCheckout}>Checkout</button>
						</div>
					</div>
				</div>
			</div>
		{/if}
	</div>
</div>

<style>
	.cart-page {
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

	.loading,
	.empty-cart {
		text-align: center;
		padding: 4rem;
		background-color: white;
		border-radius: 8px;
	}

	.empty-cart p {
		font-size: 1.5rem;
		margin-bottom: 2rem;
	}

	.continue-shopping-btn {
		display: inline-block;
		padding: 1rem 2rem;
		background-color: #e74c3c;
		color: white;
		text-decoration: none;
		border-radius: 4px;
		font-weight: bold;
	}

	.continue-shopping-btn:hover {
		background-color: #c0392b;
	}

	.cart-content {
		display: grid;
		grid-template-columns: 1fr 350px;
		gap: 2rem;
	}

	.cart-items {
		background-color: white;
		padding: 2rem;
		border-radius: 8px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.cart-table {
		width: 100%;
		border-collapse: collapse;
	}

	.cart-table thead {
		border-bottom: 2px solid #eee;
	}

	.cart-table th {
		padding: 1rem;
		text-align: left;
		font-weight: 600;
		color: #666;
	}

	.cart-table td {
		padding: 1.5rem 1rem;
		border-bottom: 1px solid #eee;
		vertical-align: middle;
	}

	.product-thumbnail {
		width: 120px;
	}

	.product-thumbnail img {
		width: 80px;
		height: 80px;
		object-fit: cover;
		border-radius: 4px;
	}

	.product-name {
		width: 30%;
	}

	.product-name a {
		color: #333;
		text-decoration: none;
		font-weight: 500;
	}

	.product-name a:hover {
		color: #e74c3c;
	}

	.no-image {
		width: 80px;
		height: 80px;
		background-color: #f0f0f0;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #999;
		border-radius: 4px;
		font-size: 0.75rem;
	}

	.product-info h3 {
		margin: 0;
		font-size: 1rem;
	}

	.price-cell,
	.subtotal-cell {
		font-weight: bold;
		color: #e74c3c;
	}

	.quantity {
		display: flex;
		align-items: center;
		gap: 0;
	}

	.quantity .minus,
	.quantity .plus {
		width: 30px;
		height: 30px;
		border: 1px solid #ddd;
		background-color: white;
		cursor: pointer;
		font-size: 1.2rem;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.quantity .minus:hover,
	.quantity .plus:hover {
		background-color: #f0f0f0;
	}

	.quantity .qty {
		width: 50px;
		height: 30px;
		text-align: center;
		border: 1px solid #ddd;
		border-left: none;
		border-right: none;
	}

	.item-remove {
		color: #e74c3c;
		font-size: 1.5rem;
		text-decoration: none;
		font-weight: bold;
		display: inline-block;
		width: 30px;
		height: 30px;
		text-align: center;
		line-height: 30px;
		border-radius: 50%;
		transition: all 0.2s;
	}

	.item-remove:hover {
		background-color: #fee;
		color: #c0392b;
	}

	.cart-footer-actions {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1rem 0;
	}

	.coupon-section {
		display: flex;
		gap: 0.5rem;
	}

	.coupon-input {
		padding: 0.75rem;
		border: 1px solid #ddd;
		border-radius: 4px;
		font-size: 0.9rem;
	}

	.apply-coupon-btn,
	.update-cart-btn {
		padding: 0.75rem 1.5rem;
		background-color: #e74c3c;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
		font-weight: 500;
		transition: background-color 0.2s;
	}

	.apply-coupon-btn:hover,
	.update-cart-btn:hover {
		background-color: #c0392b;
	}

	.cart-summary {
		position: sticky;
		top: 2rem;
		height: fit-content;
	}

	.summary-card {
		background-color: white;
		padding: 2rem;
		border-radius: 8px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.summary-card h3 {
		margin-top: 0;
		margin-bottom: 1.5rem;
		font-size: 1.5rem;
		border-bottom: 2px solid #e74c3c;
		padding-bottom: 0.5rem;
	}

	.summary-row {
		display: flex;
		justify-content: space-between;
		padding: 1rem 0;
		border-bottom: 1px solid #eee;
	}

	.summary-row.total {
		border-bottom: 2px solid #333;
		font-size: 1.5rem;
		font-weight: bold;
		margin-top: 1rem;
	}

	.cart-buttons {
		display: flex;
		gap: 1rem;
		margin-top: 1.5rem;
	}

	.view-cart-btn,
	.checkout-btn {
		flex: 1;
		padding: 0.75rem 1.5rem;
		text-align: center;
		border-radius: 4px;
		font-weight: 500;
		text-decoration: none;
		transition: all 0.2s;
	}

	.view-cart-btn {
		background-color: white;
		color: #e74c3c;
		border: 2px solid #e74c3c;
	}

	.view-cart-btn:hover {
		background-color: #f8f8f8;
	}

	.checkout-btn {
		background-color: #e74c3c;
		color: white;
		border: 2px solid #e74c3c;
		cursor: pointer;
		font-size: 1rem;
	}

	.checkout-btn:hover {
		background-color: #c0392b;
		border-color: #c0392b;
	}

	@media (max-width: 968px) {
		.cart-content {
			grid-template-columns: 1fr;
		}

		.cart-summary {
			position: static;
		}

		.cart-table {
			font-size: 0.875rem;
		}

		.product-info {
			flex-direction: column;
			align-items: flex-start;
		}
	}
</style>

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
	<title>購物車 - Shopping Cart</title>
</svelte:head>

<div class="cart-page">
	<h1>購物車</h1>

	{#if cart.loading}
		<p>載入中...</p>
	{:else if cart.items.length === 0}
		<p>購物車是空的</p>
		<a href="/">繼續購物</a>
	{:else}
		<div class="cart-items">
			{#each cart.items as item}
				<div class="cart-item">
					<div class="item-image">
						{#if item.product.image_url}
							<img src={item.product.image_url} alt={item.product.name} />
						{:else}
							<div class="no-image">無圖片</div>
						{/if}
					</div>
					<div class="item-info">
						<h3>{item.product.name}</h3>
						<p class="price">NT$ {item.product.price.toLocaleString()}</p>
					</div>
					<div class="item-quantity">
						<button on:click={() => handleUpdateQuantity(item.id, item.quantity - 1)}>-</button>
						<span>{item.quantity}</span>
						<button on:click={() => handleUpdateQuantity(item.id, item.quantity + 1)}>+</button>
					</div>
					<div class="item-total">
						NT$ {(item.product.price * item.quantity).toLocaleString()}
					</div>
					<div class="item-actions">
						<button class="remove-btn" on:click={() => handleRemoveItem(item.id)}>移除</button>
					</div>
				</div>
			{/each}
		</div>

		<div class="cart-summary">
			<div class="total">
				<strong>總計: NT$ {cart.total_amount.toLocaleString()}</strong>
			</div>
			<button class="checkout-btn" on:click={handleCheckout}>前往結帳</button>
		</div>
	{/if}
</div>

<style>
	.cart-page {
		max-width: 1000px;
		margin: 0 auto;
	}

	h1 {
		margin-bottom: 2rem;
	}

	.cart-items {
		margin-bottom: 2rem;
	}

	.cart-item {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 1rem;
		border: 1px solid #ddd;
		border-radius: 8px;
		margin-bottom: 1rem;
	}

	.item-image {
		width: 100px;
		height: 100px;
		flex-shrink: 0;
	}

	.item-image img {
		width: 100%;
		height: 100%;
		object-fit: cover;
		border-radius: 4px;
	}

	.no-image {
		width: 100%;
		height: 100%;
		background-color: #f0f0f0;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #999;
		border-radius: 4px;
	}

	.item-info {
		flex: 1;
	}

	.item-info h3 {
		margin: 0 0 0.5rem 0;
	}

	.price {
		color: #e74c3c;
		font-weight: bold;
		margin: 0;
	}

	.item-quantity {
		display: flex;
		align-items: center;
		gap: 0.5rem;
	}

	.item-quantity button {
		width: 30px;
		height: 30px;
		border: 1px solid #ddd;
		background-color: white;
		cursor: pointer;
		border-radius: 4px;
	}

	.item-quantity button:hover {
		background-color: #f0f0f0;
	}

	.item-total {
		font-weight: bold;
		min-width: 120px;
		text-align: right;
	}

	.remove-btn {
		padding: 0.5rem 1rem;
		background-color: #e74c3c;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	.remove-btn:hover {
		background-color: #c0392b;
	}

	.cart-summary {
		border-top: 2px solid #ddd;
		padding-top: 1rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.total {
		font-size: 1.5rem;
	}

	.checkout-btn {
		padding: 1rem 2rem;
		background-color: #27ae60;
		color: white;
		border: none;
		border-radius: 4px;
		font-size: 1.2rem;
		cursor: pointer;
	}

	.checkout-btn:hover {
		background-color: #229954;
	}
</style>


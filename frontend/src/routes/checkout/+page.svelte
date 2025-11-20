<script>
	import { onMount } from 'svelte';
	import { cartStore } from '$lib/stores/cart.js';
	import { createOrder } from '$lib/api.js';
	import { goto } from '$app/navigation';

	let cart = { items: [], total_amount: 0 };
	let shippingAddress = '';
	let loading = false;
	let error = '';

	cartStore.subscribe((value) => {
		cart = value;
	});

	onMount(() => {
		cartStore.load();
		if (cart.items.length === 0) {
			goto('/cart');
		}
	});

	async function handleSubmit() {
		if (!shippingAddress.trim()) {
			error = '請輸入配送地址';
			return;
		}

		loading = true;
		error = '';

		try {
			const order = await createOrder(shippingAddress);
			alert('訂單建立成功！訂單編號: ' + order.id);
			cartStore.load();
			goto('/');
		} catch (err) {
			error = '訂單建立失敗: ' + err.message;
		} finally {
			loading = false;
		}
	}
</script>

<svelte:head>
	<title>結帳 - Shopping Cart</title>
</svelte:head>

<div class="checkout-page">
	<h1>結帳</h1>

	{#if cart.items.length === 0}
		<p>購物車是空的</p>
		<a href="/cart">返回購物車</a>
	{:else}
		<div class="checkout-content">
			<div class="order-summary">
				<h2>訂單摘要</h2>
				{#each cart.items as item}
					<div class="summary-item">
						<span>{item.product.name} x {item.quantity}</span>
						<span>NT$ {(item.product.price * item.quantity).toLocaleString()}</span>
					</div>
				{/each}
				<div class="summary-total">
					<strong>總計: NT$ {cart.total_amount.toLocaleString()}</strong>
				</div>
			</div>

			<div class="checkout-form">
				<h2>配送資訊</h2>
				{#if error}
					<div class="error">{error}</div>
				{/if}

				<form on:submit|preventDefault={handleSubmit}>
					<label>
						配送地址
						<textarea
							bind:value={shippingAddress}
							required
							rows="4"
							placeholder="請輸入完整的配送地址"
						></textarea>
					</label>

					<button type="submit" disabled={loading}>
						{loading ? '處理中...' : '確認訂單'}
					</button>
				</form>
			</div>
		</div>
	{/if}
</div>

<style>
	.checkout-page {
		max-width: 1000px;
		margin: 0 auto;
	}

	h1 {
		margin-bottom: 2rem;
	}

	.checkout-content {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 2rem;
	}

	.order-summary,
	.checkout-form {
		background-color: #f9f9f9;
		padding: 2rem;
		border-radius: 8px;
	}

	h2 {
		margin-top: 0;
		margin-bottom: 1.5rem;
	}

	.summary-item {
		display: flex;
		justify-content: space-between;
		padding: 0.5rem 0;
		border-bottom: 1px solid #ddd;
	}

	.summary-total {
		margin-top: 1rem;
		padding-top: 1rem;
		border-top: 2px solid #333;
		font-size: 1.2rem;
		text-align: right;
	}

	.checkout-form label {
		display: block;
		margin-bottom: 1rem;
	}

	.checkout-form textarea {
		width: 100%;
		padding: 0.5rem;
		border: 1px solid #ddd;
		border-radius: 4px;
		font-family: inherit;
		margin-top: 0.5rem;
	}

	.checkout-form button {
		width: 100%;
		padding: 1rem;
		background-color: #27ae60;
		color: white;
		border: none;
		border-radius: 4px;
		font-size: 1.2rem;
		cursor: pointer;
		margin-top: 1rem;
	}

	.checkout-form button:hover:not(:disabled) {
		background-color: #229954;
	}

	.checkout-form button:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.error {
		background-color: #fee;
		color: #c33;
		padding: 1rem;
		border-radius: 4px;
		margin-bottom: 1rem;
	}

	@media (max-width: 768px) {
		.checkout-content {
			grid-template-columns: 1fr;
		}
	}
</style>


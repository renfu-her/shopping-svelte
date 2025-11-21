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
	<title>結帳 - Shopwise</title>
</svelte:head>

<div class="checkout-page">
	<!-- Breadcrumb Section -->
	<div class="breadcrumb-section">
		<div class="container">
			<div class="breadcrumb-content">
				<div class="page-title">
					<h1>Checkout</h1>
				</div>
				<ol class="breadcrumb">
					<li class="breadcrumb-item"><a href="/">Home</a></li>
					<li class="breadcrumb-item"><a href="/product">Pages</a></li>
					<li class="breadcrumb-item active">Checkout</li>
				</ol>
			</div>
		</div>
	</div>

	<div class="container">

		{#if cart.items.length === 0}
			<div class="empty-cart">
				<p>購物車是空的</p>
				<a href="/cart">返回購物車</a>
			</div>
		{:else}
			<div class="checkout-content">
				<div class="checkout-form-section">
					<!-- Returning Customer -->
					<div class="toggle-info">
						<span>Returning customer? <a href="#loginform" class="toggle-link">Click here to login</a></span>
					</div>

					<!-- Coupon -->
					<div class="toggle-info">
						<span>Have a coupon? <a href="#coupon" class="toggle-link">Click here to enter your code</a></span>
					</div>

					<h2>Billing Details</h2>
					{#if error}
						<div class="error-message">{error}</div>
					{/if}

					<form on:submit|preventDefault={handleSubmit}>
						<div class="form-row">
							<div class="form-group">
								<label for="fname">First name *</label>
								<input type="text" id="fname" required class="form-control" placeholder="First name *" />
							</div>
							<div class="form-group">
								<label for="lname">Last name *</label>
								<input type="text" id="lname" required class="form-control" placeholder="Last name *" />
							</div>
						</div>
						<div class="form-group">
							<label for="cname">Company Name</label>
							<input type="text" id="cname" class="form-control" placeholder="Company Name" />
						</div>
						<div class="form-group">
							<label for="country">Country *</label>
							<select id="country" required class="form-control">
								<option value="">Select an option...</option>
								<option value="TW">Taiwan</option>
								<option value="US">United States</option>
								<option value="CN">China</option>
							</select>
						</div>
						<div class="form-group">
							<label for="address">Address *</label>
							<input type="text" id="address" bind:value={shippingAddress} required class="form-control" placeholder="Address *" />
						</div>
						<div class="form-group">
							<label for="address2">Address line2</label>
							<input type="text" id="address2" class="form-control" placeholder="Address line2" />
						</div>
						<div class="form-row">
							<div class="form-group">
								<label for="city">City / Town *</label>
								<input type="text" id="city" required class="form-control" placeholder="City / Town *" />
							</div>
							<div class="form-group">
								<label for="state">State / County *</label>
								<input type="text" id="state" required class="form-control" placeholder="State / County *" />
							</div>
						</div>
						<div class="form-group">
							<label for="zipcode">Postcode / ZIP *</label>
							<input type="text" id="zipcode" required class="form-control" placeholder="Postcode / ZIP *" />
						</div>
						<div class="form-row">
							<div class="form-group">
								<label for="phone">Phone *</label>
								<input type="text" id="phone" required class="form-control" placeholder="Phone *" />
							</div>
							<div class="form-group">
								<label for="email">Email address *</label>
								<input type="email" id="email" required class="form-control" placeholder="Email address *" />
							</div>
						</div>

						<button type="submit" class="submit-btn" disabled={loading}>
							{loading ? '處理中...' : 'Place Order'}
						</button>
					</form>
				</div>

				<div class="order-summary-section">
					<div class="summary-card">
						<h3>訂單摘要</h3>
						<div class="order-items">
							{#each cart.items as item}
								<div class="order-item">
									<div class="item-info">
										<span class="item-name">{item.product.name}</span>
										<span class="item-quantity">x {item.quantity}</span>
									</div>
									<span class="item-price">NT$ {(item.product.price * item.quantity).toLocaleString()}</span>
								</div>
							{/each}
						</div>
						<div class="summary-totals">
							<div class="summary-row">
								<span>小計</span>
								<span>NT$ {cart.total_amount.toLocaleString()}</span>
							</div>
							<div class="summary-row">
								<span>運費</span>
								<span>免費</span>
							</div>
							<div class="summary-row total">
								<span>總計</span>
								<span>NT$ {cart.total_amount.toLocaleString()}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}
	</div>
</div>

<style>
	.checkout-page {
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

	.empty-cart {
		text-align: center;
		padding: 4rem;
		background-color: white;
		border-radius: 8px;
	}

	.checkout-content {
		display: grid;
		grid-template-columns: 1fr 400px;
		gap: 2rem;
	}

	.checkout-form-section,
	.order-summary-section {
		background-color: white;
		padding: 2rem;
		border-radius: 8px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.toggle-info {
		background-color: #f8f8f8;
		padding: 1rem;
		margin-bottom: 1.5rem;
		border-radius: 4px;
	}

	.toggle-link {
		color: #e74c3c;
		text-decoration: none;
		font-weight: 500;
	}

	.toggle-link:hover {
		text-decoration: underline;
	}

	.checkout-form-section h2 {
		margin-top: 0;
		margin-bottom: 1.5rem;
		font-size: 1.5rem;
		border-bottom: 2px solid #e74c3c;
		padding-bottom: 0.5rem;
	}

	.form-row {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 1rem;
	}

	.error-message {
		background-color: #fee;
		color: #c33;
		padding: 1rem;
		border-radius: 4px;
		margin-bottom: 1.5rem;
	}

	.form-group {
		margin-bottom: 1.5rem;
	}

	.form-group label {
		display: block;
		margin-bottom: 0.5rem;
		font-weight: 500;
	}

	.form-control {
		width: 100%;
		padding: 0.75rem;
		border: 1px solid #ddd;
		border-radius: 4px;
		font-family: inherit;
		font-size: 1rem;
	}

	.form-control:focus {
		outline: none;
		border-color: #e74c3c;
	}

	.submit-btn {
		width: 100%;
		padding: 1rem 2rem;
		background-color: #e74c3c;
		color: white;
		border: none;
		border-radius: 4px;
		font-size: 1.2rem;
		font-weight: bold;
		cursor: pointer;
		transition: background-color 0.2s;
	}

	.submit-btn:hover:not(:disabled) {
		background-color: #c0392b;
	}

	.submit-btn:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.summary-card {
		position: sticky;
		top: 2rem;
	}

	.summary-card h3 {
		margin-top: 0;
		margin-bottom: 1.5rem;
		font-size: 1.5rem;
		border-bottom: 2px solid #e74c3c;
		padding-bottom: 0.5rem;
	}

	.order-items {
		margin-bottom: 1.5rem;
	}

	.order-item {
		display: flex;
		justify-content: space-between;
		padding: 1rem 0;
		border-bottom: 1px solid #eee;
	}

	.item-info {
		display: flex;
		flex-direction: column;
		gap: 0.25rem;
	}

	.item-name {
		font-weight: 500;
	}

	.item-quantity {
		color: #666;
		font-size: 0.9rem;
	}

	.item-price {
		font-weight: bold;
		color: #e74c3c;
	}

	.summary-totals {
		border-top: 2px solid #eee;
		padding-top: 1rem;
	}

	.summary-row {
		display: flex;
		justify-content: space-between;
		padding: 0.75rem 0;
	}

	.summary-row.total {
		font-size: 1.5rem;
		font-weight: bold;
		border-top: 2px solid #333;
		margin-top: 1rem;
		padding-top: 1rem;
	}

	@media (max-width: 968px) {
		.checkout-content {
			grid-template-columns: 1fr;
		}

		.summary-card {
			position: static;
		}
	}
</style>

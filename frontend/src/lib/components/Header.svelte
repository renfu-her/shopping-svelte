<script>
	import { cartStore } from '$lib/stores/cart.js';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	let cart = { items: [], total_amount: 0 };
	let showCategories = false;
	let searchQuery = '';

	cartStore.subscribe((value) => {
		cart = value;
	});

	onMount(() => {
		cartStore.load();
	});

	function getCartItemCount() {
		return cart.items.reduce((sum, item) => sum + item.quantity, 0);
	}

	function handleSearch() {
		if (searchQuery.trim()) {
			goto(`/product?search=${encodeURIComponent(searchQuery.trim())}`);
		}
	}
</script>

<!-- Top Bar -->
<div class="top-bar">
	<div class="top-bar-left">
		<span>免費運送超過 $250</span>
		<span class="separator">|</span>
		<span>下載 App</span>
	</div>
	<div class="top-bar-right">
		<span>English ▼</span>
		<span>USD ▼</span>
	</div>
</div>

<!-- Main Header -->
<header class="main-header">
	<div class="header-container">
		<!-- Logo -->
		<a href="/" class="logo">
			<span class="logo-icon">🛒</span>
			<span class="logo-text">Shopwise</span>
		</a>

		<!-- Search Bar -->
		<div class="search-bar">
			<select class="category-select">
				<option>全部分類</option>
			</select>
			<input
				type="text"
				placeholder="搜尋商品..."
				bind:value={searchQuery}
				on:keydown={(e) => e.key === 'Enter' && handleSearch()}
			/>
			<button class="search-btn" on:click={handleSearch}>
				搜尋
			</button>
		</div>

		<!-- User Actions -->
		<div class="user-actions">
			<a href="/account" class="icon-btn" title="帳戶">
				👤
			</a>
			<a href="/wishlist" class="icon-btn" title="願望清單">
				❤️
				<span class="badge">0</span>
			</a>
			<a href="/cart" class="icon-btn cart-icon" title="購物車">
				🛍️
				{#if getCartItemCount() > 0}
					<span class="badge">{getCartItemCount()}</span>
				{/if}
				<span class="cart-total">NT$ {cart.total_amount.toLocaleString()}</span>
			</a>
		</div>
	</div>
</header>

<!-- Navigation Bar -->
<nav class="main-nav">
	<div class="nav-container">
		<button class="categories-btn" on:click={() => showCategories = !showCategories}>
			<span>全部分類</span>
			<span class="menu-icon">☰</span>
		</button>
		<div class="nav-links">
			<a href="/" class="nav-link">首頁</a>
			<div class="nav-link dropdown">
				頁面 ▼
				<div class="dropdown-menu">
					<a href="/cart">購物車</a>
					<a href="/checkout">結帳</a>
					<a href="/news">新聞</a>
					<a href="/about">關於我們</a>
					<a href="/faq">FAQ</a>
				</div>
			</div>
			<a href="/product" class="nav-link">商品</a>
			<a href="/blog" class="nav-link">部落格</a>
			<a href="/shop" class="nav-link">商店</a>
			<a href="/contact" class="nav-link">聯絡我們</a>
		</div>
		<div class="contact-info">
			<span class="phone-icon">📞</span>
			<span>123-456-7890</span>
		</div>
	</div>
</nav>

<style>
	.top-bar {
		background-color: #000;
		color: #fff;
		padding: 0.5rem 2rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 0.875rem;
	}

	.top-bar-left {
		display: flex;
		gap: 1rem;
		align-items: center;
	}

	.separator {
		color: #666;
	}

	.top-bar-right {
		display: flex;
		gap: 1rem;
		cursor: pointer;
	}

	.main-header {
		background-color: #fff;
		padding: 1rem 2rem;
		border-bottom: 1px solid #eee;
	}

	.header-container {
		max-width: 1400px;
		margin: 0 auto;
		display: flex;
		align-items: center;
		gap: 2rem;
	}

	.logo {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		text-decoration: none;
		color: #000;
		font-size: 1.5rem;
		font-weight: bold;
	}

	.logo-icon {
		font-size: 2rem;
	}

	.search-bar {
		flex: 1;
		display: flex;
		max-width: 600px;
		border: 2px solid #e74c3c;
		border-radius: 4px;
		overflow: hidden;
	}

	.category-select {
		padding: 0.75rem;
		border: none;
		border-right: 1px solid #ddd;
		background-color: #f8f8f8;
		cursor: pointer;
	}

	.search-bar input {
		flex: 1;
		padding: 0.75rem;
		border: none;
		outline: none;
	}

	.search-btn {
		padding: 0.75rem 2rem;
		background-color: #e74c3c;
		color: white;
		border: none;
		cursor: pointer;
		font-weight: bold;
	}

	.search-btn:hover {
		background-color: #c0392b;
	}

	.user-actions {
		display: flex;
		gap: 1rem;
		align-items: center;
	}

	.icon-btn {
		position: relative;
		font-size: 1.5rem;
		text-decoration: none;
		color: #000;
	}

	.cart-icon {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.25rem;
	}

	.badge {
		position: absolute;
		top: -8px;
		right: -8px;
		background-color: #e74c3c;
		color: white;
		border-radius: 50%;
		width: 20px;
		height: 20px;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 0.75rem;
		font-weight: bold;
	}

	.cart-total {
		font-size: 0.875rem;
		color: #e74c3c;
		font-weight: bold;
		position: static;
	}

	.main-nav {
		background-color: #fff;
		border-bottom: 1px solid #eee;
	}

	.nav-container {
		max-width: 1400px;
		margin: 0 auto;
		padding: 0 2rem;
		display: flex;
		align-items: center;
		gap: 2rem;
	}

	.categories-btn {
		background-color: #e74c3c;
		color: white;
		padding: 1rem 2rem;
		border: none;
		cursor: pointer;
		font-weight: bold;
		font-size: 1rem;
	}

	.categories-btn:hover {
		background-color: #c0392b;
	}

	.nav-links {
		display: flex;
		gap: 2rem;
		flex: 1;
	}

	.nav-link {
		text-decoration: none;
		color: #000;
		font-weight: 500;
		position: relative;
		padding: 1rem 0;
	}

	.nav-link:hover {
		color: #e74c3c;
	}

	.dropdown {
		position: relative;
		cursor: pointer;
	}

	.dropdown-menu {
		display: none;
		position: absolute;
		top: 100%;
		left: 0;
		background-color: white;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
		min-width: 200px;
		padding: 0.5rem 0;
		z-index: 1000;
	}

	.dropdown:hover .dropdown-menu {
		display: block;
	}

	.dropdown-menu a {
		display: block;
		padding: 0.75rem 1.5rem;
		color: #000;
		text-decoration: none;
	}

	.dropdown-menu a:hover {
		background-color: #f8f8f8;
		color: #e74c3c;
	}

	.contact-info {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		color: #e74c3c;
		font-weight: bold;
	}

	.phone-icon {
		font-size: 1.25rem;
	}
</style>


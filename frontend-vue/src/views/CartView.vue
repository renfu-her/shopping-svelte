<template>
	<div class="cart-page">
		<div class="container">
			<h1>購物車</h1>
			<div v-if="cartStore.loading" class="loading">載入中...</div>
			<div v-else-if="cartStore.items.length === 0" class="empty-cart">
				<p>購物車是空的</p>
				<router-link to="/product" class="btn">繼續購物</router-link>
			</div>
			<div v-else class="cart-content">
				<div class="cart-items">
					<table class="cart-table">
						<thead>
							<tr>
								<th>商品</th>
								<th>價格</th>
								<th>數量</th>
								<th>小計</th>
								<th></th>
							</tr>
						</thead>
						<tbody>
							<tr v-for="item in cartStore.items" :key="item.id">
								<td class="product-cell">
									<img v-if="item.product?.image_url" :src="item.product.image_url" :alt="item.product.name" />
									<span>{{ item.product?.name || '商品' }}</span>
								</td>
								<td>NT$ {{ item.product?.price?.toLocaleString() || 0 }}</td>
								<td>
									<div class="quantity-controls">
										<button @click="updateQuantity(item.id, item.quantity - 1)">-</button>
										<input type="number" :value="item.quantity" @change="updateQuantity(item.id, $event.target.value)" min="1" />
										<button @click="updateQuantity(item.id, item.quantity + 1)">+</button>
									</div>
								</td>
								<td>NT$ {{ (item.quantity * (item.product?.price || 0)).toLocaleString() }}</td>
								<td>
									<button class="remove-btn" @click="removeItem(item.id)">×</button>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
				<div class="cart-summary">
					<h3>訂單摘要</h3>
					<div class="summary-row">
						<span>小計</span>
						<span>NT$ {{ cartStore.total_amount.toLocaleString() }}</span>
					</div>
					<div class="summary-row">
						<span>運費</span>
						<span>NT$ 0</span>
					</div>
					<div class="summary-row total">
						<span>總計</span>
						<span>NT$ {{ cartStore.total_amount.toLocaleString() }}</span>
					</div>
					<router-link to="/checkout" class="checkout-btn">前往結帳</router-link>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCartStore } from '@/stores/cart.js';

const cartStore = useCartStore();

onMounted(() => {
	cartStore.load();
});

function updateQuantity(itemId, quantity) {
	const qty = parseInt(quantity);
	if (qty > 0) {
		cartStore.updateItem(itemId, qty);
	}
}

function removeItem(itemId) {
	if (confirm('確定要移除這個商品嗎？')) {
		cartStore.removeItem(itemId);
	}
}
</script>

<style scoped>
.cart-page {
	padding: 2rem 0;
	min-height: calc(100vh - 300px);
}

.container {
	max-width: 1200px;
	margin: 0 auto;
	padding: 0 2rem;
}

h1 {
	margin-bottom: 2rem;
}

.cart-content {
	display: grid;
	grid-template-columns: 2fr 1fr;
	gap: 2rem;
}

.cart-table {
	width: 100%;
	border-collapse: collapse;
	background-color: white;
	border-radius: 8px;
	overflow: hidden;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.cart-table th {
	background-color: #f8f8f8;
	padding: 1rem;
	text-align: left;
	font-weight: 600;
}

.cart-table td {
	padding: 1rem;
	border-top: 1px solid #eee;
}

.product-cell {
	display: flex;
	align-items: center;
	gap: 1rem;
}

.product-cell img {
	width: 80px;
	height: 80px;
	object-fit: cover;
	border-radius: 4px;
}

.quantity-controls {
	display: flex;
	align-items: center;
	gap: 0.5rem;
}

.quantity-controls button {
	width: 30px;
	height: 30px;
	border: 1px solid #ddd;
	background-color: white;
	cursor: pointer;
	border-radius: 4px;
}

.quantity-controls input {
	width: 60px;
	text-align: center;
	border: 1px solid #ddd;
	border-radius: 4px;
	padding: 0.5rem;
}

.remove-btn {
	background: none;
	border: none;
	font-size: 1.5rem;
	cursor: pointer;
	color: #e74c3c;
}

.cart-summary {
	background-color: white;
	padding: 2rem;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	height: fit-content;
}

.cart-summary h3 {
	margin-top: 0;
	margin-bottom: 1.5rem;
}

.summary-row {
	display: flex;
	justify-content: space-between;
	padding: 1rem 0;
	border-bottom: 1px solid #eee;
}

.summary-row.total {
	border-bottom: 2px solid #333;
	font-size: 1.2rem;
	font-weight: bold;
	margin-top: 1rem;
}

.checkout-btn {
	display: block;
	width: 100%;
	padding: 1rem;
	background-color: #e74c3c;
	color: white;
	text-align: center;
	border-radius: 4px;
	margin-top: 1.5rem;
	font-weight: bold;
	text-decoration: none;
}

.checkout-btn:hover {
	background-color: #c0392b;
}

.loading,
.empty-cart {
	text-align: center;
	padding: 4rem;
}

.empty-cart .btn {
	display: inline-block;
	margin-top: 1rem;
	padding: 0.75rem 2rem;
	background-color: #e74c3c;
	color: white;
	border-radius: 4px;
	text-decoration: none;
}

@media (max-width: 968px) {
	.cart-content {
		grid-template-columns: 1fr;
	}
}
</style>


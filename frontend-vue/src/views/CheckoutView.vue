<template>
	<div class="checkout-page">
		<div class="container">
			<h1>結帳</h1>
			<div class="checkout-content">
				<div class="checkout-form">
					<h2>帳單詳情</h2>
					<form @submit.prevent="handleSubmit">
						<div class="form-group">
							<label>姓名 *</label>
							<input type="text" v-model="form.name" required />
						</div>
						<div class="form-group">
							<label>電子郵件 *</label>
							<input type="email" v-model="form.email" required />
						</div>
						<div class="form-group">
							<label>電話 *</label>
							<input type="tel" v-model="form.phone" required />
						</div>
						<div class="form-group">
							<label>地址 *</label>
							<input type="text" v-model="form.address" required />
						</div>
						<div class="form-row">
							<div class="form-group">
								<label>城市 *</label>
								<input type="text" v-model="form.city" required />
							</div>
							<div class="form-group">
								<label>郵遞區號 *</label>
								<input type="text" v-model="form.postalCode" required />
							</div>
						</div>
						<button type="submit" class="submit-btn">下訂單</button>
					</form>
				</div>
				<div class="order-summary">
					<h2>訂單摘要</h2>
					<div v-if="cartStore.items.length === 0" class="empty">
						<p>購物車是空的</p>
					</div>
					<template v-else>
						<div class="order-items">
							<div v-for="item in cartStore.items" :key="item.id" class="order-item">
								<span>{{ item.product?.name }} × {{ item.quantity }}</span>
								<span>NT$ {{ (item.quantity * (item.product?.price || 0)).toLocaleString() }}</span>
							</div>
						</div>
						<div class="order-total">
							<div class="total-row">
								<span>小計</span>
								<span>NT$ {{ cartStore.total_amount.toLocaleString() }}</span>
							</div>
							<div class="total-row">
								<span>運費</span>
								<span>NT$ 0</span>
							</div>
							<div class="total-row final">
								<span>總計</span>
								<span>NT$ {{ cartStore.total_amount.toLocaleString() }}</span>
							</div>
						</div>
					</template>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useCartStore } from '@/stores/cart.js';
import { createOrder } from '@/services/api.js';

const router = useRouter();
const cartStore = useCartStore();

const form = ref({
	name: '',
	email: '',
	phone: '',
	address: '',
	city: '',
	postalCode: ''
});

onMounted(() => {
	cartStore.load();
});

async function handleSubmit() {
	try {
		await createOrder({
			...form.value
		});
		alert('訂單已成功建立！');
		router.push('/');
	} catch (error) {
		alert('訂單建立失敗，請稍後再試');
		console.error(error);
	}
}
</script>

<style scoped>
.checkout-page {
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

.checkout-content {
	display: grid;
	grid-template-columns: 2fr 1fr;
	gap: 2rem;
}

.checkout-form,
.order-summary {
	background-color: white;
	padding: 2rem;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.checkout-form h2,
.order-summary h2 {
	margin-top: 0;
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

.form-group input {
	width: 100%;
	padding: 0.75rem;
	border: 1px solid #ddd;
	border-radius: 4px;
	font-size: 1rem;
}

.form-row {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 1rem;
}

.submit-btn {
	width: 100%;
	padding: 1rem;
	background-color: #e74c3c;
	color: white;
	border: none;
	border-radius: 4px;
	font-size: 1.1rem;
	font-weight: bold;
	cursor: pointer;
	margin-top: 1rem;
}

.submit-btn:hover {
	background-color: #c0392b;
}

.order-items {
	margin-bottom: 1.5rem;
}

.order-item {
	display: flex;
	justify-content: space-between;
	padding: 0.75rem 0;
	border-bottom: 1px solid #eee;
}

.order-total {
	border-top: 2px solid #333;
	padding-top: 1rem;
}

.total-row {
	display: flex;
	justify-content: space-between;
	padding: 0.5rem 0;
}

.total-row.final {
	font-size: 1.2rem;
	font-weight: bold;
	margin-top: 0.5rem;
}

.empty {
	text-align: center;
	padding: 2rem;
	color: #999;
}

@media (max-width: 968px) {
	.checkout-content {
		grid-template-columns: 1fr;
	}
}
</style>


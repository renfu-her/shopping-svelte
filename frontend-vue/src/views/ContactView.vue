<template>
	<div class="contact-page">
		<div class="container">
			<h1>聯絡我們</h1>
			<div class="contact-content">
				<div class="contact-info">
					<h2>聯絡資訊</h2>
					<p>電話: 123-456-7890</p>
					<p>電子郵件: info@shopwise.com</p>
					<p>地址: 台北市信義區信義路五段7號</p>
				</div>
				<div class="contact-form">
					<h2>發送訊息</h2>
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
							<label>訊息 *</label>
							<textarea v-model="form.message" rows="5" required></textarea>
						</div>
						<button type="submit" class="submit-btn">發送</button>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue';

const form = ref({
	name: '',
	email: '',
	message: ''
});

function handleSubmit() {
	alert('訊息已發送！');
	form.value = { name: '', email: '', message: '' };
}
</script>

<style scoped>
.contact-page {
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

.contact-content {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 2rem;
}

.contact-info,
.contact-form {
	background-color: white;
	padding: 2rem;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.contact-info h2,
.contact-form h2 {
	margin-top: 0;
	margin-bottom: 1.5rem;
}

.contact-info p {
	margin-bottom: 1rem;
	line-height: 1.8;
}

.form-group {
	margin-bottom: 1.5rem;
}

.form-group label {
	display: block;
	margin-bottom: 0.5rem;
	font-weight: 500;
}

.form-group input,
.form-group textarea {
	width: 100%;
	padding: 0.75rem;
	border: 1px solid #ddd;
	border-radius: 4px;
	font-size: 1rem;
	font-family: inherit;
}

.submit-btn {
	padding: 0.75rem 2rem;
	background-color: #e74c3c;
	color: white;
	border: none;
	border-radius: 4px;
	font-size: 1rem;
	font-weight: bold;
	cursor: pointer;
}

.submit-btn:hover {
	background-color: #c0392b;
}

@media (max-width: 768px) {
	.contact-content {
		grid-template-columns: 1fr;
	}
}
</style>


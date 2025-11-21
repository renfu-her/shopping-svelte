<template>
	<footer class="footer">
		<div class="container">
			<div class="footer-content">
				<div class="footer-section">
					<h3>關於我們</h3>
					<p>Shopwise 是一個現代化的電商平台，提供優質的商品和服務。</p>
				</div>
				<div class="footer-section">
					<h3>快速連結</h3>
					<ul>
						<li><router-link to="/about">關於我們</router-link></li>
						<li><router-link to="/contact">聯絡我們</router-link></li>
						<li><router-link to="/faq">常見問題</router-link></li>
					</ul>
				</div>
				<div class="footer-section">
					<h3>客戶服務</h3>
					<ul>
						<li><router-link to="/cart">購物車</router-link></li>
						<li><router-link to="/checkout">結帳</router-link></li>
					</ul>
				</div>
			</div>
			<div class="footer-bottom">
				<p>&copy; 2024 Shopwise. All rights reserved.</p>
			</div>
		</div>
	</footer>
</template>

<script setup>
// Footer component
</script>

<style scoped>
.footer {
	background-color: #333;
	color: #fff;
	padding: 3rem 0 1rem;
	margin-top: auto;
}

.container {
	max-width: 1400px;
	margin: 0 auto;
	padding: 0 2rem;
}

.footer-content {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
	gap: 2rem;
	margin-bottom: 2rem;
}

.footer-section h3 {
	margin-bottom: 1rem;
	font-size: 1.2rem;
}

.footer-section p {
	color: #ccc;
	line-height: 1.6;
}

.footer-section ul {
	list-style: none;
}

.footer-section ul li {
	margin-bottom: 0.5rem;
}

.footer-section a {
	color: #ccc;
	text-decoration: none;
	transition: color 0.2s;
}

.footer-section a:hover {
	color: #e74c3c;
}

.footer-bottom {
	border-top: 1px solid #555;
	padding-top: 1rem;
	text-align: center;
	color: #ccc;
}
</style>


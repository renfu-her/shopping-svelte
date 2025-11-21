<template>
	<div class="product-detail-page">
		<!-- Breadcrumb Section -->
		<div class="breadcrumb-section">
			<div class="container">
				<div class="breadcrumb-content">
					<div class="page-title">
						<h1>Product Detail Left Sidebar</h1>
					</div>
					<ol class="breadcrumb">
						<li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
						<li class="breadcrumb-item"><router-link to="/product">Pages</router-link></li>
						<li class="breadcrumb-item active">Product Detail Left Sidebar</li>
					</ol>
				</div>
			</div>
		</div>

		<div class="container">
			<div class="page-layout">
				<!-- Left Sidebar -->
				<aside class="sidebar">
					<div class="sidebar-section">
						<h3>分類</h3>
						<CategoryTree :categories="categories" @click="handleCategoryClick" />
					</div>

					<div v-if="recentProducts.length > 0" class="sidebar-section">
						<h3>最近商品</h3>
						<div class="recent-products">
							<div
								v-for="recentProduct in recentProducts"
								:key="recentProduct.id"
								class="recent-product-item"
								@click="router.push(`/product/detail/${recentProduct.slug}`)"
							>
								<img v-if="recentProduct.image_url" :src="recentProduct.image_url" :alt="recentProduct.name" />
								<div v-else class="no-image-small">無圖片</div>
								<div class="recent-product-info">
									<h4>{{ recentProduct.name }}</h4>
									<p class="price">NT$ {{ recentProduct.price.toLocaleString() }}</p>
								</div>
							</div>
						</div>
					</div>
				</aside>

				<!-- Main Content -->
				<main class="content">
					<div v-if="loading" class="loading">載入中...</div>
					<div v-else-if="error" class="error">
						<p>{{ error }}</p>
						<router-link to="/product">返回商品列表</router-link>
					</div>
					<template v-else-if="product">
						<div class="product-detail">
							<!-- Product Image -->
							<div class="product-image-section">
								<img v-if="product.image_url" :src="product.image_url" :alt="product.name" class="main-image" />
								<div v-else class="no-image">無圖片</div>
							</div>

							<!-- Product Info -->
							<div class="product-info-section">
								<h1>{{ product.name }}</h1>
								<div class="price-section">
									<span class="current-price">NT$ {{ product.price.toLocaleString() }}</span>
								</div>
								<div class="rating-section">
									<span class="stars">★★★★☆</span>
									<span class="review-count">(21 評價)</span>
								</div>

								<div v-if="product.description" class="description">
									<p>{{ product.description }}</p>
								</div>

								<div class="features">
									<div class="feature-item">✓ 1 年保固</div>
									<div class="feature-item">✓ 30 天退貨政策</div>
									<div class="feature-item">✓ 貨到付款</div>
								</div>

								<div class="options">
									<div class="option-group">
										<label>尺寸</label>
										<div class="size-buttons">
											<button
												v-for="size in ['XS', 'S', 'M', 'L', 'XL']"
												:key="size"
												:class="['size-btn', { active: selectedSize === size }]"
												@click="selectedSize = size"
											>
												{{ size }}
											</button>
										</div>
									</div>

									<div class="option-group">
										<label>數量</label>
										<div class="quantity-selector">
											<button @click="quantity = Math.max(1, quantity - 1)">-</button>
											<input type="number" v-model.number="quantity" :min="1" :max="product.stock" />
											<button @click="quantity = Math.min(product.stock, quantity + 1)">+</button>
										</div>
									</div>
								</div>

								<div class="actions">
									<button
										class="add-to-cart-btn"
										@click="handleAddToCart"
										:disabled="product.stock === 0"
									>
										{{ product.stock === 0 ? '已售完' : '加入購物車' }}
									</button>
									<button class="wishlist-btn">加入願望清單</button>
								</div>

								<div class="stock-info">庫存: {{ product.stock }} 件</div>

								<div class="product-meta">
									<div class="meta-item">
										<span class="meta-label">SKU:</span>
										<span class="meta-value">{{ product.id }}</span>
									</div>
									<div class="meta-item">
										<span class="meta-label">Category:</span>
										<span class="meta-value">Clothing</span>
									</div>
								</div>
							</div>
						</div>

						<!-- Product Tabs -->
						<div class="product-tabs">
							<div class="tab-headers">
								<button
									:class="['tab-header', { active: activeTab === 'description' }]"
									@click="activeTab = 'description'"
								>
									Description
								</button>
								<button
									:class="['tab-header', { active: activeTab === 'additional' }]"
									@click="activeTab = 'additional'"
								>
									Additional info
								</button>
								<button
									:class="['tab-header', { active: activeTab === 'reviews' }]"
									@click="activeTab = 'reviews'"
								>
									Reviews (2)
								</button>
							</div>
							<div class="tab-content">
								<div v-if="activeTab === 'description'" class="tab-pane">
									<p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Vivamus bibendum magna Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
									<p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.</p>
								</div>
								<div v-else-if="activeTab === 'additional'" class="tab-pane">
									<table class="info-table">
										<tr>
											<td>Capacity</td>
											<td>5 Kg</td>
										</tr>
										<tr>
											<td>Color</td>
											<td>Black, Brown, Red</td>
										</tr>
										<tr>
											<td>Water Resistant</td>
											<td>Yes</td>
										</tr>
										<tr>
											<td>Material</td>
											<td>Artificial Leather</td>
										</tr>
									</table>
								</div>
								<div v-else-if="activeTab === 'reviews'" class="tab-pane">
									<div class="reviews-section">
										<h4>2 Review For <span>{{ product.name }}</span></h4>
										<div class="review-list">
											<div class="review-item">
												<div class="review-rating">★★★★☆</div>
												<div class="review-meta">
													<span class="review-author">Alea Brooks</span>
													<span class="review-date">March 5, 2018</span>
												</div>
												<p class="review-text">Lorem Ipsumin gravida nibh vel velit auctor aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis sem nibh id elit.</p>
											</div>
											<div class="review-item">
												<div class="review-rating">★★★☆☆</div>
												<div class="review-meta">
													<span class="review-author">Grace Wong</span>
													<span class="review-date">June 17, 2018</span>
												</div>
												<p class="review-text">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>

						<!-- Related Products -->
						<div v-if="relatedProducts.length > 0" class="related-products-section">
							<h3>Related Products</h3>
							<div class="related-products-grid">
								<ProductCard
									v-for="relatedProduct in relatedProducts"
									:key="relatedProduct.id"
									:product="relatedProduct"
								/>
							</div>
						</div>
					</template>
				</main>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { getProduct, getProducts, getCategories } from '@/services/api.js';
import { useCartStore } from '@/stores/cart.js';
import CategoryTree from '@/components/CategoryTree.vue';
import ProductCard from '@/components/ProductCard.vue';

const route = useRoute();
const router = useRouter();
const cartStore = useCartStore();

const product = ref(null);
const categories = ref([]);
const recentProducts = ref([]);
const relatedProducts = ref([]);
const loading = ref(true);
const error = ref('');
const quantity = ref(1);
const selectedSize = ref('M');
const activeTab = ref('description');

const slug = computed(() => route.params.slug);

onMounted(async () => {
	await Promise.all([loadProduct(), loadCategories(), loadRecentProducts()]);
});

async function loadProduct() {
	loading.value = true;
	error.value = '';
	try {
		product.value = await getProduct(slug.value);
	} catch (err) {
		error.value = '產品不存在';
	} finally {
		loading.value = false;
	}
}

async function loadCategories() {
	try {
		categories.value = await getCategories();
	} catch (error) {
		console.error('Failed to load categories:', error);
	}
}

async function loadRecentProducts() {
	try {
		const result = await getProducts(1, 8);
		recentProducts.value = result.items.filter(p => p.slug !== slug.value).slice(0, 3);
		relatedProducts.value = result.items.filter(p => p.slug !== slug.value).slice(0, 4);
	} catch (error) {
		console.error('Failed to load recent products:', error);
	}
}

function handleAddToCart() {
	if (product.value) {
		cartStore.addItem(product.value.id, quantity.value);
		alert('已加入購物車');
	}
}

function handleCategoryClick(category) {
	if (category && category.level === 3) {
		router.push(`/product?category=${category.slug}`);
	}
}
</script>

<style scoped>
.product-detail-page {
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

.page-layout {
	display: flex;
	gap: 2rem;
}

.sidebar {
	width: 280px;
	flex-shrink: 0;
}

.sidebar-section {
	background-color: white;
	padding: 1.5rem;
	margin-bottom: 1.5rem;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.sidebar-section h3 {
	margin-top: 0;
	margin-bottom: 1rem;
	font-size: 1.2rem;
	border-bottom: 2px solid #e74c3c;
	padding-bottom: 0.5rem;
}

.recent-products {
	display: flex;
	flex-direction: column;
	gap: 1rem;
}

.recent-product-item {
	display: flex;
	gap: 1rem;
	cursor: pointer;
	padding: 0.5rem;
	border-radius: 4px;
	transition: background-color 0.2s;
}

.recent-product-item:hover {
	background-color: #f8f8f8;
}

.recent-product-item img {
	width: 80px;
	height: 80px;
	object-fit: cover;
	border-radius: 4px;
}

.no-image-small {
	width: 80px;
	height: 80px;
	background-color: #f0f0f0;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 0.75rem;
	color: #999;
	border-radius: 4px;
}

.recent-product-info h4 {
	margin: 0 0 0.5rem 0;
	font-size: 0.9rem;
}

.recent-product-info .price {
	color: #e74c3c;
	font-weight: bold;
	font-size: 0.9rem;
	margin: 0;
}

.content {
	flex: 1;
	background-color: white;
	padding: 2rem;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.product-detail {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 3rem;
}

.product-image-section {
	width: 100%;
}

.main-image {
	width: 100%;
	height: auto;
	border-radius: 8px;
	box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.no-image {
	width: 100%;
	aspect-ratio: 1;
	background-color: #f0f0f0;
	display: flex;
	align-items: center;
	justify-content: center;
	color: #999;
	border-radius: 8px;
}

.product-info-section h1 {
	margin-top: 0;
	font-size: 2rem;
	margin-bottom: 1rem;
}

.price-section {
	margin: 1.5rem 0;
}

.current-price {
	font-size: 2.5rem;
	font-weight: bold;
	color: #e74c3c;
}

.rating-section {
	display: flex;
	align-items: center;
	gap: 0.5rem;
	margin: 1rem 0;
}

.stars {
	color: #ffc107;
	font-size: 1.2rem;
}

.review-count {
	color: #666;
}

.description {
	margin: 2rem 0;
	line-height: 1.8;
	color: #666;
}

.features {
	display: flex;
	flex-direction: column;
	gap: 0.75rem;
	margin: 2rem 0;
	padding: 1.5rem;
	background-color: #f8f8f8;
	border-radius: 8px;
}

.feature-item {
	color: #27ae60;
	font-weight: 500;
}

.options {
	margin: 2rem 0;
}

.option-group {
	margin-bottom: 1.5rem;
}

.option-group label {
	display: block;
	margin-bottom: 0.75rem;
	font-weight: 500;
}

.size-buttons {
	display: flex;
	gap: 0.5rem;
}

.size-btn {
	padding: 0.75rem 1.5rem;
	border: 2px solid #ddd;
	background-color: white;
	cursor: pointer;
	border-radius: 4px;
	font-weight: 500;
	transition: all 0.2s;
}

.size-btn:hover {
	border-color: #e74c3c;
}

.size-btn.active {
	background-color: #e74c3c;
	color: white;
	border-color: #e74c3c;
}

.quantity-selector {
	display: flex;
	align-items: center;
	gap: 0.5rem;
}

.quantity-selector button {
	width: 40px;
	height: 40px;
	border: 1px solid #ddd;
	background-color: white;
	cursor: pointer;
	border-radius: 4px;
	font-size: 1.2rem;
}

.quantity-selector button:hover {
	background-color: #f0f0f0;
}

.quantity-selector input {
	width: 60px;
	height: 40px;
	text-align: center;
	border: 1px solid #ddd;
	border-radius: 4px;
}

.actions {
	display: flex;
	gap: 1rem;
	margin: 2rem 0;
}

.add-to-cart-btn,
.wishlist-btn {
	flex: 1;
	padding: 1rem 2rem;
	border: none;
	border-radius: 4px;
	font-size: 1.1rem;
	font-weight: bold;
	cursor: pointer;
	transition: all 0.2s;
}

.add-to-cart-btn {
	background-color: #e74c3c;
	color: white;
}

.add-to-cart-btn:hover:not(:disabled) {
	background-color: #c0392b;
}

.add-to-cart-btn:disabled {
	opacity: 0.5;
	cursor: not-allowed;
}

.wishlist-btn {
	background-color: white;
	color: #e74c3c;
	border: 2px solid #e74c3c;
}

.wishlist-btn:hover {
	background-color: #f8f8f8;
}

.stock-info {
	color: #666;
	font-size: 0.9rem;
	margin-top: 1rem;
}

.product-meta {
	margin-top: 2rem;
	padding-top: 1rem;
	border-top: 1px solid #eee;
	display: flex;
	flex-direction: column;
	gap: 0.5rem;
}

.meta-item {
	display: flex;
	gap: 0.5rem;
}

.meta-label {
	font-weight: 500;
	color: #666;
}

.meta-value {
	color: #333;
}

/* Product Tabs */
.product-tabs {
	margin-top: 3rem;
	padding-top: 2rem;
	border-top: 2px solid #eee;
}

.tab-headers {
	display: flex;
	gap: 0;
	border-bottom: 2px solid #eee;
}

.tab-header {
	padding: 1rem 2rem;
	background: none;
	border: none;
	border-bottom: 3px solid transparent;
	cursor: pointer;
	font-size: 1rem;
	font-weight: 500;
	color: #666;
	transition: all 0.3s;
	margin-bottom: -2px;
}

.tab-header:hover {
	color: #e74c3c;
}

.tab-header.active {
	color: #e74c3c;
	border-bottom-color: #e74c3c;
}

.tab-content {
	padding: 2rem 0;
}

.tab-pane {
	line-height: 1.8;
	color: #666;
}

.info-table {
	width: 100%;
	border-collapse: collapse;
}

.info-table td {
	padding: 1rem;
	border: 1px solid #eee;
}

.info-table td:first-child {
	font-weight: 500;
	background-color: #f8f8f8;
	width: 200px;
}

.reviews-section h4 {
	margin-bottom: 2rem;
	font-size: 1.2rem;
}

.review-list {
	display: flex;
	flex-direction: column;
	gap: 2rem;
}

.review-item {
	padding-bottom: 2rem;
	border-bottom: 1px solid #eee;
}

.review-item:last-child {
	border-bottom: none;
}

.review-rating {
	color: #ffc107;
	font-size: 1.2rem;
	margin-bottom: 0.5rem;
}

.review-meta {
	display: flex;
	gap: 1rem;
	margin-bottom: 1rem;
}

.review-author {
	font-weight: 500;
	color: #333;
}

.review-date {
	color: #999;
	font-size: 0.9rem;
}

.review-text {
	color: #666;
	line-height: 1.6;
	margin: 0;
}

/* Related Products */
.related-products-section {
	margin-top: 3rem;
	padding-top: 2rem;
	border-top: 2px solid #eee;
}

.related-products-section h3 {
	margin-bottom: 2rem;
	font-size: 1.5rem;
}

.related-products-grid {
	display: grid;
	grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
	gap: 2rem;
}

.loading,
.error {
	text-align: center;
	padding: 4rem;
}

.error a {
	color: #e74c3c;
	text-decoration: none;
}

@media (max-width: 968px) {
	.page-layout {
		flex-direction: column;
	}

	.sidebar {
		width: 100%;
	}

	.product-detail {
		grid-template-columns: 1fr;
	}
}
</style>


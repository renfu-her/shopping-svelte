<template>
	<div class="news-page">
		<div class="container">
			<h1>最新消息</h1>
			<div v-if="loading" class="loading">載入中...</div>
			<div v-else-if="news.length === 0" class="empty">暫無消息</div>
			<div v-else class="news-list">
				<article v-for="item in news" :key="item.id" class="news-item">
					<img v-if="item.image_url" :src="item.image_url" :alt="item.title" />
					<div class="news-content">
						<h2>{{ item.title }}</h2>
						<p class="date">{{ new Date(item.created_at).toLocaleDateString() }}</p>
						<p class="excerpt">{{ item.content }}</p>
					</div>
				</article>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getNews } from '@/services/api.js';

const news = ref([]);
const loading = ref(true);

onMounted(async () => {
	try {
		news.value = await getNews();
	} catch (error) {
		console.error('Failed to load news:', error);
	} finally {
		loading.value = false;
	}
});
</script>

<style scoped>
.news-page {
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

.news-list {
	display: flex;
	flex-direction: column;
	gap: 2rem;
}

.news-item {
	background-color: white;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	overflow: hidden;
	display: flex;
	gap: 2rem;
}

.news-item img {
	width: 300px;
	height: 200px;
	object-fit: cover;
	flex-shrink: 0;
}

.news-content {
	padding: 2rem;
	flex: 1;
}

.news-content h2 {
	margin-top: 0;
	margin-bottom: 0.5rem;
}

.date {
	color: #999;
	font-size: 0.9rem;
	margin-bottom: 1rem;
}

.excerpt {
	line-height: 1.6;
	color: #666;
}

.loading,
.empty {
	text-align: center;
	padding: 4rem;
}

@media (max-width: 768px) {
	.news-item {
		flex-direction: column;
	}

	.news-item img {
		width: 100%;
		height: 200px;
	}
}
</style>


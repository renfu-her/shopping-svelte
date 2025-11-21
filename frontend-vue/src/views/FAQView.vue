<template>
	<div class="faq-page">
		<div class="container">
			<h1>常見問題</h1>
			<div v-if="loading" class="loading">載入中...</div>
			<div v-else-if="faqs.length === 0" class="empty">暫無問題</div>
			<div v-else class="faq-list">
				<div v-for="faq in faqs" :key="faq.id" class="faq-item">
					<h3>{{ faq.question }}</h3>
					<p>{{ faq.answer }}</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getFAQ } from '@/services/api.js';

const faqs = ref([]);
const loading = ref(true);

onMounted(async () => {
	try {
		faqs.value = await getFAQ();
	} catch (error) {
		console.error('Failed to load FAQ:', error);
	} finally {
		loading.value = false;
	}
});
</script>

<style scoped>
.faq-page {
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

.faq-list {
	display: flex;
	flex-direction: column;
	gap: 1.5rem;
}

.faq-item {
	background-color: white;
	padding: 2rem;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.faq-item h3 {
	margin-top: 0;
	margin-bottom: 1rem;
	color: #e74c3c;
}

.faq-item p {
	line-height: 1.8;
	color: #666;
	margin: 0;
}

.loading,
.empty {
	text-align: center;
	padding: 4rem;
}
</style>


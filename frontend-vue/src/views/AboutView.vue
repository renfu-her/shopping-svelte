<template>
	<div class="about-page">
		<div class="container">
			<h1>關於我們</h1>
			<div v-if="loading" class="loading">載入中...</div>
			<div v-else-if="content" class="content" v-html="content"></div>
			<div v-else class="default-content">
				<p>Shopwise 是一個現代化的電商平台，致力於為客戶提供優質的商品和服務。</p>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getAbout } from '@/services/api.js';

const content = ref('');
const loading = ref(true);

onMounted(async () => {
	try {
		const data = await getAbout();
		content.value = data.content || '';
	} catch (error) {
		console.error('Failed to load about:', error);
	} finally {
		loading.value = false;
	}
});
</script>

<style scoped>
.about-page {
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

.content,
.default-content {
	background-color: white;
	padding: 2rem;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	line-height: 1.8;
}

.loading {
	text-align: center;
	padding: 4rem;
}
</style>


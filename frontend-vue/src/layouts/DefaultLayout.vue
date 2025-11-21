<template>
	<div class="layout">
		<Header />
		<main class="main-content">
			<slot />
		</main>
		<Footer />
	</div>
</template>

<script setup>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
</script>

<style scoped>
.layout {
	min-height: 100vh;
	display: flex;
	flex-direction: column;
}

.main-content {
	flex: 1;
}
</style>


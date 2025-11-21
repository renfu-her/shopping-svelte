<template>
	<div class="banner-carousel">
		<div class="carousel-container" @mouseenter="pauseAutoSlide" @mouseleave="resumeAutoSlide">
			<div
				class="carousel-slide"
				:style="{ transform: `translateX(-${currentIndex * 100}%)` }"
			>
				<div
					v-for="(ad, index) in ads"
					:key="index"
					class="slide-item"
					:style="{ backgroundImage: `url(${ad.image_url || ''})` }"
				>
					<div class="slide-content">
						<h2 v-if="ad.title">{{ ad.title }}</h2>
						<p v-if="ad.description">{{ ad.description }}</p>
						<router-link v-if="ad.link" :to="ad.link" class="shop-now-btn">SHOP NOW</router-link>
					</div>
				</div>
			</div>
			<button class="carousel-btn prev" @click="prevSlide">‹</button>
			<button class="carousel-btn next" @click="nextSlide">›</button>
			<div class="carousel-indicators">
				<button
					v-for="(ad, index) in ads"
					:key="index"
					:class="['indicator', { active: currentIndex === index }]"
					@click="goToSlide(index)"
				></button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const props = defineProps({
	ads: {
		type: Array,
		default: () => []
	}
});

const currentIndex = ref(0);
let autoSlideInterval = null;

function nextSlide() {
	currentIndex.value = (currentIndex.value + 1) % props.ads.length;
}

function prevSlide() {
	currentIndex.value = currentIndex.value === 0 ? props.ads.length - 1 : currentIndex.value - 1;
}

function goToSlide(index) {
	currentIndex.value = index;
}

function startAutoSlide() {
	autoSlideInterval = setInterval(() => {
		nextSlide();
	}, 5000);
}

function pauseAutoSlide() {
	if (autoSlideInterval) {
		clearInterval(autoSlideInterval);
	}
}

function resumeAutoSlide() {
	startAutoSlide();
}

onMounted(() => {
	if (props.ads.length > 1) {
		startAutoSlide();
	}
});

onUnmounted(() => {
	if (autoSlideInterval) {
		clearInterval(autoSlideInterval);
	}
});
</script>

<style scoped>
.banner-carousel {
	width: 100%;
	position: relative;
	overflow: hidden;
}

.carousel-container {
	position: relative;
	width: 100%;
	height: 450px;
	overflow: hidden;
}

.carousel-slide {
	display: flex;
	transition: transform 0.5s ease-in-out;
	height: 100%;
}

.slide-item {
	min-width: 100%;
	height: 100%;
	background-size: cover;
	background-position: center;
	display: flex;
	align-items: center;
	justify-content: flex-start;
	padding: 0 4rem;
}

.slide-content {
	max-width: 600px;
	color: #333;
}

.slide-content h2 {
	font-size: 3rem;
	font-weight: bold;
	margin-bottom: 1rem;
}

.slide-content p {
	font-size: 1.2rem;
	margin-bottom: 2rem;
}

.shop-now-btn {
	display: inline-block;
	padding: 1rem 2rem;
	background-color: #e74c3c;
	color: white;
	text-decoration: none;
	border-radius: 4px;
	font-weight: bold;
	transition: background-color 0.2s;
}

.shop-now-btn:hover {
	background-color: #c0392b;
}

.carousel-btn {
	position: absolute;
	top: 50%;
	transform: translateY(-50%);
	background-color: rgba(0, 0, 0, 0.5);
	color: white;
	border: none;
	width: 50px;
	height: 50px;
	border-radius: 50%;
	cursor: pointer;
	font-size: 2rem;
	display: flex;
	align-items: center;
	justify-content: center;
	transition: background-color 0.2s;
	z-index: 10;
}

.carousel-btn:hover {
	background-color: rgba(0, 0, 0, 0.7);
}

.carousel-btn.prev {
	left: 1rem;
}

.carousel-btn.next {
	right: 1rem;
}

.carousel-indicators {
	position: absolute;
	bottom: 1rem;
	left: 50%;
	transform: translateX(-50%);
	display: flex;
	gap: 0.5rem;
	z-index: 10;
}

.indicator {
	width: 12px;
	height: 12px;
	border-radius: 50%;
	border: 2px solid white;
	background-color: transparent;
	cursor: pointer;
	transition: background-color 0.2s;
}

.indicator.active {
	background-color: white;
}
</style>


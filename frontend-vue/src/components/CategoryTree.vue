<template>
	<div class="category-tree">
		<CategoryNode
			v-for="category in categories"
			:key="category.id"
			:category="category"
			:current-slug="currentSlug"
			@click="handleCategoryClick"
		/>
	</div>
</template>

<script setup>
import CategoryNode from './CategoryNode.vue';
import { useRouter } from 'vue-router';

const props = defineProps({
	categories: {
		type: Array,
		default: () => []
	},
	currentSlug: {
		type: String,
		default: null
	},
	useQueryParam: {
		type: Boolean,
		default: false
	}
});

const router = useRouter();

function handleCategoryClick(category) {
	if (category && category.level === 3) {
		if (props.useQueryParam) {
			router.push(`/product?category=${category.slug}`);
		} else {
			router.push(`/product/${category.slug}`);
		}
	}
}
</script>

<style scoped>
.category-tree {
	background-color: transparent;
}
</style>


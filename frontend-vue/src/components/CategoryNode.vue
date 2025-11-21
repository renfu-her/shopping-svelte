<template>
	<div class="category-group">
		<div
			:class="['category-item', `level-${category.level}`, { active: category.slug === currentSlug, clickable: category.level === 3 }]"
			:role="category.level === 3 ? 'button' : 'presentation'"
			:tabindex="category.level === 3 ? 0 : -1"
			@click="handleClick"
			@keydown.enter="handleClick"
			@keydown.space.prevent="handleClick"
		>
			{{ category.name }}
		</div>
		<div v-if="category.children && category.children.length > 0" class="children">
			<CategoryNode
				v-for="child in category.children"
				:key="child.id"
				:category="child"
				:current-slug="currentSlug"
				@click="$emit('click', $event)"
			/>
		</div>
	</div>
</template>

<script setup>
const props = defineProps({
	category: {
		type: Object,
		required: true
	},
	currentSlug: {
		type: String,
		default: null
	}
});

const emit = defineEmits(['click']);

function handleClick() {
	if (props.category.level === 3) {
		emit('click', props.category);
	}
}
</script>

<style scoped>
.category-group {
	margin-bottom: 0.5rem;
}

.category-item {
	padding: 0.5rem;
	border-radius: 4px;
	transition: background-color 0.2s;
}

.category-item.level-1 {
	font-weight: bold;
	font-size: 1.1rem;
}

.category-item.level-2 {
	padding-left: 1.5rem;
	font-weight: 500;
}

.category-item.level-3 {
	padding-left: 2.5rem;
	color: #3498db;
}

.category-item.clickable {
	cursor: pointer;
}

.category-item.level-3:hover,
.category-item.level-3.active {
	background-color: #e3f2fd;
}

.children {
	margin-left: 0.5rem;
}
</style>


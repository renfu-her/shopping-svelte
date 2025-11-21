import { createRouter, createWebHistory } from 'vue-router';
import Layout from '@/layouts/DefaultLayout.vue';

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: '/',
			component: Layout,
			children: [
				{
					path: '',
					name: 'home',
					component: () => import('@/views/HomeView.vue')
				},
				{
					path: 'product',
					name: 'product-list',
					component: () => import('@/views/ProductListView.vue')
				},
				{
					path: 'product/detail/:slug',
					name: 'product-detail',
					component: () => import('@/views/ProductDetailView.vue')
				},
				{
					path: 'cart',
					name: 'cart',
					component: () => import('@/views/CartView.vue')
				},
				{
					path: 'checkout',
					name: 'checkout',
					component: () => import('@/views/CheckoutView.vue')
				},
				{
					path: 'about',
					name: 'about',
					component: () => import('@/views/AboutView.vue')
				},
				{
					path: 'news',
					name: 'news',
					component: () => import('@/views/NewsView.vue')
				},
				{
					path: 'faq',
					name: 'faq',
					component: () => import('@/views/FAQView.vue')
				},
				{
					path: 'blog',
					name: 'blog',
					component: () => import('@/views/BlogView.vue')
				},
				{
					path: 'shop',
					name: 'shop',
					component: () => import('@/views/ShopView.vue')
				},
				{
					path: 'contact',
					name: 'contact',
					component: () => import('@/views/ContactView.vue')
				}
			]
		}
	]
});

export default router;


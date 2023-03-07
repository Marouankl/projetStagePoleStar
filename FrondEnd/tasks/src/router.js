import { createWebHistory, createRouter } from 'vue-router';
import AjouterTask from './components/AjouterTask';
import Accueil from './components/Accueil';

const routes = [
	{
		path: '/',
		name: 'Accueil',
		component: Accueil,
	},
    {
		path: '/AjouterTask',
		name: 'AjouterTask',
		component: AjouterTask,
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
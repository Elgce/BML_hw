import {createRouter, createWebHashHistory} from "vue-router"
const routes = [
    {
        path: '/',
        redirect: '/index/menu1',
        children:[
            {path: '/index/menu1',component: () => import('./components/pages/main1.vue')},
            {path: '/index/menu2',component: () => import('./components/pages/main2.vue')},
            {path: '/index/menu3',component: () => import('./components/pages/main3.vue')},
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router



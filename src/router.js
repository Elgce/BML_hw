import {createRouter, createWebHashHistory} from "vue-router"
const routes = [
    {
        path: '/',
        redirect: '/index/manage/dataset',
        children:[
            {
                path: '/index/manage/dataset',
                component: () => import('./components/pages/main1-1.vue'),
                mata: {title: '我的数据总览'},
                name: '我的数据总览',
            },
            {
                path: '/index/manage/dataset/insert',
                component: () => import('./components/pages/main2.vue'),
                mata: {title: '导入'},
                name: '导入',
            },
            {
                path: '/index/menu3',
                component: () => import('./components/pages/main3.vue'),
                mata: {title: '查看与标注'},
                name: '查看与标注',
            },
            {
                path: '/index/manage/dataset/create',
                component: () => import('./components/pages/CreateSet.vue'),
                mata: {title: '创建数据集'},
                name: '创建数据集',
            },
            {
                path: '/index/manage/blank',
                component: () => import('./components/pages/BlankPage.vue'),
                name: '跳转空白页',
                meta: {title:'跳转空白页'}
            },
            {
                path: '/index/manage/test',
                component: () => import('./components/pages/main4.vue'),
                name: '测试页面',
                meta: {title:'测试页面'}
            },
            {
                path: '/index/manage/dataset/pic/addtag',
                component: () => import('./components/pages/AddTag.vue'),
                name: '添加图片标签',
                meta: {title:'添加图片标签'}
            },
            
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router



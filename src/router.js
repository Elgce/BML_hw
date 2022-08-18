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
                component: () => import('./components/pages/AddTagGroup.vue'),
                name: '标签组管理',
                meta: {title:'标签组管理'}
            },
            {
                path: '/index/manage/dataset/video/addtag',
                component: () => import('./components/pages/VideoTag.vue'),
                name: '添加视频标签',
                meta: {title:'添加视频标签'}
            },
            {
                path: '/index/manage/dataset/text/addtag',
                component: () => import('./components/pages/TxtTag.vue'),
                name: '添加文本标签',
                meta: {title:'添加文本标签'}
            },
            {
                path: '/index/manage/dataset/text/taggroup',
                component: () => import('./components/pages/TagGroup.vue'),
                name: '标签管理',
                meta: {title:'标签管理'}
            },
            {
                path: '/index/manage/dataset/pic/label/blank',
                component: () => import("./components/pages/BlankLabel.vue"),
                name: '图片标签空白页',
                meta: {title:'图片标签空白页'}
            },
            {
                path: '/index/manage/dataset/txt/label/blank',
                component: () => import("./components/pages/BlankTxt.vue"),
                name: '文本标签空白页',
                meta: {title:'文本标签空白页'}
            },
            {
                path: '/index/3-1',
                component: () => import("./components/pages/TextMarking.vue"),
                name: '标注',
                meta: {title:'标注'}
            },
            {
                path: '/index/3-2',
                component: () => import("./components/pages/VideoMarking.vue"),
                name: '视频标注',
                meta: {title:'视频标注'}
            },
            {
                path: '/index/4-1',
                component: () => import("./components/pages/PlatformIntroduction.vue"),
                name: '平台说明',
                meta: {title:'平台说明'}
            }
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router



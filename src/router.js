import {createRouter, createWebHashHistory} from "vue-router"
const routes = [
    {
        path: '/',
        redirect: '/index/manage/dataset',
        children:[
            {
                path: '/index/manage/dataset',
                component: () => import('./components/pages/Main.vue'),
                mata: {title: '我的数据总览'},
                name: '我的数据总览',
            },
            {
                path: '/index/manage/dataset/insert',
                component: () => import('./components/pages/Import.vue'),
                mata: {title: '导入'},
                name: '导入',
            },
            {
                path: '/index/menu3',
                component: () => import('./components/pages/PicOverview.vue'),
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
                path: '/index/manage/dataset/text/similarity',
                component: () => import('./components/pages/TxtSim.vue'),
                name: '文本相似度',
                meta: {title:'文本相似度'}
            },
            {
                path: '/index/manage/dataset/text/taggroup',
                component: () => import('./components/pages/TagGroup.vue'),
                name: '标签管理',
                meta: {title:'标签管理'}
            },
            {
                path: '/index/manage/dataset/pic/taggroupblank',
                component: () => import('./components/pages/BlankTagGroup.vue'),
                name: '标签组管理空白页',
                meta: {title:'标签组管理空白页'}
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
                path: '/index/manage/dataset/txt/blank',
                component: () => import("./components/pages/BlankTxtl.vue"),
                name: '文本标注空白页',
                meta: {title:'文本标注空白页'}
            },
            {
                path: '/index/manage/dataset/txt/extract/blank',
                component: () => import("./components/pages/BlankExtract.vue"),
                name: '文本抽取标签空白页',
                meta: {title:'文本抽取标签空白页'}
            },
            {
                path: '/index/manage/dataset/txt/extracted/blank',
                component: () => import("./components/pages/BlankExtracted.vue"),
                name: '文本抽取空白页',
                meta: {title:'文本抽取空白页'}
            },
            {
                path: '/index/manage/dataset/textmarking',
                component: () => import("./components/pages/TextMarking.vue"),
                name: '文本标注',
                meta: {title:'文本标注'}
            },
            {
                path: '/index/manage/dataset/blank/similarity',
                component: () => import("./components/pages/BlankSim.vue"),
                name: '文本相似度空白页',
                meta: {title:'文本相似度空白页'}
            },
            {
                path: '/index/manage/dataset/blank/pic',
                component: () => import("./components/pages/BlankPic.vue"),
                name: '图片展示空白页',
                meta: {title:'图片展示空白页'}
            },
            {
                path: '/index/manage/dataset/blank/piced',
                component: () => import("./components/pages/BlankPiced.vue"),
                name: '图片标注空白页',
                meta: {title:'图片标注空白页'}
            },
            {
                path: '/index/manage/dataset/video/mark',
                component: () => import("./components/pages/VideoMarking.vue"),
                name: '视频分类',
                meta: {title:'视频分类'}
            },
            {
                path: '/index/manage/dataset/video/split',
                component: () => import("./components/pages/VideoSplitting.vue"),
                name: '视频分割',
                meta: {title:'视频分割'}
            },
            {
                path: '/index/manage/dataset/audio/mark',
                component: () => import("./components/pages/AudioMarking.vue"),
                name: '音频分类',
                meta: {title:'音频分类'}
            },
            {
                path: '/index/manage/dataset/audio/split',
                component: () => import("./components/pages/AudioSplitting.vue"),
                name: '音频分割',
                meta: {title:'音频分割'}
            },
            {
                path: '/index/manage/dataset/4-2',
                component: () => import("./components/pages/Export.vue"),
                name: '导出',
                meta: {title:'导出'}
            },
            {
                path: '/index/manage/dataset/wholetxt',
                component: () => import("./components/pages/ExtractText.vue"),
                name: '文本实体抽取',
                meta: {title:'文本实体抽取'}
            },
            {
                path: '/index/manage/dataset/extracttag',
                component: () => import("./components/pages/ExtractTag.vue"),
                name: '文本实体抽取数据',
                meta: {title:'文本实体抽取数据'}
            },
            {
                path: '/index/manage/dataset/blank/video',
                component: () => import("./components/pages/BlankVideo.vue"),
                name: '视频分类空白页',
                meta: {title:'视频分类空白页'}
            },
            {
                path: '/index/manage/4-2',
                component: () => import("./components/pages/PlatformIntroduction.vue"),
                name: '平台说明',
                meta: {title:'平台说明'}
            },
            {
                path: '/index/manage/dataset/picmarking',
                component: () => import("./components/pages/PicMarking.vue"),
                name: '图片标注',
                meta: {title:'图片标注'}
            },
            {
                path: '/index/manage/dataset/pic/managegroupblank',
                component: () => import("./components/pages/BlankManageGroup.vue"),
                name: '标签管理空白页',
                meta: {title:'标签管理空白页'}
            },
            {
                path: '/index/manage/dataset/pic/machinelearning',
                component: () => import("./components/pages/MachineLearning.vue"),
                name: '机器学习',
                meta: {title:'机器学习'}
            },
            
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router



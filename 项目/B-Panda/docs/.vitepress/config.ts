import { defineConfig } from 'vitepress'
//import { autoGenerateSidebar } from 'press-util'
import vite from './vite.config'
import theme from './theme'

export default defineConfig({
  base: '/',
  appearance: true,
  title: 'B-Panda|自动化工具集',
  lastUpdated: true,
  // 标签页logo
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/logo.png' }],
    ['link', { rel: 'manifest', href: '/manifest.webmanifest' }], // chrome pwa
  ],
  markdown: {
    lineNumbers: true,
    image: {
      lazyLoading: true,
    }
  },

  themeConfig: {
    logo: '/logo.png',
    ignoreDeadLinks: true,
    lastUpdatedText: '最近更新于',
    // 2/3/4级标题均形成目录
    outline: [2, 4],
    outlineTitle: '目录',
    nav: [{
      text: '🎯介绍',
      link: '/overview.md'
    },
    {
      text: '📒文档',
      link: '/docc/'
    },
    {
      text:'👀网站监控系统',
      link:'/monitor/'
    },
    {
      text: '😄关于我',
      link: '/about.md'
    },
  ],

  // 手动配置 sidebar
  sidebar: {
    // 当用户位于 'docc' 目录时，会显示此侧边栏
    '/docc/': [
      {
        text: 'BTool文档',
        items: [
          { text: '介绍', link: '/docc/index.md' },
          { text: 'BTools', link: '/docc/BTools.md' },
          { text: '蓝图开发模式', link: '/docc/Blueprint.md' },
          { text: 'Vitepress搭建记录', link: '/docc/Vitepress.md' },
          { text: 'Docker部署记录',link:'/docc/docker.md'},
          { text: 'App主路由', link: '/docc/app.md' },
          { text: '路由模块', link: '/docc/routes.md' },
          { text: '样式风格', link: '/docc/style.md' },
          { text: '功能模块', link: '/docc/utils.md' },
          { text: '系统资源监控', link: '/docc/system.md'},
        ]
      }
    ],

    // 当用户位于 'monitor' 目录时，会显示此侧边栏
    '/monitor/': [
      {
        text: '网站监控系统文档',
        items: [
          { text: '介绍', link: '/monitor/index.md' },
          { text: '代码分析', link: '/monitor/jiesao.md' }
        ]
      }
    ]
  },

  // 编辑链接
  editLink: {
    pattern: 'https://github.com/bx33661/B-Panda',
    text: '在Github编辑',
  },

  // 搜索
  search: {
    provider: 'local',
  },
  
  // 在这里添加右大括号
  },
  vite,
})
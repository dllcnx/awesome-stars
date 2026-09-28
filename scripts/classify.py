"""Starred-repo taxonomy: first matching rule wins (MECE)."""

from __future__ import annotations

from typing import Any

# (category_id, subcategory_id, title used only for docs)
CATEGORIES: list[dict[str, Any]] = [
    {
        "id": "ai",
        "title": "AI 与智能体",
        "emoji": "🤖",
        "blurb": "大模型、Agent、Skills、提示词与 AI 应用。对应原 List「⭐️⭐️⭐️⭐️⭐️AI」，并补进未归档的新星标。",
        "subs": [
            ("ai-agent", "Agent、Skills 与 Claude Code"),
            ("ai-model", "模型、推理、网关与生成"),
            ("ai-app", "应用、教程与资源"),
        ],
    },
    {
        "id": "gis",
        "title": "测绘地理与三维可视化",
        "emoji": "🌍",
        "blurb": "Cesium、Mapbox、GIS 引擎、三维地球、气象海洋与地理数据。对应原 List「⭐️专业领域」，并把散落在前端/Demo 里的 Cesium 案例收拢回来。",
        "subs": [
            ("gis-cesium", "Cesium 与三维地球"),
            ("gis-map", "Mapbox / 地图引擎与 GIS 库"),
            ("gis-data", "地理数据、气象海洋与转换"),
        ],
    },
    {
        "id": "proxy",
        "title": "网络代理与路由",
        "emoji": "🛰️",
        "blurb": "代理客户端、规则、面板与软路由。对应原 List「科学网络与路由」。",
        "subs": [
            ("proxy-core", "内核、客户端与面板"),
            ("proxy-rule", "规则、订阅与一键脚本"),
            ("proxy-router", "软路由、OpenWrt 与优选 IP"),
        ],
    },
    {
        "id": "learn",
        "title": "学习资料、面试与 Awesome",
        "emoji": "📚",
        "blurb": "教程、面试、算法、技术周刊与精选清单。对应原 List「学习资料」。",
        "subs": [
            ("learn-interview", "面试、算法与计算机基础"),
            ("learn-frontend", "前端教程与最佳实践"),
            ("learn-awesome", "Awesome、书单与综合资源"),
        ],
    },
    {
        "id": "ssg",
        "title": "静态站点、博客与文档",
        "emoji": "📝",
        "blurb": "博客引擎、文档站、评论系统与主题。对应原 List「静态站点与文档构建」。",
        "subs": [
            ("ssg-engine", "静态站点与博客引擎"),
            ("ssg-theme", "主题、评论与文档工具"),
        ],
    },
    {
        "id": "selfhost",
        "title": "自托管软件与系统工具",
        "emoji": "🧰",
        "blurb": "NAS、媒体、笔记、Git 托管、桌面应用与系统增强。对应原 List「软件与服务」。",
        "subs": [
            ("selfhost-media", "媒体、网盘与阅读"),
            ("selfhost-note", "笔记、CMS 与知识库"),
            ("selfhost-ops", "Git 托管、证书、Docker 与运维"),
            ("selfhost-desktop", "桌面应用与系统增强"),
        ],
    },
    {
        "id": "mobile",
        "title": "跨端与移动开发",
        "emoji": "📱",
        "blurb": "小程序、混合应用、React Native、Flutter、Cordova 与 Android。从原「⭐️前端」中拆出。",
        "subs": [
            ("mobile-mini", "小程序与跨端框架"),
            ("mobile-native", "Cordova / Android / Flutter / RN"),
        ],
    },
    {
        "id": "ui",
        "title": "UI 组件、动效与可视化",
        "emoji": "🎨",
        "blurb": "组件库、图表、动画、拖拽、Canvas/WebGL 与编辑器。从原「⭐️前端」和「优秀案例与 DEMO」拆出界面层。",
        "subs": [
            ("ui-lib", "组件库与 Design System"),
            ("ui-angular", "Angular 组件"),
            ("ui-chart", "图表与数据可视化"),
            ("ui-motion", "动画、拖拽与交互"),
            ("ui-editor", "编辑器、Markdown 与画布"),
        ],
    },
    {
        "id": "fw",
        "title": "前端框架与运行时",
        "emoji": "⚛️",
        "blurb": "Vue / React / Angular / Svelte 等框架核心与配套生态。对应原「⭐️前端」「⭐️常用」中的框架本体。",
        "subs": [
            ("fw-vue", "Vue / Nuxt"),
            ("fw-react", "React / Next"),
            ("fw-angular", "Angular"),
            ("fw-svelte", "Svelte / Solid / 其他框架"),
            ("fw-util", "请求、状态、工具库与运行时"),
        ],
    },
    {
        "id": "tooling",
        "title": "工程化与开发工具",
        "emoji": "🔧",
        "blurb": "构建打包、包管理、测试、Lint、脚手架与编辑器插件。对应原 List「开发辅助」。",
        "subs": [
            ("tool-build", "构建、打包与包管理"),
            ("tool-quality", "测试、Lint、Git 与发布"),
            ("tool-cli", "脚手架、CLI 与编辑器插件"),
        ],
    },
    {
        "id": "backend",
        "title": "后端、数据库与全栈",
        "emoji": "🗄️",
        "blurb": "Node/Java 服务端、ORM、微服务与全栈方案。对应原 List「⭐️开发」中的后端部分。",
        "subs": [
            ("be-node", "Node.js 服务端与 ORM"),
            ("be-java", "Java / 其他后端"),
            ("be-full", "全栈后台与低代码"),
        ],
    },
    {
        "id": "template",
        "title": "模板、后台与解决方案",
        "emoji": "📦",
        "blurb": "Admin 模板、企业站与可落地的整套方案。对应原 List「模版社区与解决方案」。",
        "subs": [
            ("tpl-admin", "Admin 与后台模板"),
            ("tpl-site", "站点模板与脚手架方案"),
        ],
    },
    {
        "id": "demo",
        "title": "示例、Demo 与实验",
        "emoji": "🧪",
        "blurb": "真正偏案例、实验和小玩具的收藏。原「优秀案例与 DEMO」过大，这里只保留拆分后仍不像库的部分。",
        "subs": [
            ("demo-web", "前端案例与特效"),
            ("demo-misc", "其他示例"),
        ],
    },
    {
        "id": "other",
        "title": "其它",
        "emoji": "📎",
        "blurb": "无法稳定归入上面主题的项目。目前只剩少量无法归类的仓库。",
        "subs": [
            ("other-misc", "未归类"),
        ],
    },
]

CAT_ORDER = [c["id"] for c in CATEGORIES]
CAT_META = {c["id"]: c for c in CATEGORIES}
SUB_TITLES = {sid: title for c in CATEGORIES for sid, title in c["subs"]}


def _blob(repo: dict) -> dict:
    name = repo.get("full_name") or ""
    desc = repo.get("description") or ""
    topics = [t.lower() for t in (repo.get("topics") or [])]
    owner, _, repo_name = name.lower().partition("/")
    text = f"{name} {desc} {' '.join(topics)}".lower()
    return {
        "full": name.lower(),
        "owner": owner,
        "repo": repo_name,
        "desc": desc.lower(),
        "topics": set(topics),
        "text": text,
        "lang": (repo.get("language") or "").lower(),
    }


def _has(text: str, words: tuple[str, ...] | list[str]) -> bool:
    return any(w in text for w in words)


def _topic(b: dict, words: tuple[str, ...] | list[str]) -> bool:
    return any(w in b["topics"] for w in words)


def _name_in(b: dict, names: set[str]) -> bool:
    return b["full"] in names or b["repo"] in names


AI_REPOS = {
    "liuup/claude-code-analysis",
    "liyupi/ai-guide",
    "linshenkx/prompt-optimizer",
    "jefferyhcool/bilinote",
    "deepseek-ai/deepseek-harness",
    "zhaoxuya520/reverse-skill",
    "k-dense-ai/scientific-agent-skills",
    "datawhalechina/hello-agents",
    "liguodongiot/llm-action",
    "diegosouzapw/omniroute",
    "xai-org/grok-1",
    "comfy-org/workflow_templates",
    "openclaw/openclaw",
    "nousresearch/hermes-agent",
    "michael-a-kuykendall/shimmy",
    "javaht/claude-desktop-zh-cn",
    "mattpocock/skills",
    "phuryn/pm-skills",
    "mvanhorn/last30days-skill",
    "kepano/obsidian-skills",
    "yishentu/claudian",
    "adddaao/claude-hud",
    "colbymchenry/codegraph",
    "multica-ai/andrej-karpathy-skills",
    "nextlevelbuilder/ui-ux-pro-max-skill",
    "farion1231/cc-switch",
    "luongnv89/claude-howto",
    "666ghj/mirafish",
    "dayuanjiang/next-ai-draw-io",
    "lencx/noi",
    "instantx-research/instantid",
    "nagadomi/waifu2x",
    "chatgptnextweb/nextchat",
    "significant-gravitas/autogpt",
    "tencentarc/gfpgan",
    "advimman/lama",
    "husky-dot/xiaozhi",
}

GIS_REPOS = {
    "cesiumgs/cesium",
    "mapbox/mapbox-gl-js",
    "hongfaqiu/mvtimageryprovider",
    "supermap/iclient3d-for-webgl",
    "mesh-3d/cesium-vectortile-gl",
    "hongfaqiu/cesium-extends",
    "jiawanlong/threejs-examples",
    "jiawanlong/cesium-examples",
    "jiawanlong/go-cesium-view",
    "chenkuangkuang/world-countries-geojson",
    "hongfaqiu/tiffimageryprovider",
    "z2586300277/three-cesium-examples",
    "hujiulin/cesiumjs-tutorial",
    "opendrift/opendrift",
    "hongfaqiu/cesium-wind-layer",
    "quietly-20201113/cesium-windy-canvas",
    "tingyuxuan2302/cesium-vue3-vite",
    "lyqh-ctx/cesiumtx",
    "zouyaoji/vue-cesium",
    "mikeswei/cesiumvectortile",
    "cesium-plugin/cesium-navigation-es6",
    "nshen/vite-plugin-cesium",
    "zhangti0708/cesium-videoshed",
    "zhangti0708/cesium-viewshed",
    "zhangti0708/cesium-materialline",
    "zhangti0708/new-cesiumgraph",
    "zhangti0708/cesium-graphicbuffer",
    "zhangti0708/cesium-measure",
    "xuzhusheng/gltf-to-3d-tiles",
    "fanvanzh/3dtiles",
    "zhangti0708/cesium-examples",
    "zhangti0708/cesium-city3d",
    "potree/potree",
    "analyticalgraphicsinc/czml-writer",
    "iooooo/drawhelperforcesium1.7.x",
    "turfjs/turf",
    "crunchydata/pg_tileserv",
    "mapbox/mapbox-gl-draw",
    "proj4js/proj4js",
    "happyport/mapboxgl-echarts",
    "lzxue/echartslayer",
    "mapbox/mapbox-gl-compare",
    "mapbox/storytelling",
    "wrld3d/wrld.js",
    "jscastro76/threebox",
    "mourner/suncalc",
    "osgeo/gdal",
    "wavded/ogr2ogr",
    "modood/administrative-divisions-of-china",
    "thegisdev/mapbox-gl-draw-rectangle-mode",
    "datadesk/print-map-maker",
    "maplibre/maputnik",
    "cschwarz/wkx",
    "visgl/deck.gl",
}

PROXY_REPOS = {
    "hotseo123/jichangtizi-youhuima",
    "nelvko/clash-for-linux-install",
    "metacubex/clashx.meta",
    "clash-verge-rev/clash-verge-rev",
    "yanue/v2rayu",
    "2dust/clashn",
    "zzzgydi/clash-verge",
    "jinwyp/one_click_script",
    "ermaozi/get_subscribe",
    "jrohy/trojan",
    "p4gefau1t/trojan-go",
    "hackl0us/ss-rule-snippet",
    "trojan-gfw/trojan",
    "freefq/free",
    "franzkafayu/x-ui",
    "vaxilu/x-ui",
    "careywang/sub-web",
    "tindy2013/subconverter",
    "blackmatrix7/ios_rule_script",
    "loyalsoldier/clash-rules",
    "metacubex/mihomo",
    "xiu2/cloudflarespeedtest",
    "badafans/better-cloudflare-ip",
    "qv2ray/qv2ray",
    "trojanpanel/install-script",
    "proxysu/proxysu",
    "jrohy/multi-v2ray",
    "wulabing/xray_onekey",
    "xtls/xray-core",
    "mack-a/v2ray-agent",
    "vernesong/openclash",
    "juewuy/shellcrash",
    "bannedbook/fanqiang",
    "2dust/v2rayng",
    "2dust/v2rayn",
    "tunnelblick/tunnelblick",
    "cenmrev/v2rayx",
    "233boy/v2ray",
    "v2fly/v2ray-core",
    "yinghuocho/firefly-proxy",
    "kiddin9/kwrt",
    "istoreos/istoreos",
    "auk9527/are-u-ok",
}

LEARN_REPOS = {
    "codecrafters-io/build-your-own-x",
    "asabeneh/30-days-of-python",
    "anduin2017/howtocook",
    "qufei1993/nextjs-learn-cn",
    "jaywcjlove/awesome-mac",
    "neetcode-gh/leetcode",
    "snailclimb/javaguide",
    "milanm/devops-roadmap",
    "rd2coding/road2coding",
    "wu529778790/wu529778790.github.io",
    "ebookfoundation/free-programming-books",
    "jwasham/coding-interview-university",
    "firstcontributions/first-contributions",
    "wangdoc/typescript-tutorial",
    "john-smilga/node-express-course",
    "paradite/frontend-encyclopedia",
    "jonasschmedtmann/complete-javascript-course",
    "jonasschmedtmann/ultimate-react-course",
    "krahets/hello-algo",
    "asabeneh/30-days-of-react",
    "zuopf769/notebook",
    "haizlin/fe-interview",
    "mrxujiang/frontend-developer-roadmap",
    "denysdovhan/wtfjs",
    "doocs/leetcode",
    "alienzhou/frontend-tech-list",
    "advanced-frontend/daily-interview-question",
    "cyc2018/cs-notes",
    "dujltqzv/some-many-books",
    "asabeneh/30-days-of-javascript",
    "zhonghuasheng/tutorial",
    "kiesun/all-of-frontend",
    "scutan90/deeplearning-500-questions",
    "sudheerj/javascript-interview-questions",
    "chokcoco/css-inspiration",
    "careercup/ctci-6th-edition-javascript",
    "dylanaraps/pure-bash-bible",
    "xxlllq/system_architect",
    "521xueweihan/hellogithub",
    "labuladong/fucking-algorithm",
    "microsoft/web-dev-for-beginners",
    "bradtraversy/50projects50days",
    "qianguyihao/web",
    "zhongmeizhi/fed-note",
    "ascoders/weekly",
    "frontendgithub/frontendgithub",
    "bradtraversy/vanillawebprojects",
    "thedaviddias/front-end-checklist",
    "yangshun/tech-interview-handbook",
    "ryanmcdermott/clean-code-javascript",
    "getify/you-dont-know-js",
    "goldbergyoni/nodebestpractices",
    "trekhleb/javascript-algorithms",
    "thealgorithms/javascript",
    "chalarangelo/30-seconds-of-code",
    "leonardomso/33-js-concepts",
    "freecodecamp/freecodecamp",
    "nilbuild/developer-roadmap",
    "gluu1/front-end-navigator",
    "roger-hiro/blogfn",
    "fengshi123/blog",
    "bin392328206/six-finger",
    "wususu/effective-resourses",
    "airbnb/javascript",
    "patrickjs/awesome-angular",
    "solido/awesome-flutter",
    "vitejs/awesome-vite",
    "vuepress/awesome-vuepress",
    "rollup/awesome",
    "xitu/gold-miner",
    "jaywcjlove/handbook",
    "semlinker/angular-faq",
    "markyun/markyun",
    "lgwebdream/fe-interview",
    "ityouknow/spring-boot-book",
    "potoyang/spring-in-action-v6-translate",
    "potoyang/spring-in-action-v5-translate",
    "hoochanlon/hamuleite",
    "mgechev/angular-performance-checklist",
    "nimoc/gulp-book",
    "microsoft/typescript-wiki",
}

SSG_REPOS = {
    "vuepress-theme-hope/vuepress-theme-hope",
    "giscus/giscus",
    "zmister2016/mrdoc",
    "gohugoio/hugo",
    "jekyll/jekyll",
    "docsifyjs/docsify",
    "hexojs/hexo",
    "vuejs/vitepress",
    "star7th/showdoc",
    "twikoojs/twikoo",
    "chengzhongxue/halo-theme-hao",
    "halo-dev/halo",
    "notionnext-org/notionnext",
    "gatsbyjs/gatsby",
    "typecho/typecho",
    "dllcnx/leanote-simple-pebbles",
    "dllcnx/leanote-fonte",
    "vuepress/core",
    "vuejs/vuepress",
    "leanote/leanote",
    "dllcnx/docker-leanote",
    "zthxxx/hexo-theme-wikitten",
    "eyhn/hexo-helper-live2d",
    "d0n9x1n/hexo-tag-cloud",
    "d0n9x1n/hexo-blog-encrypt",
    "wongminho/hexo-theme-miho",
    "mrminfive/hexo-theme-skapp",
    "iissnan/hexo-theme-next",
    "gitalk/gitalk",
    "fechin/hexo-theme-diaspora",
    "levblanc/hexo-theme-aero-dual",
    "dllcnx/hexo-toc",
    "hakimel/reveal.js",
    "timqian/chinese-independent-blogs",
    "ralscha/blog",
}

SELFHOST_REPOS = {
    "moontechlab/lunatv",
    "memstechtips/winhance",
    "massgravel/microsoft-activation-scripts",
    "bitwarden/server",
    "certimate-go/certimate",
    "stirling-tools/stirling-pdf",
    "xhongc/music-tag-web",
    "ffmpeg/ffmpeg",
    "iina/iina",
    "monlor/docker-xiaoya",
    "gedoor/legado",
    "xiu2/yuedu",
    "hectorqin/reader",
    "xiaoyadev/xiaoya-alist",
    "alistgo/alist",
    "icewhaletech/casaos",
    "brave/brave-browser",
    "helloxz/onenav",
    "strapi/strapi",
    "themepark-dev/theme.park",
    "gethomepage/homepage",
    "jinenge/tvbox",
    "eugeny/tabby",
    "maotoumao/musicfree",
    "corentinth/it-tools",
    "liu673cn/bug",
    "nondanee/unblockneteasemusic",
    "maxlicheng/luci-app-unblockmusic",
    "kuingsmile/piclist",
    "qbittorrent/search-plugins",
    "navidrome/navidrome",
    "molunerfinn/picgo",
    "picgo/picgo-core",
    "obsproject/obs-studio",
    "qbittorrent/qbittorrent",
    "windmill-labs/windmill",
    "usememos/memos",
    "czbix/qb-web",
    "cym1102/nginxwebui",
    "nginxproxymanager/nginx-proxy-manager",
    "unblockneteasemusic/luci-app-unblockneteasemusic",
    "desirefire/animetrackerlist",
    "ngosang/trackerslist",
    "acmesh-official/acme.sh",
    "jellyfin/jellyfin",
    "go-gitea/gitea",
    "mortennn/dozer",
    "ronggang/transmission-web-control",
    "xanderiye/tmm-cracker",
    "dzhuang/tinymediamanager-docker",
    "charliemonroe/downieextensions",
    "automaapp/automa",
    "lyswhut/lx-music-desktop",
    "johncoates/aerial",
    "onlyoffice/onlyoffice-owncloud",
    "onlyoffice/docker-onlyoffice-nextcloud",
    "onlyoffice/onlyoffice-nextcloud",
    "onlyoffice/docker-onlyoffice-owncloud",
    "ohmyzsh/ohmyzsh",
    "powerlevel9k/powerlevel9k",
    "mbadolato/iterm2-color-schemes",
    "gogs/gogs",
    "ventoy/ventoy",
    "zhaoolee/chromeappheroes",
    "supermarin/powerline-fonts",
    "andreafrancia/trash-cli",
    "beyondtranslate/beyondtranslate-ce",
    "aidenlx/obsidian-bridge",
    "aidenlx/marginnote-companion",
    "wechatsync/wechatsync",
    "lowlighter/metrics",
    "jaywcjlove/awesome-mac",  # learning/awesome already; keep mac apps in learn
    "dllcnx/pikpak",
}

MOBILE_REPOS = {
    "ionic-team/ionic-framework",
    "eleme/morjs",
    "react/react-native",
    "nervjs/taro",
    "dllcnx/tts",
    "dllcnx/cordova-plugin-chinese-tts",
    "mauron85/cordova-plugin-background-geolocation",
    "zws-china/wechat-coordinate",
    "lovedise/permissiongen",
    "getactivity/xxpermissions",
    "iampawan/flutter-music-player",
    "ikew0ng/swipebacklayout",
    "immortalz/stereoview",
    "mouhsine786/macaddres",
    "katzer/cordova-plugin-local-notifications",
    "mohamed-salah/macaddress",
    "jd-opensource/nutui",
    "airyland/vux",
    "didi/cube-ui",
    "youzan/vant",
    "didi/mand-mobile",
    "liriliri/eruda",
    "tencent/vconsole",
}

UI_REPOS = {
    "element-plus/element-plus",
    "antvis/x6",
    "datav-team/datav",
    "vuetifyjs/vuetify",
    "shadcn-ui/ui",
    "wangeditor-team/wangeditor",
    "preactjs/preact",
    "nilbuild/driver.js",
    "videojs/video.js",
    "layui/layui",
    "vueup/vue-quill",
    "daidaibg/ioftv-screen",
    "plotly/plotly.js",
    "airbnb/lottie",
    "lucide-icons/lucide",
    "tencent/cherry-markdown",
    "doocs/md",
    "nolimits4web/atropos",
    "bytedance/xgplayer",
    "mozilla/pdf.js",
    "chartjs/chart.js",
    "apexcharts/apexcharts.js",
    "bpmn-io/bpmn-js",
    "adrai/flowchart.js",
    "kingsora/overlayscrollbars",
    "grsmto/simplebar",
    "mdbootstrap/perfect-scrollbar",
    "gka/chroma.js",
    "bmsvieira/moovie.js",
    "mattboldt/typed.js",
    "sortablejs/sortable",
    "bevacqua/dragula",
    "emotion-js/emotion",
    "adopted-ember-addons/ember-drag-sort",
    "kornelski/slip",
    "kutlugsahin/smooth-dnd",
    "qgh810/dnd",
    "fortawesome/font-awesome",
    "schum123/svelte-loading-spinners",
    "atomiks/tippyjs",
    "rob-balfre/svelte-select",
    "simonwep/pickr",
    "tailwindlabs/tailwindcss",
    "mrdoob/three.js",
    "apache/echarts",
    "valqelyan/svelte-grid",
    "yuri2peter/win10-ui",
    "fabricjs/fabric.js",
    "bootstrap-vue/bootstrap-vue",
    "mui/material-ui",
    "carbon-design-system/carbon",
    "c0bra/svelma",
    "hustcc/canvas-nest.js",
    "diygod/aplayer",
    "daybrush/moveable",
    "jenil/bulmaswatch",
    "x-extends/vxe-table",
    "beizhedenglong/rough-charts",
    "thlorenz/brace",
    "chairuosen/vue2-ace-editor",
    "mauricius/vue-draggable-resizable",
    "kirillmurashov/vue-drag-resize",
    "israelzablianov/draggable-vue-directive",
    "ecomfe/vue-echarts",
    "unocss/unocss",
    "jbaysolutions/vue-grid-layout",
    "chrisrhymes/bulma-block-list",
    "hunzaboy/cool-checkboxes-for-bulma.io",
    "dllcnx/svelma-pro",
    "elcobvg/svelte-bulma-forms",
    "elcobvg/svelte-bulma-components",
    "hperrin/svelte-material-ui",
    "dllcnx/css3-anime",
    "paveldogreat/webgl-fluid-simulation",
    "highcharts/highcharts-vue",
    "michalsnik/aos",
    "mattlewis92/angular-calendar",
    "angular/flex-layout",
    "swimlane/ngx-dnd",
    "swimlane/ngx-charts",
    "merri-ment/lazy-line-painter",
    "animate-css/animate.css",
    "obaidurrehman/ng-drag-drop",
    "ajaxorg/ace-builds",
    "hammerjs/hammer.js",
    "nosir/cleave.js",
    "nosir/cleave-zen",
    "codyhouse/3d-rotating-navigation",
    "codyhouse/3d-bold-navigation",
    "juliangarnier/anime",
    "scttcper/ngx-toastr",
    "ag-grid/ag-grid",
    "scttcper/ngx-color",
    "ng-zorro/ng-zorro-antd",
    "elemefe/element-angular",
    "yuanfux/vue-metro-tile",
    "ng-bootstrap/ng-bootstrap",
    "minimac/magic",
    "akveo/ng2-smart-table",
    "1inus/ng.tree",
    "1inus/ngx.layer",
    "zefoy/ngx-color-picker",
    "cipchk/ngx-weui",
    "nobitagit/ng-material-floating-button",
    "nobitagit/react-material-floating-button",
    "xieziyu/ngx-echarts",
    "cordobo/angularx-qrcode",
    "superiorjt/angular2-qrcode",
    "casesandberg/react-color",
    "fkhadra/react-toastify",
    "tomchentw/react-toastr",
    "jesusoterogomez/react-notify-toast",
    "valor-software/ng2-dragula",
    "sortablejs/ngx-sortablejs",
    "clauderic/react-sortable-hoc",
    "valor-software/ng2-tree",
    "aitboudad/ngx-loading-bar",
    "akserg/ng2-toasty",
    "akserg/ng2-slim-loading-bar",
    "akserg/ng2-dnd",
    "tahashahid/ng2-floating-button",
    "rpocklin/angular-timeline",
    "josdejong/jsoneditor",
    "dschnelldavis/angular2-json-schema-form",
    "jdorn/json-editor",
    "reactchartjs/react-chartjs-2",
    "nolimits4web/swiper",
    "kimmobrunfeldt/progressbar.js",
    "malihu/malihu-custom-scrollbar-plugin",
    "zpao/qrcode.react",
    "davidshimjs/qrcodejs",
    "lin-xin/schart.js",
    "alvarotrigo/fullpage.js",
    "niklasvh/html2canvas",
    "parallax/jspdf",
    "e-oj/magic-grid",
    "dllcnx/vue-document-ace",
    "dllcnx/ng-scroll",
    "fxmontigny/ng2-ace-editor",
    "ajaxorg/ace",
    "cipchk/ngx-umeditor",
    "cipchk/ngx-ueditor",
    "bogdan1975/ng2-slider-component",
    "dolanmiu/ng-color",
    "marcinmichalik/ng-scrollto",
    "anasash/ngx-scroll-event",
    "sachinchoolur/ladda-angular",
    "zak-c/ngx-loading",
    "maxisam/ngx-clipboard",
    "zenorocha/clipboard.js",
    "alexgibson/shake.js",
    "jackmoore/autosize",
    "guo-weijie/win11_vue",
}

FW_REPOS = {
    "react/react": ("fw", "fw-react"),
    "vercel/next.js": ("fw", "fw-react"),
    "jaredpalmer/razzle": ("fw", "fw-react"),
    "timarney/react-app-rewired": ("tooling", "tool-build"),
    "sveltejs/svelte": ("fw", "fw-svelte"),
    "sveltejs/kit": ("fw", "fw-svelte"),
    "solidjs/solid": ("fw", "fw-svelte"),
    "emberjs/ember.js": ("fw", "fw-svelte"),
    "tencent/omi": ("fw", "fw-svelte"),
    "angular/angular": ("fw", "fw-angular"),
    "angular/angular-cli": ("fw", "fw-angular"),
    "nuxt/nuxt": ("fw", "fw-vue"),
    "axios/axios": ("fw", "fw-util"),
    "zloirock/core-js": ("fw", "fw-util"),
    "caolan/async": ("fw", "fw-util"),
    "nextapps-de/flexsearch": ("fw", "fw-util"),
    "nanostores/nanostores": ("fw", "fw-util"),
    "sodiray/radash": ("fw", "fw-util"),
    "ramda/ramda": ("fw", "fw-util"),
    "developit/mitt": ("fw", "fw-util"),
    "brix/crypto-js": ("fw", "fw-util"),
    "localforage/localforage": ("fw", "fw-util"),
    "moment/moment": ("fw", "fw-util"),
    "iamkun/dayjs": ("fw", "fw-util"),
    "chalk/chalk": ("fw", "fw-util"),
    "nodejs/node": ("tooling", "tool-build"),
    "oven-sh/bun": ("tooling", "tool-build"),
    "handlebars-lang/handlebars.js": ("fw", "fw-util"),
    "mde/ejs": ("fw", "fw-util"),
    "markedjs/marked": ("fw", "fw-util"),
    "showdownjs/showdown": ("fw", "fw-util"),
    "jonschlinkert/gray-matter": ("fw", "fw-util"),
    "eemeli/yaml": ("fw", "fw-util"),
    "nodeca/js-yaml": ("fw", "fw-util"),
    "jeremyfa/yaml.js": ("fw", "fw-util"),
    "dankogai/js-base64": ("fw", "fw-util"),
    "zh-lx/pinyin-pro": ("fw", "fw-util"),
    "xinglie/pinyin": ("fw", "fw-util"),
    "auth0/jwt-decode": ("fw", "fw-util"),
    "auth0/angular2-jwt": ("fw", "fw-angular"),
    "storeon/storeon": ("fw", "fw-util"),
    "italypaleale/svelte-spa-router": ("fw", "fw-svelte"),
    "emiltholin/svelte-routing": ("fw", "fw-svelte"),
    "svelte-society/sveltesociety.dev": ("fw", "fw-svelte"),
    "vuejs/devtools-v6": ("tooling", "tool-cli"),
    "mqttjs/mqtt.js": ("fw", "fw-util"),
    "sockjs/sockjs-client": ("fw", "fw-util"),
    "socketio/engine.io-client": ("fw", "fw-util"),
    "rodgc/ngx-socket-io": ("fw", "fw-angular"),
    "eligrey/filesaver.js": ("fw", "fw-util"),
    "mailru/fileapi": ("fw", "fw-util"),
    "sheetjs/sheetjs": ("fw", "fw-util"),
    "zzzhan/js-shortid": ("fw", "fw-util"),
    "alibaba/handyjson": ("fw", "fw-util"),
}

TOOL_REPOS = {
    "microsoft/playwright": ("tooling", "tool-quality"),
    "antfu-collective/vite-plugin-inspect": ("tooling", "tool-build"),
    "webpack/webpack": ("tooling", "tool-build"),
    "vitejs/vite": ("tooling", "tool-build"),
    "typicode/husky": ("tooling", "tool-quality"),
    "streamich/git-cz": ("tooling", "tool-quality"),
    "commitizen/cz-cli": ("tooling", "tool-quality"),
    "obkoro1/koro1fileheader": ("tooling", "tool-cli"),
    "biomejs/biome": ("tooling", "tool-quality"),
    "rome/tools": ("tooling", "tool-quality"),
    "volta-cli/volta": ("tooling", "tool-build"),
    "nodejs/corepack": ("tooling", "tool-build"),
    "release-it/release-it": ("tooling", "tool-quality"),
    "joeshutt/version-polling": ("tooling", "tool-cli"),
    "jenv/jenv": ("tooling", "tool-cli"),
    "ringotangs/jenv": ("tooling", "tool-cli"),
    "tj/n": ("tooling", "tool-build"),
    "nvm-sh/nvm": ("tooling", "tool-build"),
    "nvm-windows/nvm": ("tooling", "tool-build"),
    "yarnpkg/berry": ("tooling", "tool-build"),
    "yarnpkg/yarn": ("tooling", "tool-build"),
    "pana/nrm": ("tooling", "tool-build"),
    "pnpm/pnpm": ("tooling", "tool-build"),
    "npm/cli": ("tooling", "tool-build"),
    "lerna/lerna": ("tooling", "tool-build"),
    "rollup/rollup": ("tooling", "tool-build"),
    "rollup/plugins": ("tooling", "tool-build"),
    "terser/terser": ("tooling", "tool-build"),
    "mishoo/uglifyjs": ("tooling", "tool-build"),
    "yui/yuicompressor": ("tooling", "tool-build"),
    "egoist/rollup-plugin-postcss": ("tooling", "tool-build"),
    "jackfranklin/rollup-plugin-markdown": ("tooling", "tool-build"),
    "johnagan/clean-webpack-plugin": ("tooling", "tool-build"),
    "webpack/minimizer-webpack-plugin": ("tooling", "tool-build"),
    "shellscape/webpack-plugin-serve": ("tooling", "tool-build"),
    "postcss/postcss": ("tooling", "tool-build"),
    "cypress-io/cypress": ("tooling", "tool-quality"),
    "puppeteer/puppeteer": ("tooling", "tool-quality"),
    "google/zx": ("tooling", "tool-cli"),
    "antfu-collective/ni": ("tooling", "tool-build"),
    "lukechilds/zsh-better-npm-completion": ("tooling", "tool-cli"),
    "chrisands/zsh-yarn-completions": ("tooling", "tool-cli"),
    "jasongin/nvs": ("tooling", "tool-build"),
    "wbyoung/avn": ("tooling", "tool-build"),
    "gucong3000/mirror-config-china": ("tooling", "tool-build"),
    "cnpm/cnpmjs.org": ("tooling", "tool-build"),
    "verdaccio/verdaccio": ("tooling", "tool-build"),
    "dylang/npm-check": ("tooling", "tool-quality"),
    "th0r/npm-upgrade": ("tooling", "tool-quality"),
    "ng-packagr/ng-packagr": ("tooling", "tool-build"),
    "mgechev/codelyzer": ("tooling", "tool-quality"),
    "rich-harris/degit": ("tooling", "tool-cli"),
    "sveltejs/svelte-preprocess": ("tooling", "tool-build"),
    "nklayman/vue-cli-plugin-electron-builder": ("mobile", "mobile-native"),
    "dllcnx/auto-deploy": ("tooling", "tool-cli"),
    "bgwd666/deploy": ("tooling", "tool-cli"),
    "steelbrain/node-ssh": ("tooling", "tool-cli"),
    "tschaub/gh-pages": ("tooling", "tool-cli"),
    "staven630/vue-cli4-config": ("tooling", "tool-build"),
    "remy/nodemon": ("tooling", "tool-cli"),
    "nodejs/node-gyp": ("tooling", "tool-build"),
    "ops-gaurav/es6-scaffolder": ("tooling", "tool-cli"),
    "react-webpack-generators/generator-react-webpack": ("tooling", "tool-cli"),
    "ant-design/antd-init": ("tooling", "tool-cli"),
    "i5ting/koa-generator": ("tooling", "tool-cli"),
    "dllcnx/vue-category-pages": ("tooling", "tool-build"),
    "seizedev/vue-more-pages": ("tooling", "tool-build"),
    "dllcnx/sapper-template-saas": ("tooling", "tool-cli"),
    "minimistjs/minimist": ("tooling", "tool-cli"),
    "sboudrias/inquirer.js": ("tooling", "tool-cli"),
    "fluent-ffmpeg/node-fluent-ffmpeg": ("tooling", "tool-cli"),
    "lovell/sharp": ("tooling", "tool-cli"),
    "winstonjs/winston": ("tooling", "tool-cli"),
    "winstonjs/winston-daily-rotate-file": ("tooling", "tool-cli"),
    "simonh1000/ftp-deploy": ("tooling", "tool-cli"),
    "alibaba/anyproxy": ("tooling", "tool-cli"),
    "http-party/node-http-proxy": ("tooling", "tool-cli"),
    "chimurai/http-proxy-middleware": ("tooling", "tool-cli"),
    "kong/insomnia": ("tooling", "tool-cli"),
    "apidoc/apidoc": ("tooling", "tool-cli"),
    "jgm/pandoc": ("tooling", "tool-cli"),
    "nuysoft/mock": ("tooling", "tool-quality"),
    "easy-mock/easy-mock": ("tooling", "tool-quality"),
    "smollweide/node-mock-server": ("tooling", "tool-quality"),
    "smollweide/dash4": ("tooling", "tool-cli"),
    "vercel/serve": ("tooling", "tool-cli"),
    "lukeed/sirv": ("tooling", "tool-cli"),
    "openresty/lua-nginx-module": ("tooling", "tool-cli"),
    "cujojs/curl": ("tooling", "tool-cli"),
    "dllcnx/iframEventBus": ("tooling", "tool-cli"),
}

BACKEND_REPOS = {
    "yunaiV/ruoyi-vue-pro": ("backend", "be-full"),
    "prisma/orm": ("backend", "be-node"),
    "senecajs/seneca": ("backend", "be-node"),
    "trpc/trpc": ("backend", "be-node"),
    "fastify/fastify": ("backend", "be-node"),
    "nestjs/nest": ("backend", "be-node"),
    "eggjs/egg": ("backend", "be-node"),
    "sequelize/sequelize": ("backend", "be-node"),
    "sequelize/sequelize-auto": ("backend", "be-node"),
    "automattic/mongoose": ("backend", "be-node"),
    "moleculerjs/moleculer": ("backend", "be-node"),
    "lukeed/polka": ("backend", "be-node"),
    "node-schedule/node-schedule": ("backend", "be-node"),
    "expressjs/compression": ("backend", "be-node"),
    "reactivex/rxjava": ("backend", "be-java"),
    "siegmar/fastcsv": ("backend", "be-java"),
    "osiegmar/fastcsv": ("backend", "be-java"),
    "haracejacob/sequelize-use-cache": ("backend", "be-node"),
    "senecajs/seneca-postgres-store": ("backend", "be-node"),
    "yangzongzhuan/ruoyi-vue3": ("backend", "be-full"),
}

TEMPLATE_REPOS = {
    "panjiachen/vue-element-admin": ("template", "tpl-admin"),
    "zxwk1998/vue-admin-better": ("template", "tpl-admin"),
    "lin-xin/vue-manage-system": ("template", "tpl-admin"),
    "akveo/ngx-admin": ("template", "tpl-admin"),
    "ng-alain/ng-alain": ("template", "tpl-admin"),
    "surmon-china/surmon.me.admin": ("template", "tpl-admin"),
    "surmon-china/angular-admin": ("template", "tpl-admin"),
    "myopenresources/cc": ("template", "tpl-admin"),
    "linweiwei123/hotshots-admin-angular2": ("template", "tpl-admin"),
    "neveryu/official-website": ("template", "tpl-site"),
    "realworld-apps/realworld": ("template", "tpl-site"),
    "lucperkins/bulma-dashboard": ("template", "tpl-admin"),
    "mimecorg/vuido": ("mobile", "mobile-native"),
    "electron/electron": ("mobile", "mobile-native"),
}

# High-frequency cores to pin at the top of README
PINNED = [
    "react/react",
    "vercel/next.js",
    "sveltejs/svelte",
    "angular/angular",
    "nuxt/nuxt",
    "vitejs/vite",
    "webpack/webpack",
    "nodejs/node",
    "cesiumgs/cesium",
    "apache/echarts",
    "mrdoob/three.js",
    "element-plus/element-plus",
    "nestjs/nest",
    "openclaw/openclaw",
    "xtls/xray-core",
]

# Explicit overrides (checked first). Use to fix leftovers and cross-bucket moves.
OVERRIDE = {
    "preactjs/preact": ("fw", "fw-svelte"),
    "kelektiv/node.bcrypt.js": ("backend", "be-node"),
    "openharmony/docs": ("learn", "learn-frontend"),
    "dom-bro/es6-dessert": ("demo", "demo-web"),
    "dllcnx/css3-anime": ("demo", "demo-web"),
    "guo-weijie/win11_vue": ("demo", "demo-web"),
    "codyhouse/3d-rotating-navigation": ("demo", "demo-web"),
    "codyhouse/3d-bold-navigation": ("demo", "demo-web"),
    "yuri2peter/win10-ui": ("demo", "demo-web"),
    "moontechlab/lunatv": ("selfhost", "selfhost-media"),
    "hectorqin/reader": ("selfhost", "selfhost-media"),
    "lowlighter/metrics": ("tooling", "tool-cli"),
    "wechatsync/wechatsync": ("selfhost", "selfhost-desktop"),
    "johncoates/aerial": ("selfhost", "selfhost-desktop"),
    "picgo/picgo-core": ("selfhost", "selfhost-desktop"),
    "molunerfinn/picgo": ("selfhost", "selfhost-desktop"),
    "corentinth/it-tools": ("selfhost", "selfhost-desktop"),
    "zhaoolee/chromeappheroes": ("learn", "learn-awesome"),
    "supermarin/powerline-fonts": ("selfhost", "selfhost-desktop"),
    "krahets/hello-algo": ("learn", "learn-interview"),
    "cyc2018/cs-notes": ("learn", "learn-interview"),
    "yangshun/tech-interview-handbook": ("learn", "learn-interview"),
    "chalarangelo/30-seconds-of-code": ("learn", "learn-frontend"),
    "mimecorg/vuido": ("mobile", "mobile-native"),
    "electron/electron": ("mobile", "mobile-native"),
    "yunaiv/ruoyi-vue-pro": ("backend", "be-full"),
    "yangzongzhuan/ruoyi-vue3": ("backend", "be-full"),
}


def _lk(obj):
    if isinstance(obj, set):
        return {x.lower() for x in obj}
    return {k.lower(): v for k, v in obj.items()}


AI_REPOS = _lk(AI_REPOS)
GIS_REPOS = _lk(GIS_REPOS)
PROXY_REPOS = _lk(PROXY_REPOS)
LEARN_REPOS = _lk(LEARN_REPOS)
SSG_REPOS = _lk(SSG_REPOS)
SELFHOST_REPOS = _lk(SELFHOST_REPOS)
MOBILE_REPOS = _lk(MOBILE_REPOS)
UI_REPOS = _lk(UI_REPOS)
FW_REPOS = _lk(FW_REPOS)
TOOL_REPOS = _lk(TOOL_REPOS)
BACKEND_REPOS = _lk(BACKEND_REPOS)
TEMPLATE_REPOS = _lk(TEMPLATE_REPOS)
OVERRIDE = _lk(OVERRIDE)
PINNED = [p.lower() for p in PINNED]


def classify(repo: dict) -> tuple[str, str]:
    b = _blob(repo)
    full = b["full"]
    text = b["text"]
    topics = b["topics"]

    if full in OVERRIDE:
        return OVERRIDE[full]
    if full in AI_REPOS:
        return _ai_sub(b)
    if full in GIS_REPOS:
        return _gis_sub(b)
    if full in PROXY_REPOS:
        return _proxy_sub(b)
    if full in LEARN_REPOS:
        return _learn_sub(b)
    if full in SSG_REPOS:
        return _ssg_sub(b)
    if full in SELFHOST_REPOS:
        return _selfhost_sub(b)
    if full in MOBILE_REPOS:
        return _mobile_sub(b)
    if full in UI_REPOS:
        return _ui_sub(b)
    if full in FW_REPOS:
        return FW_REPOS[full]
    if full in TOOL_REPOS:
        return TOOL_REPOS[full]
    if full in BACKEND_REPOS:
        return BACKEND_REPOS[full]
    if full in TEMPLATE_REPOS:
        return TEMPLATE_REPOS[full]

    # --- heuristic fallback ---
    if _topic(b, ("ai", "llm", "claude", "chatgpt", "openai", "gpt", "agent-skills", "mcp", "generative-ai")) or _has(
        f"{b['full']} {' '.join(b['topics'])}",
        ("claude-code", "openclaw", "llm", "chatgpt", "openai", "agent-skill", "prompt-optimizer"),
    ):
        return _ai_sub(b)

    if _topic(b, ("cesium", "gis", "mapbox", "geospatial", "webgl")) or _has(
        text,
        (
            "cesium",
            "mapbox",
            "geospatial",
            "geojson",
            "3dtiles",
            "3d-tiles",
            "turf",
            "gdal",
            "proj4",
            "czml",
            "maplibre",
            "deck.gl",
            "测绘",
            "三维地球",
            "矢量瓦片",
            "风场",
        ),
    ):
        if any(k in text for k in ("cesium", "mapbox", "gis", "geo", "maplibre", "gdal", "turf", "proj4", "czml", "3dtile", "测绘")):
            return _gis_sub(b)

    if _topic(b, ("v2ray", "xray", "clash", "trojan", "shadowsocks", "vpn", "gfw")) or _has(
        text,
        (
            "v2ray",
            "xray-core",
            "clash",
            "mihomo",
            "trojan",
            "shadowsocks",
            "科学上网",
            "翻墙",
            "机场",
            "gfw",
            "hysteria",
            "sing-box",
            "v2rayn",
            "v2rayng",
        ),
    ):
        return _proxy_sub(b)

    if _topic(b, ("interview", "leetcode", "algorithm", "algorithms", "awesome-list", "tutorial")) or _has(
        text,
        ("面试", "leetcode", "algorithm", "awesome list", "roadmap", "教程", "best practices", "interview"),
    ):
        if any(
            k in text
            for k in (
                "面试",
                "leetcode",
                "algorithm",
                "awesome",
                "roadmap",
                "interview",
                "tutorial",
                "handbook",
                "30-days",
                "30 days",
                "you-dont-know",
                "best practice",
            )
        ):
            return _learn_sub(b)

    if _has(
        text,
        (
            "hexo",
            "hugo",
            "jekyll",
            "vuepress",
            "vitepress",
            "docsify",
            "static site",
            "static-site",
            "blog theme",
            "blog-engine",
            "typecho",
            "halo-theme",
            "leanote",
            "gitbook",
        ),
    ) or _topic(b, ("hexo", "hugo", "jekyll", "vuepress", "static-site-generator", "blog")):
        if not _has(text, ("gatsby is",)):
            return _ssg_sub(b)

    if _topic(b, ("self-hosted", "docker", "nas")) or _has(
        text,
        (
            "self-hosted",
            "self hosted",
            "jellyfin",
            "alist",
            "casaos",
            "bitwarden",
            "nextcloud",
            "onlyoffice",
            "qbittorrent",
            "navidrome",
            "gitea",
            "media server",
            "网盘",
            "阅读3",
        ),
    ):
        return _selfhost_sub(b)

    if _has(
        text,
        (
            "react native",
            "react-native",
            "cordova",
            "phonegap",
            "flutter",
            "taro",
            "uni-app",
            "uniapp",
            "小程序",
            "wechat",
            "miniprogram",
            "ionic",
            "capacitor",
        ),
    ) or _topic(b, ("android", "ios", "flutter", "react-native", "cordova", "miniprogram", "wechat")):
        if b["lang"] in {"java", "kotlin", "dart", "swift", "objective-c"} or _has(
            text, ("android", "cordova", "flutter", "react-native", "小程序", "taro", "ionic")
        ):
            return _mobile_sub(b)

    if _has(
        text,
        (
            "ui library",
            "component library",
            "component-library",
            "design system",
            "chart",
            "echarts",
            "animation",
            "drag-and-drop",
            "drag and drop",
            "canvas",
            "webgl",
            "markdown editor",
            "rich text",
            "color picker",
            "toast",
            "datepicker",
            "scrollbar",
            "swiper",
            "carousel",
        ),
    ) or _topic(
        b,
        (
            "ui",
            "components",
            "animation",
            "drag-and-drop",
            "charts",
            "webgl",
            "canvas",
            "material-design",
        ),
    ):
        if any(
            k in text
            for k in (
                "component",
                "ui kit",
                "ui library",
                "chart",
                "echarts",
                "animation",
                "drag",
                "dnd",
                "canvas",
                "webgl",
                "editor",
                "toast",
                "color picker",
                "swiper",
                "antd",
                "element",
                "vuetify",
            )
        ):
            return _ui_sub(b)

    if _has(
        text,
        (
            "webpack",
            "vite",
            "rollup",
            "esbuild",
            "parcel",
            "babel",
            "eslint",
            "prettier",
            "linter",
            "bundler",
            "package manager",
            "npm",
            "pnpm",
            "yarn",
            "monorepo",
            "scaffold",
            "yeoman",
        ),
    ) or _topic(b, ("webpack", "vite", "eslint", "cli", "bundler", "npm")):
        if any(
            k in text
            for k in (
                "webpack",
                "vite ",
                "vite.",
                "rollup",
                "esbuild",
                "eslint",
                "bundler",
                "package manager",
                "scaffold",
                "cli",
                "npm",
                "pnpm",
                "yarn",
            )
        ):
            return _tool_sub(b)

    if _has(
        text,
        (
            "express",
            "koa",
            "fastify",
            "nestjs",
            "spring boot",
            "spring-boot",
            "orm",
            "mongodb",
            "mysql",
            "postgres",
            "microservice",
            "graphql",
        ),
    ) or _topic(b, ("nodejs", "java", "mysql", "mongodb")):
        if any(
            k in text
            for k in (
                "server",
                "backend",
                "orm",
                "database",
                "microservice",
                "nestjs",
                "express",
                "koa",
                "spring",
                "graphql",
                "mongodb",
                "mysql",
            )
        ):
            return _backend_sub(b)

    if _has(text, ("admin", "dashboard", "后台管理", "boilerplate", "starter", "template")):
        if any(k in text for k in ("admin", "dashboard", "后台", "boilerplate", "starter template")):
            return _template_sub(b)

    if _has(text, ("vue", "react", "angular", "svelte", "next.js", "nuxt")):
        return _fw_sub(b)

    if _has(text, ("demo", "example", "示例", "案例", "playground")):
        return ("demo", "demo-web")

    return ("other", "other-misc")


def _ai_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if _has(t, ("skill", "agent", "claude", "openclaw", "hermes", "codex", "mcp", "智能体")):
        return ("ai", "ai-agent")
    if _has(t, ("model", "gguf", "inference", "gateway", "diffusion", "super-resolution", "inpaint", "grok", "deepseek", "comfy")):
        return ("ai", "ai-model")
    return ("ai", "ai-app")


def _gis_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if "cesium" in t or "3dtile" in t or "czml" in t or "three" in t and "earth" in t:
        return ("gis", "gis-cesium")
    if _has(t, ("mapbox", "maplibre", "deck.gl", "turf", "leaflet", "openlayers")):
        return ("gis", "gis-map")
    return ("gis", "gis-data")


def _proxy_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if _has(t, ("openwrt", "软路由", "istoreos", "kwrt", "cloudflare", "speedtest", "luci")):
        return ("proxy", "proxy-router")
    if _has(t, ("rule", "订阅", "subscribe", "subconverter", "script", "onekey", "一键", "机场")):
        return ("proxy", "proxy-rule")
    return ("proxy", "proxy-core")


def _learn_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if _has(t, ("面试", "interview", "leetcode", "algorithm", "algo", "cs-notes", "计算机基础", "数据结构")):
        return ("learn", "learn-interview")
    if _has(t, ("awesome", "book", "书单", "hellogithub", "howtocook", "gold-miner", "资源汇总")):
        return ("learn", "learn-awesome")
    return ("learn", "learn-frontend")


def _ssg_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if _has(t, ("theme", "主题", "gitalk", "giscus", "twikoo", "comment", "live2d", "plugin")):
        return ("ssg", "ssg-theme")
    return ("ssg", "ssg-engine")


def _selfhost_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if _has(t, ("music", "video", "tvbox", "lunatv", "jellyfin", "qbittorrent", "alist", "阅读", "legado", "ffmpeg", "obs", "iina", "navidrome", "torrent", "tracker")):
        return ("selfhost", "selfhost-media")
    if _has(t, ("note", "cms", "wiki", "memo", "obsidian", "strapi", "halo", "知识")):
        return ("selfhost", "selfhost-note")
    if _has(t, ("macos", "windows", "desktop", "electron", "terminal", "zsh", "ohmyzsh", "browser", "ventoy", "activation")):
        return ("selfhost", "selfhost-desktop")
    return ("selfhost", "selfhost-ops")


def _mobile_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if _has(t, ("小程序", "taro", "uni-app", "miniprogram", "wechat", "ionic", "nutui", "vant", "vux", "cube-ui")):
        return ("mobile", "mobile-mini")
    return ("mobile", "mobile-native")


def _ui_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    name = b["repo"]
    if name.startswith(("ngx-", "ng2-", "ng-", "angular")) or "angular" in t and _has(
        t, ("ngx", "ng2", "ng-", "directive", "component")
    ):
        if "admin" not in t:
            return ("ui", "ui-angular")
    if _has(t, ("chart", "echarts", "datav", "visualization", "plotly", "highcharts", "d3", "x6", "bpmn")):
        return ("ui", "ui-chart")
    if _has(t, ("editor", "markdown", "ace", "quill", "wangeditor", "fabric", "canvas", "pdf", "json-editor")):
        return ("ui", "ui-editor")
    if _has(t, ("animat", "drag", "dnd", "sortable", "swiper", "three.js", "webgl", "lottie", "aos", "fullpage", "spinner", "toast")):
        return ("ui", "ui-motion")
    return ("ui", "ui-lib")


def _fw_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if "angular" in t:
        return ("fw", "fw-angular")
    if "svelte" in t or "solid" in t or "ember" in t:
        return ("fw", "fw-svelte")
    if "react" in t or "next.js" in t or "nextjs" in t:
        return ("fw", "fw-react")
    if "vue" in t or "nuxt" in t:
        return ("fw", "fw-vue")
    return ("fw", "fw-util")


def _tool_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if _has(t, ("test", "lint", "eslint", "cypress", "playwright", "husky", "commit", "prettier", "mock")):
        return ("tooling", "tool-quality")
    if _has(t, ("webpack", "vite", "rollup", "bundl", "pnpm", "yarn", "npm", "package")):
        return ("tooling", "tool-build")
    return ("tooling", "tool-cli")


def _backend_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if _has(t, ("java", "spring", "rxjava")):
        return ("backend", "be-java")
    if _has(t, ("admin", "ruoyi", "全栈", "low-code", "lowcode")):
        return ("backend", "be-full")
    return ("backend", "be-node")


def _template_sub(b: dict) -> tuple[str, str]:
    t = b["text"]
    if "admin" in t or "后台" in t or "dashboard" in t:
        return ("template", "tpl-admin")
    return ("template", "tpl-site")

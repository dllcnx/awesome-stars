#!/usr/bin/env python3
"""Generate README.md from starred repos + taxonomy."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from classify import CATEGORIES, PINNED, classify  # noqa: E402

USER = "dllcnx"
DEFAULT_STARS = ROOT / "data" / "stars.json"


def format_stars(n: int | None) -> str:
    if not n:
        return "0"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}m".replace(".0m", "m")
    if n >= 1_000:
        v = n / 1_000
        return f"{v:.1f}k".replace(".0k", "k")
    return str(n)


def fetch_stars(user: str) -> list[dict]:
    url = f"https://api.github.com/users/{user}/starred?per_page=100"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "dllcnx-awesome-stars",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    repos: list[dict] = []
    while url:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            page = json.loads(resp.read().decode())
            for r in page:
                repos.append(
                    {
                        "full_name": r["full_name"],
                        "html_url": r.get("html_url"),
                        "description": r.get("description"),
                        "language": r.get("language"),
                        "stargazers_count": r.get("stargazers_count"),
                        "topics": r.get("topics") or [],
                        "fork": r.get("fork"),
                        "archived": r.get("archived"),
                        "homepage": r.get("homepage"),
                        "created_at": r.get("created_at"),
                        "updated_at": r.get("updated_at"),
                        "pushed_at": r.get("pushed_at"),
                        "license": (r.get("license") or {}).get("spdx_id") if isinstance(r.get("license"), dict) else r.get("license"),
                    }
                )
            link = resp.headers.get("Link") or ""
            nxt = re.search(r'<([^>]+)>;\s*rel="next"', link)
            url = nxt.group(1) if nxt else ""
    return repos


def load_stars(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("repos") or data.get("items") or []
    return data


def bucket(repos: list[dict]) -> dict[str, dict[str, list[dict]]]:
    grouped: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for repo in repos:
        cat, sub = classify(repo)
        repo["_cat"] = cat
        repo["_sub"] = sub
        grouped[cat][sub].append(repo)
    for cat in grouped:
        for sub in grouped[cat]:
            grouped[cat][sub].sort(key=lambda r: (-(r.get("stargazers_count") or 0), r["full_name"].lower()))
    return grouped


def render_item(repo: dict) -> str:
    name = repo["full_name"]
    url = repo.get("html_url") or f"https://github.com/{name}"
    desc = (repo.get("description") or "").replace("\n", " ").strip()
    if len(desc) > 140:
        desc = desc[:137] + "…"
    if not desc:
        desc = "暂无简介"
    lang = repo.get("language") or "—"
    stars = format_stars(repo.get("stargazers_count") or 0)
    return f"- [{name}]({url}) — {desc} `{lang}` ★{stars}"


def toc_anchor(title: str) -> str:
    # GitHub heading slug: lowercase, spaces to -, strip most punctuation but keep CJK
    slug = title.lower()
    out = []
    for ch in slug:
        if ch.isalnum() or "\u4e00" <= ch <= "\u9fff":
            out.append(ch)
        elif ch in " -_":
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def build_readme(repos: list[dict], grouped: dict, generated_at: str) -> str:
    n = len(repos)
    langs = defaultdict(int)
    for r in repos:
        langs[r.get("language") or "未知"] += 1
    lang_line = " · ".join(f"{k} {v}" for k, v in sorted(langs.items(), key=lambda x: -x[1])[:8])

    lines: list[str] = []
    lines.append("# Awesome Stars")
    lines.append("")
    lines.append(f"> [@dllcnx](https://github.com/{USER}) 的 GitHub 星标索引 · 按主题互斥分类 · 共 **{n}** 个项目")
    lines.append(">")
    lines.append(f"> 生成时间：{generated_at} · 语言分布：{lang_line}")
    lines.append("")
    lines.append("原先用 GitHub Lists 分成 14 类，边界重叠比较明显：`⭐️前端`（113）和 `优秀案例与 DEMO`（103）几乎把组件库、框架、案例混在一起；Cesium 地理项目散落在前端里；新加星的 AI 仓库也没有全部进 AI 列表。这份索引按**主题优先、一条项目只进一类**重新整理，并保留和旧 List 的对应关系，方便你之后改 GitHub Lists。")
    lines.append("")
    lines.append("## 目录")
    lines.append("")
    for cat in CATEGORIES:
        count = sum(len(grouped.get(cat["id"], {}).get(sid, [])) for sid, _ in cat["subs"])
        if count == 0:
            continue
        heading = f"{cat['emoji']} {cat['title']}"
        lines.append(f"- [{heading}](#{toc_anchor(heading)}) — {count}")
        for sid, stitle in cat["subs"]:
            scount = len(grouped.get(cat["id"], {}).get(sid, []))
            if scount:
                lines.append(f"  - [{stitle}](#{toc_anchor(stitle)}) — {scount}")
    lines.append("")

    # pinned
    by_name = {r["full_name"].lower(): r for r in repos}
    pinned_hits = [by_name[p] for p in PINNED if p in by_name]
    if pinned_hits:
        lines.append("## 常用核心速览")
        lines.append("")
        lines.append("从星标里抽出的高频底座，方便日常翻找。完整分类见下方。")
        lines.append("")
        for r in pinned_hits:
            lines.append(render_item(r))
        lines.append("")

    lines.append("## 和旧 GitHub Lists 的对应")
    lines.append("")
    lines.append("| 原 List | 数量 | 主要问题 | 新去向 |")
    lines.append("|---|---:|---|---|")
    lines.append("| ⭐️⭐️⭐️⭐️⭐️AI | 22 | 新星标没及时归档 | AI 与智能体 |")
    lines.append("| ⭐️前端 | 113 | 框架、组件、GIS、跨端混在一起 | 前端框架 / UI / 跨端 / GIS |")
    lines.append("| 优秀案例与 DEMO | 103 | 很多其实是库，不是案例 | 按主题拆走，Demo 只留真正的例子 |")
    lines.append("| ⭐️开发 | 71 | 和前端、工程化重叠 | 后端与全栈 / 工程化 |")
    lines.append("| 软件与服务 | 70 | 范围偏大 | 自托管软件与系统工具 |")
    lines.append("| 学习资料 | 64 | 结构清楚，基本保留 | 学习资料、面试与 Awesome |")
    lines.append("| ⭐️专业领域 | 44 | Cesium 案例没进来 | 测绘地理与三维可视化 |")
    lines.append("| 开发辅助 | 42 | 和前端工具链重叠 | 工程化与开发工具 |")
    lines.append("| 科学网络与路由 | 35 | 结构清楚，基本保留 | 网络代理与路由 |")
    lines.append("| 静态站点与文档构建 | 25 | 结构清楚，基本保留 | 静态站点、博客与文档 |")
    lines.append("| 镜像 | 17 | 和包管理/镜像源混用 | 工程化（包管理） |")
    lines.append("| ⭐️常用 | 10 | 和前端/框架重复 | 文首「常用核心速览」 |")
    lines.append("| 模版社区与解决方案 | 10 | 太窄 | 模板、后台与解决方案 |")
    lines.append("| 其它 | 5 | 兜底 | 其它（尽量压缩） |")
    lines.append("")
    lines.append("GitHub Lists 无法用当前仓库权限改写。你可以按上表在 [Stars Lists](https://github.com/stars/dllcnx/lists) 里手动对齐，或只把本 README 当索引。")
    lines.append("")

    for cat in CATEGORIES:
        cat_id = cat["id"]
        buckets = grouped.get(cat_id, {})
        total = sum(len(v) for v in buckets.values())
        if total == 0:
            continue
        lines.append(f"## {cat['emoji']} {cat['title']}")
        lines.append("")
        lines.append(f"{cat['blurb']} **{total}** 个项目。")
        lines.append("")
        for sid, stitle in cat["subs"]:
            items = buckets.get(sid) or []
            if not items:
                continue
            lines.append(f"### {stitle}")
            lines.append("")
            for repo in items:
                lines.append(render_item(repo))
            lines.append("")

    # language appendix (counts only — full list is in the topic sections)
    lines.append("## 按语言统计")
    lines.append("")
    lines.append("| 语言 | 数量 |")
    lines.append("|---|---:|")
    lang_map: dict[str, int] = defaultdict(int)
    for r in repos:
        lang_map[r.get("language") or "未知"] += 1
    for lang, count in sorted(lang_map.items(), key=lambda x: (-x[1], x[0].lower())):
        lines.append(f"| {lang} | {count} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("重新生成：`python3 scripts/generate.py`。从 GitHub 拉取公开星标：`python3 scripts/generate.py --fetch`。")
    lines.append("")
    return "\n".join(lines)


def stats(grouped: dict, repos: list[dict]) -> str:
    lines = ["# classification stats", f"total={len(repos)}"]
    other = []
    for cat in CATEGORIES:
        buckets = grouped.get(cat["id"], {})
        total = sum(len(v) for v in buckets.values())
        lines.append(f"{cat['id']:10} {total:4d}  {cat['title']}")
        for sid, title in cat["subs"]:
            items = buckets.get(sid) or []
            if items:
                lines.append(f"           {len(items):4d}  {sid} / {title}")
                if cat["id"] == "other":
                    other.extend(items)
    if other:
        lines.append("\n[other]")
        for r in other:
            lines.append(f"  {r['full_name']} | {r.get('language')} | {(r.get('description') or '')[:80]}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stars", type=Path, default=DEFAULT_STARS)
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    parser.add_argument("--classified", type=Path, default=ROOT / "data" / "classified.json")
    parser.add_argument("--fetch", action="store_true", help="Refresh starred repos from GitHub before generating")
    args = parser.parse_args()

    if args.fetch:
        repos = fetch_stars(USER)
        args.stars.parent.mkdir(parents=True, exist_ok=True)
        args.stars.write_text(json.dumps(repos, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"fetched {len(repos)} starred repos")
    else:
        repos = load_stars(args.stars)
    grouped = bucket(repos)
    generated_at = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    args.readme.write_text(build_readme(repos, grouped, generated_at), encoding="utf-8")

    payload = []
    for r in repos:
        payload.append(
            {
                "full_name": r["full_name"],
                "category": r["_cat"],
                "subcategory": r["_sub"],
                "language": r.get("language"),
                "stars": r.get("stargazers_count"),
                "description": r.get("description"),
                "html_url": r.get("html_url"),
            }
        )
    args.classified.parent.mkdir(parents=True, exist_ok=True)
    args.classified.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(stats(grouped, repos))
    print(f"wrote {args.readme} ({args.readme.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

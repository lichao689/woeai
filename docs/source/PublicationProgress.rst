:orphan:

论文制作进度
============

.. raw:: html

   <div id="publication-board" data-source="_static/publication-board-data.json">
     <div id="board-summary" class="board-summary" aria-label="全部论文概览"></div>
     <div class="board-toolbar">
     <div class="board-tracks" role="group" aria-label="选择状态筛选渠道">
       <button type="button" data-board-track="rtd" aria-pressed="true" disabled>按 RTD 筛选</button>
       <button type="button" data-board-track="wechat" aria-pressed="false" disabled>按公众号筛选</button>
     </div>
     <details class="board-help">
       <summary>状态与筛选说明</summary>
     <p class="board-intro">RTD 全文精解与公众号，独立记录、只读查看。制作与状态维护由助手完成。</p>
     <p class="board-explainer">未登记不等于未开始；历史导读不等于全文核验；草稿不等于发布。每行一篇论文，两条渠道状态同时显示；状态筛选与“仅看未完成”按所选渠道计算。</p>
     </details>
     </div>
     <form id="board-filters" class="board-filters" aria-label="筛选论文">
       <label class="board-search">搜索论文<input name="query" type="search" placeholder="题名 / DOI" disabled></label>
       <label>发表年份<select name="year" disabled><option value="">全部年份</option></select></label>
       <label>研究方向<select name="direction" disabled><option value="">全部方向</option></select></label>
       <label>当前渠道状态<select name="status" disabled><option value="">全部状态</option></select></label>
       <label class="board-checkbox"><input name="unfinished" type="checkbox" disabled>仅看未完成</label>
       <button type="button" id="board-reset" disabled>重置筛选</button>
     </form>
     <p id="board-notice" role="status" aria-live="polite">正在加载进度数据…</p>
     <div id="board-results" class="board-results" role="region" aria-label="论文进度表，可横向滚动" tabindex="0"></div>
     <noscript><p>交互看板需要 JavaScript；可使用下方的仓库进度清单。</p></noscript>
     <p class="board-footer">进度随仓库清单更新并重新构建，不查询公众号后台。<a href="https://github.com/lichao689/woeai/blob/main/project/publication-progress.md">查看仓库进度清单</a> · <a href="https://github.com/lichao689/woeai/blob/main/project/guides/publication-registry.md">状态说明</a></p>
   </div>

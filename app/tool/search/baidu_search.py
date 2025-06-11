import logging
from typing import List

from baidusearch.baidusearch import search

from app.tool.search.base import SearchItem, WebSearchEngine

logger = logging.getLogger(__name__)


class BaiduSearchEngine(WebSearchEngine):
    def perform_search(
        self, query: str, num_results: int = 10, *args, **kwargs
    ) -> List[SearchItem]:
        """
        Baidu search engine.

        Returns results formatted according to SearchItem model.
        """
        logger.info(f"开始百度搜索 - 查询: '{query}', 请求结果数: {num_results}")

        try:
            raw_results = search(query, num_results=num_results)
            logger.info(f"百度搜索原始结果数量: {len(raw_results) if raw_results else 0}")

            if not raw_results:
                logger.warning(f"百度搜索未返回任何结果 - 查询: '{query}'")
                return []

            # Convert raw results to SearchItem format
            results = []
            for i, item in enumerate(raw_results):
                try:
                    if isinstance(item, str):
                        # If it's just a URL
                        logger.debug(f"处理字符串类型结果 [{i+1}]: {item}")
                        results.append(
                            SearchItem(title=f"Baidu Result {i+1}", url=item, description=None)
                        )
                    elif isinstance(item, dict):
                        # If it's a dictionary with details
                        title = item.get("title", f"Baidu Result {i+1}")
                        url = item.get("url", "")
                        description = item.get("abstract", None)
                        logger.debug(f"处理字典类型结果 [{i+1}]: title='{title}', url='{url}'")
                        results.append(
                            SearchItem(
                                title=title,
                                url=url,
                                description=description,
                            )
                        )
                    else:
                        # Try to get attributes directly
                        try:
                            title = getattr(item, "title", f"Baidu Result {i+1}")
                            url = getattr(item, "url", "")
                            description = getattr(item, "abstract", None)
                            logger.debug(f"处理对象类型结果 [{i+1}]: title='{title}', url='{url}'")
                            results.append(
                                SearchItem(
                                    title=title,
                                    url=url,
                                    description=description,
                                )
                            )
                        except Exception as e:
                            # Fallback to a basic result
                            logger.warning(f"处理搜索结果 [{i+1}] 时发生错误: {e}, 使用备用格式")
                            results.append(
                                SearchItem(
                                    title=f"Baidu Result {i+1}", url=str(item), description=None
                                )
                            )
                except Exception as e:
                    logger.error(f"处理搜索结果项 [{i+1}] 时发生异常: {e}, 跳过此结果")
                    continue

            logger.info(f"百度搜索完成 - 查询: '{query}', 返回有效结果数: {len(results)}")
            return results

        except Exception as e:
            logger.error(f"百度搜索发生异常 - 查询: '{query}', 错误: {e}")
            raise

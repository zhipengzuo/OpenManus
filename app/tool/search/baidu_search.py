from typing import List

from baidusearch.baidusearch import search

from app.logger import logger
from app.tool.search.base import SearchItem, WebSearchEngine


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

            # Convert raw results to SearchItem format
            results = []
            for i, item in enumerate(raw_results):
                if isinstance(item, str):
                    # If it's just a URL
                    results.append(
                        SearchItem(title=f"Baidu Result {i+1}", url=item, description=None)
                    )
                    logger.debug(f"处理URL结果 {i+1}: {item}")
                elif isinstance(item, dict):
                    # If it's a dictionary with details
                    title = item.get("title", f"Baidu Result {i+1}")
                    url = item.get("url", "")
                    description = item.get("abstract", None)
                    results.append(
                        SearchItem(title=title, url=url, description=description)
                    )
                    logger.debug(f"处理字典结果 {i+1}: 标题='{title}', URL='{url}'")
                else:
                    # Try to get attributes directly
                    try:
                        title = getattr(item, "title", f"Baidu Result {i+1}")
                        url = getattr(item, "url", "")
                        description = getattr(item, "abstract", None)
                        results.append(
                            SearchItem(title=title, url=url, description=description)
                        )
                        logger.debug(f"处理对象结果 {i+1}: 标题='{title}', URL='{url}'")
                    except Exception as parse_error:
                        # Fallback to a basic result
                        results.append(
                            SearchItem(
                                title=f"Baidu Result {i+1}", url=str(item), description=None
                            )
                        )
                        logger.warning(f"解析结果 {i+1} 失败，使用备用格式: {str(parse_error)}")

            logger.info(f"百度搜索完成 - 查询: '{query}', 返回 {len(results)} 个结果")
            return results

        except Exception as e:
            logger.error(f"百度搜索失败 - 查询: '{query}', 错误: {str(e)}")
            logger.exception("百度搜索异常详细信息:")
            return []

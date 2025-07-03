from typing import List

from duckduckgo_search import DDGS

from app.logger import logger
from app.tool.search.base import SearchItem, WebSearchEngine


class DuckDuckGoSearchEngine(WebSearchEngine):
    def perform_search(
        self, query: str, num_results: int = 10, *args, **kwargs
    ) -> List[SearchItem]:
        """
        DuckDuckGo search engine.

        Returns results formatted according to SearchItem model.
        """
        logger.info(f"开始DuckDuckGo搜索 - 查询: '{query}', 请求结果数: {num_results}")

        try:
            raw_results = DDGS().text(query, max_results=num_results)

            results = []
            for i, item in enumerate(raw_results):
                if isinstance(item, str):
                    # If it's just a URL
                    results.append(
                        SearchItem(
                            title=f"DuckDuckGo Result {i + 1}", url=item, description=None
                        )
                    )
                    logger.debug(f"处理URL结果 {i+1}: {item}")
                elif isinstance(item, dict):
                    # Extract data from the dictionary
                    title = item.get("title", f"DuckDuckGo Result {i + 1}")
                    url = item.get("href", "")
                    description = item.get("body", None)
                    results.append(
                        SearchItem(title=title, url=url, description=description)
                    )
                    logger.debug(f"处理字典结果 {i+1}: 标题='{title}', URL='{url}'")
                else:
                    # Try to extract attributes directly
                    try:
                        title = getattr(item, "title", f"DuckDuckGo Result {i + 1}")
                        url = getattr(item, "href", "")
                        description = getattr(item, "body", None)
                        results.append(
                            SearchItem(title=title, url=url, description=description)
                        )
                        logger.debug(f"处理对象结果 {i+1}: 标题='{title}', URL='{url}'")
                    except Exception as parse_error:
                        # Fallback
                        results.append(
                            SearchItem(
                                title=f"DuckDuckGo Result {i + 1}",
                                url=str(item),
                                description=None,
                            )
                        )
                        logger.warning(f"解析结果 {i+1} 失败，使用备用格式: {str(parse_error)}")

            logger.info(f"DuckDuckGo搜索完成 - 查询: '{query}', 返回 {len(results)} 个结果")
            return results

        except Exception as e:
            logger.error(f"DuckDuckGo搜索失败 - 查询: '{query}', 错误: {str(e)}")
            logger.exception("DuckDuckGo搜索异常详细信息:")
            return []

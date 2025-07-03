from typing import List

from googlesearch import search

from app.logger import logger
from app.tool.search.base import SearchItem, WebSearchEngine


class GoogleSearchEngine(WebSearchEngine):
    def perform_search(
        self, query: str, num_results: int = 10, *args, **kwargs
    ) -> List[SearchItem]:
        """
        Google search engine.

        Returns results formatted according to SearchItem model.
        """
        logger.info(f"开始Google搜索 - 查询: '{query}', 请求结果数: {num_results}")

        try:
            raw_results = search(query, num_results=num_results, advanced=True)

            results = []
            for i, item in enumerate(raw_results):
                if isinstance(item, str):
                    # If it's just a URL
                    results.append(
                        {"title": f"Google Result {i+1}", "url": item, "description": ""}
                    )
                    logger.debug(f"处理URL结果 {i+1}: {item}")
                else:
                    results.append(
                        SearchItem(
                            title=item.title, url=item.url, description=item.description
                        )
                    )
                    logger.debug(f"处理详细结果 {i+1}: 标题='{item.title}', URL='{item.url}'")

            logger.info(f"Google搜索完成 - 查询: '{query}', 返回 {len(results)} 个结果")
            return results

        except Exception as e:
            logger.error(f"Google搜索失败 - 查询: '{query}', 错误: {str(e)}")
            logger.exception("Google搜索异常详细信息:")
            return []

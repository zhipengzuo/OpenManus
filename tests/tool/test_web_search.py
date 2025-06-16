import asyncio
from typing import List
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest

from app.tool.search.base import SearchItem
from app.tool.search.google_search import GoogleSearchEngine
from app.tool.web_search import (SearchMetadata, SearchResponse, SearchResult,
                                 WebContentFetcher, WebSearch)


class TestWebSearch:
    """Test cases for WebSearch class."""

    @pytest.fixture
    def web_search(self):
        """Create a WebSearch instance for testing."""
        return WebSearch()

    @pytest.fixture
    def mock_search_items(self):
        """Mock search items returned by search engines."""
        return [
            SearchItem(
                title="Python Tutorial",
                url="https://example1.com",
                description="Learn Python programming"
            ),
            SearchItem(
                title="Advanced Python",
                url="https://example2.com",
                description="Advanced Python techniques"
            )
        ]

    @pytest.fixture
    def mock_google_search_results(self):
        """Mock Google search results."""
        return [
            SearchItem(
                title="Google Result 1",
                url="https://google1.com",
                description="First Google result"
            ),
            SearchItem(
                title="Google Result 2",
                url="https://google2.com",
                description="Second Google result"
            )
        ]

    @pytest.mark.asyncio
    async def test_execute_successful_search(self, web_search, mock_search_items):
        """Test successful search execution."""
        with patch.object(web_search, '_try_all_engines', return_value=mock_search_items):
            response = await web_search.execute("Python programming", num_results=2)

            assert isinstance(response, SearchResponse)
            assert response.status == "success"
            assert response.query == "Python programming"
            assert len(response.results) == 2
            assert response.metadata.total_results == 2
            assert response.metadata.language == "en"
            assert response.metadata.country == "us"

            # Check individual results
            assert response.results[0].title == "Python Tutorial"
            assert response.results[0].url == "https://example1.com"
            assert response.results[0].position == 1

            assert response.results[1].title == "Advanced Python"
            assert response.results[1].url == "https://example2.com"
            assert response.results[1].position == 2

    @pytest.mark.asyncio
    async def test_execute_with_content_fetching(self, web_search, mock_search_items):
        """Test search execution with content fetching enabled."""
        mock_content = "This is the fetched content from the webpage."

        with patch.object(web_search, '_try_all_engines', return_value=mock_search_items), \
             patch.object(web_search, '_fetch_content_for_results') as mock_fetch:

            # Setup mock to return results with content
            enhanced_results = mock_search_items.copy()
            for result in enhanced_results:
                result.raw_content = mock_content
            mock_fetch.return_value = enhanced_results

            response = await web_search.execute(
                "Python programming",
                num_results=2,
                fetch_content=True
            )

            mock_fetch.assert_called_once()
            assert response.results[0].raw_content == mock_content
            assert response.results[1].raw_content == mock_content

    @pytest.mark.asyncio
    async def test_execute_search_failure_with_retries(self, web_search):
        """Test search failure handling with retries."""
        with patch.object(web_search, '_try_all_engines', return_value=[]), \
             patch('asyncio.sleep', new_callable=AsyncMock) as mock_sleep:

            response = await web_search.execute("failed query")

            assert response.status != "success"
            assert response.error is not None
            assert "All search engines failed" in response.error
            assert response.results == []

            # Should have retried 3 times (default max_retries)
            assert mock_sleep.call_count >= 3

    @pytest.mark.asyncio
    async def test_execute_with_custom_language_and_country(self, web_search, mock_search_items):
        """Test search with custom language and country settings."""
        with patch.object(web_search, '_try_all_engines', return_value=mock_search_items):
            response = await web_search.execute(
                "test query",
                lang="zh",
                country="cn"
            )

            assert response.metadata.language == "zh"
            assert response.metadata.country == "cn"

    @pytest.mark.asyncio
    async def test_try_all_engines_google_first(self, web_search, mock_google_search_results):
        """Test that Google search engine is tried first."""
        with patch.object(web_search, '_get_engine_order', return_value=['google', 'bing', 'duckduckgo']), \
             patch.object(web_search, '_perform_search_with_engine') as mock_perform:

            mock_perform.return_value = mock_google_search_results

            results = await web_search._try_all_engines("test query", 5, {"lang": "en", "country": "us"})

            # Should call Google search first
            mock_perform.assert_called_once()
            call_args = mock_perform.call_args
            assert isinstance(call_args[0][0], GoogleSearchEngine)  # First argument should be GoogleSearchEngine
            assert call_args[0][1] == "test query"  # Query
            assert call_args[0][2] == 5  # num_results

            # Check results are properly formatted
            assert len(results) == 2
            assert all(isinstance(result, SearchResult) for result in results)
            assert results[0].source == "google"

    @pytest.mark.asyncio
    async def test_try_all_engines_fallback_on_google_failure(self, web_search):
        """Test fallback to other engines when Google fails."""
        mock_bing_results = [
            SearchItem(title="Bing Result", url="https://bing.com", description="From Bing")
        ]

        with patch.object(web_search, '_get_engine_order', return_value=['google', 'bing', 'duckduckgo']), \
             patch.object(web_search, '_perform_search_with_engine') as mock_perform:

            # Google fails, Bing succeeds
            mock_perform.side_effect = [[], mock_bing_results]

            results = await web_search._try_all_engines("test query", 5, {"lang": "en", "country": "us"})

            # Should have tried Google first, then Bing
            assert mock_perform.call_count == 2
            assert len(results) == 1
            assert results[0].source == "bing"

    @pytest.mark.asyncio
    async def test_perform_search_with_engine_google(self, web_search):
        """Test _perform_search_with_engine specifically with GoogleSearchEngine."""
        google_engine = GoogleSearchEngine()
        mock_search_items = [
            SearchItem(title="Test", url="https://test.com", description="Test desc")
        ]

        with patch.object(google_engine, 'perform_search', return_value=mock_search_items):
            results = await web_search._perform_search_with_engine(
                google_engine,
                "test query",
                5,
                {"lang": "en", "country": "us"}
            )

            assert results == mock_search_items
            google_engine.perform_search.assert_called_once_with(
                "test query",
                num_results=5,
                lang="en",
                country="us"
            )

    @pytest.mark.asyncio
    async def test_fetch_content_for_results(self, web_search):
        """Test content fetching for search results."""
        results = [
            SearchResult(
                position=1,
                title="Test Result",
                url="https://example.com",
                description="Test description",
                source="google"
            )
        ]

        mock_content = "Fetched webpage content"

        with patch.object(web_search.content_fetcher, 'fetch_content', return_value=mock_content):
            enhanced_results = await web_search._fetch_content_for_results(results)

            assert len(enhanced_results) == 1
            assert enhanced_results[0].raw_content == mock_content

    def test_get_engine_order_google_preferred(self, web_search):
        """Test that Google is preferred in engine order."""
        with patch('app.config.config.search_config') as mock_config:
            mock_config.engine = "google"
            mock_config.fallback_engines = ["bing", "duckduckgo"]

            engine_order = web_search._get_engine_order()

            assert engine_order[0] == "google"
            assert "bing" in engine_order
            assert "duckduckgo" in engine_order

    def test_get_engine_order_no_config(self, web_search):
        """Test engine order when no config is provided."""
        with patch('app.config.config.search_config', None):
            engine_order = web_search._get_engine_order()

            # Should default to Google first
            assert engine_order[0] == "google"
            assert len(engine_order) == 4  # All available engines


class TestWebContentFetcher:
    """Test cases for WebContentFetcher class."""

    @pytest.fixture
    def content_fetcher(self):
        """Create a WebContentFetcher instance for testing."""
        return WebContentFetcher()

    @pytest.mark.asyncio
    async def test_fetch_content_success(self, content_fetcher):
        """Test successful content fetching."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <head><title>Test Page</title></head>
            <body>
                <h1>Main Content</h1>
                <p>This is the main content of the page.</p>
                <script>alert('remove me');</script>
                <style>body { color: red; }</style>
            </body>
        </html>
        """

        with patch('requests.get', return_value=mock_response):
            content = await content_fetcher.fetch_content("https://example.com")

            assert content is not None
            assert "Main Content" in content
            assert "This is the main content" in content
            assert "alert('remove me')" not in content  # Script should be removed
            assert "color: red" not in content  # Style should be removed

    @pytest.mark.asyncio
    async def test_fetch_content_http_error(self, content_fetcher):
        """Test content fetching with HTTP error."""
        mock_response = Mock()
        mock_response.status_code = 404

        with patch('requests.get', return_value=mock_response):
            content = await content_fetcher.fetch_content("https://example.com")

            assert content is None

    @pytest.mark.asyncio
    async def test_fetch_content_request_exception(self, content_fetcher):
        """Test content fetching with request exception."""
        with patch('requests.get', side_effect=Exception("Connection error")):
            content = await content_fetcher.fetch_content("https://example.com")

            assert content is None

    @pytest.mark.asyncio
    async def test_fetch_content_with_timeout(self, content_fetcher):
        """Test content fetching with custom timeout."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Test</body></html>"

        with patch('requests.get', return_value=mock_response) as mock_get:
            await content_fetcher.fetch_content("https://example.com", timeout=5)

            mock_get.assert_called_once()
            call_kwargs = mock_get.call_args[1]
            assert call_kwargs['timeout'] == 5

    @pytest.mark.asyncio
    async def test_fetch_content_size_limit(self, content_fetcher):
        """Test that content is limited to 10KB."""
        large_content = "x" * 20000  # 20KB content
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = f"<html><body>{large_content}</body></html>"

        with patch('requests.get', return_value=mock_response):
            content = await content_fetcher.fetch_content("https://example.com")

            assert content is not None
            assert len(content) <= 10000  # Should be truncated to 10KB


class TestSearchResponseModel:
    """Test cases for SearchResponse model."""

    def test_search_response_success_output_formatting(self):
        """Test that SearchResponse formats output correctly for successful searches."""
        results = [
            SearchResult(
                position=1,
                title="Python Tutorial",
                url="https://example1.com",
                description="Learn Python programming",
                source="google"
            ),
            SearchResult(
                position=2,
                title="Advanced Python",
                url="https://example2.com",
                description="Advanced techniques",
                source="google",
                raw_content="This is the full content of the page..."
            )
        ]

        metadata = SearchMetadata(
            total_results=2,
            language="en",
            country="us"
        )

        response = SearchResponse(
            status="success",
            query="Python programming",
            results=results,
            metadata=metadata
        )

        output = response.output
        assert "Search results for 'Python programming':" in output
        assert "1. Python Tutorial" in output
        assert "URL: https://example1.com" in output
        assert "Description: Learn Python programming" in output
        assert "2. Advanced Python" in output
        assert "Content: This is the full content" in output
        assert "Total results: 2" in output
        assert "Language: en" in output
        assert "Country: us" in output

    def test_search_response_error_output(self):
        """Test SearchResponse with error."""
        response = SearchResponse(
            query="failed query",
            error="Search failed",
            results=[]
        )

        assert response.error == "Search failed"
        assert response.results == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

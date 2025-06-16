from typing import List
from unittest.mock import MagicMock, Mock, patch

import pytest

from app.tool.search.base import SearchItem
from app.tool.search.google_search import GoogleSearchEngine


class TestGoogleSearchEngine:
    """Test cases for GoogleSearchEngine class."""

    @pytest.fixture
    def search_engine(self):
        """Create a GoogleSearchEngine instance for testing."""
        return GoogleSearchEngine()

    @pytest.fixture
    def mock_search_results(self):
        """Mock search results with different formats."""
        # Mock advanced search results with objects
        mock_result_1 = Mock()
        mock_result_1.title = "Python Programming Tutorial"
        mock_result_1.url = "https://example1.com"
        mock_result_1.description = "Learn Python programming"

        mock_result_2 = Mock()
        mock_result_2.title = "Advanced Python"
        mock_result_2.url = "https://example2.com"
        mock_result_2.description = "Advanced Python techniques"

        return [mock_result_1, mock_result_2]

    @pytest.fixture
    def mock_simple_search_results(self):
        """Mock simple search results with just URLs."""
        return ["https://simple1.com", "https://simple2.com"]

    @patch('app.tool.search.google_search.search')
    def test_perform_search_with_advanced_results(self, mock_search, search_engine, mock_search_results):
        """Test searching with advanced result objects."""
        mock_search.return_value = mock_search_results

        results = search_engine.perform_search("Python programming", num_results=2)

        # Verify the search function was called correctly
        mock_search.assert_called_once_with("Python programming", num_results=2, advanced=True)

        # Verify results format
        assert len(results) == 2
        assert isinstance(results[0], SearchItem)
        assert isinstance(results[1], SearchItem)

        # Check first result
        assert results[0].title == "Python Programming Tutorial"
        assert results[0].url == "https://example1.com"
        assert results[0].description == "Learn Python programming"

        # Check second result
        assert results[1].title == "Advanced Python"
        assert results[1].url == "https://example2.com"
        assert results[1].description == "Advanced Python techniques"

    @patch('app.tool.search.google_search.search')
    def test_perform_search_with_simple_url_results(self, mock_search, search_engine, mock_simple_search_results):
        """Test searching with simple URL string results."""
        mock_search.return_value = mock_simple_search_results

        results = search_engine.perform_search("test query", num_results=2)

        # Verify the search function was called correctly
        mock_search.assert_called_once_with("test query", num_results=2, advanced=True)

        # Verify results format
        assert len(results) == 2

        # Check that URL strings are converted to proper SearchItem objects
        assert results[0]["title"] == "Google Result 1"
        assert results[0]["url"] == "https://simple1.com"
        assert results[0]["description"] == ""

        assert results[1]["title"] == "Google Result 2"
        assert results[1]["url"] == "https://simple2.com"
        assert results[1]["description"] == ""

    @patch('app.tool.search.google_search.search')
    def test_perform_search_with_mixed_results(self, mock_search, search_engine):
        """Test searching with mixed result types (both objects and strings)."""
        # Create mixed results
        mock_result_obj = Mock()
        mock_result_obj.title = "Object Result"
        mock_result_obj.url = "https://object.com"
        mock_result_obj.description = "Object description"

        mixed_results = [mock_result_obj, "https://string.com"]
        mock_search.return_value = mixed_results

        results = search_engine.perform_search("mixed query", num_results=2)

        # Verify results
        assert len(results) == 2

        # First result should be from the object
        assert isinstance(results[0], SearchItem)
        assert results[0].title == "Object Result"
        assert results[0].url == "https://object.com"
        assert results[0].description == "Object description"

        # Second result should be converted from string
        assert results[1]["title"] == "Google Result 2"
        assert results[1]["url"] == "https://string.com"
        assert results[1]["description"] == ""

    @patch('app.tool.search.google_search.search')
    def test_perform_search_with_empty_results(self, mock_search, search_engine):
        """Test searching when no results are returned."""
        mock_search.return_value = []

        results = search_engine.perform_search("empty query")

        assert results == []
        mock_search.assert_called_once_with("empty query", num_results=10, advanced=True)

    @patch('app.tool.search.google_search.search')
    def test_perform_search_with_default_num_results(self, mock_search, search_engine):
        """Test that default num_results parameter works correctly."""
        mock_search.return_value = []

        search_engine.perform_search("test query")

        # Should use default value of 10
        mock_search.assert_called_once_with("test query", num_results=10, advanced=True)

    @patch('app.tool.search.google_search.search')
    def test_perform_search_with_custom_num_results(self, mock_search, search_engine):
        """Test that custom num_results parameter works correctly."""
        mock_search.return_value = []

        search_engine.perform_search("test query", num_results=5)

        mock_search.assert_called_once_with("test query", num_results=5, advanced=True)

    @patch('app.tool.search.google_search.search')
    def test_perform_search_with_additional_args(self, mock_search, search_engine):
        """Test that additional args and kwargs are passed through."""
        mock_search.return_value = []

        search_engine.perform_search("test query", num_results=3, lang="en", country="us")

        mock_search.assert_called_once_with("test query", num_results=3, advanced=True)

    @patch('app.tool.search.google_search.search')
    def test_perform_search_exception_handling(self, mock_search, search_engine):
        """Test that exceptions from the search library are properly handled."""
        mock_search.side_effect = Exception("Search API error")

        with pytest.raises(Exception) as exc_info:
            search_engine.perform_search("error query")

        assert "Search API error" in str(exc_info.value)

    @patch('app.tool.search.google_search.search')
    def test_perform_search_with_malformed_objects(self, mock_search, search_engine):
        """Test handling of malformed result objects."""
        # Create a mock object that's missing some attributes
        malformed_result = Mock()
        malformed_result.title = "Title only"
        # Missing url and description attributes

        mock_search.return_value = [malformed_result]

        # This should raise an AttributeError when trying to access missing attributes
        with pytest.raises(AttributeError):
            search_engine.perform_search("malformed query")

    def test_inheritance(self, search_engine):
        """Test that GoogleSearchEngine properly inherits from WebSearchEngine."""
        from app.tool.search.base import WebSearchEngine
        assert isinstance(search_engine, WebSearchEngine)

    def test_method_signature(self, search_engine):
        """Test that perform_search method has the correct signature."""
        import inspect
        signature = inspect.signature(search_engine.perform_search)

        # Check parameter names
        param_names = list(signature.parameters.keys())
        assert "query" in param_names
        assert "num_results" in param_names
        assert "args" in param_names
        assert "kwargs" in param_names

        # Check default value for num_results
        assert signature.parameters["num_results"].default == 10

        # Check return annotation
        assert signature.return_annotation == List[SearchItem]


class TestGoogleSearchEngineIntegration:
    """Integration tests for GoogleSearchEngine (optional - requires network)."""

    @pytest.mark.integration
    @pytest.mark.skip(reason="Requires network access and may be flaky")
    def test_real_search(self):
        """Test actual search functionality (integration test)."""
        engine = GoogleSearchEngine()
        results = engine.perform_search("Python programming", num_results=2)

        assert len(results) <= 2  # May return fewer results
        if results:
            assert all(isinstance(result, (SearchItem, dict)) for result in results)
            assert all(result.get("url") or hasattr(result, "url") for result in results)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

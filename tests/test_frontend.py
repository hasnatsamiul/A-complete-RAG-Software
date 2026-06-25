from unittest.mock import MagicMock

def test_rag_search_response():
    mock_rag = MagicMock()
    mock_rag.search_and_summarize.return_value = "This is a test answer."

    answer = mock_rag.search_and_summarize("What is TKG?", top_k=3)

    assert answer == "This is a test answer."
    mock_rag.search_and_summarize.assert_called_once_with("What is TKG?", top_k=3)
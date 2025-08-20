"""
Paper Service - Main backend service combining ArXiv API and caching
"""
from typing import List, Dict
from .arxiv_service import ArxivService
from .cache_manager import CacheManager


class PaperService:
    def __init__(self, cache_duration_minutes: int = 30):
        self.arxiv_service = ArxivService()
        self.cache_manager = CacheManager(cache_duration_minutes)
    
    def get_papers(self, force_refresh: bool = False, days_back: int = 2, max_results: int = 100) -> List[Dict]:
        """Get papers from cache or fetch from API"""
        
        # Check cache first unless force refresh
        if not force_refresh:
            cached_papers = self.cache_manager.get_cached_papers()
            if cached_papers:
                print(f"Using cached papers ({len(cached_papers)} papers)")
                return cached_papers
        
        # Fetch fresh papers from API
        print("Fetching fresh papers from arXiv API...")
        try:
            papers = self.arxiv_service.get_daily_ai_papers(
                days_back=days_back, 
                max_results=max_results
            )
            
            # Update cache
            self.cache_manager.update_cache(papers)
            return papers
            
        except Exception as e:
            print(f"Error fetching papers: {e}")
            # Return cached papers if available, empty list otherwise
            return self.cache_manager.get_cached_papers()
    
    def get_cache_info(self) -> Dict:
        """Get cache status information"""
        return self.cache_manager.get_cache_info()
    
    def clear_cache(self) -> None:
        """Clear the cache"""
        self.cache_manager.clear_cache()
    
    def filter_papers_by_category(self, papers: List[Dict], category: str) -> List[Dict]:
        """Filter papers by category"""
        if not category or category == 'all':
            return papers
        
        return [paper for paper in papers if category in paper.get('categories', [])]
    
    def get_all_categories(self, papers: List[Dict]) -> set:
        """Get all unique categories from papers"""
        categories = set()
        for paper in papers:
            categories.update(paper.get('categories', []))
        return categories
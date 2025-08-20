"""
Cache Manager - Handles in-memory caching for papers
"""
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class CacheManager:
    def __init__(self, cache_duration_minutes: int = 30):
        self.cache = {
            'papers': [],
            'last_updated': None,
            'cache_date': None,
            'cache_duration': timedelta(minutes=cache_duration_minutes)
        }
    
    def is_cache_valid(self) -> bool:
        """Check if cache is still valid"""
        if not self.cache['papers'] or self.cache['last_updated'] is None:
            return False
        
        now = datetime.now()
        today = now.date()
        
        # Cache is invalid if it's a new day or expired
        if (self.cache['cache_date'] != today or 
            now - self.cache['last_updated'] > self.cache['cache_duration']):
            return False
        
        return True
    
    def get_cached_papers(self) -> List[Dict]:
        """Get papers from cache if valid"""
        if self.is_cache_valid():
            return self.cache['papers']
        return []
    
    def update_cache(self, papers: List[Dict]) -> None:
        """Update cache with new papers"""
        now = datetime.now()
        today = now.date()
        
        # Clear cache if it's a new day
        if self.cache['cache_date'] and self.cache['cache_date'] != today:
            print(f"New day detected ({today}), clearing cache from {self.cache['cache_date']}")
            self.cache['papers'] = []
        
        self.cache['papers'] = papers
        self.cache['last_updated'] = now
        self.cache['cache_date'] = today
        
        print(f"Cache updated with {len(papers)} papers for {today}")
    
    def get_cache_info(self) -> Dict:
        """Get cache status information"""
        if not self.cache['last_updated']:
            return {
                'age_minutes': 0,
                'cache_date': None,
                'is_valid': False,
                'papers_count': 0
            }
        
        now = datetime.now()
        age_minutes = int((now - self.cache['last_updated']).total_seconds() / 60)
        
        return {
            'age_minutes': age_minutes,
            'cache_date': self.cache['cache_date'],
            'is_valid': self.is_cache_valid(),
            'papers_count': len(self.cache['papers'])
        }
    
    def clear_cache(self) -> None:
        """Manually clear the cache"""
        self.cache['papers'] = []
        self.cache['last_updated'] = None
        self.cache['cache_date'] = None
        print("Cache cleared manually")
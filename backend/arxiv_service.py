"""
ArXiv API Service - Backend service for fetching AI research papers
"""
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional


class ArxivService:
    def __init__(self):
        self.base_url = "http://export.arxiv.org/api/query"
        # AI-related categories on arXiv
        self.ai_categories = [
            "cs.AI",    # Artificial Intelligence
            "cs.LG",    # Machine Learning  
            "cs.CL",    # Computation and Language
            "cs.CV",    # Computer Vision and Pattern Recognition
            "cs.NE",    # Neural and Evolutionary Computing
            "stat.ML"   # Machine Learning (Statistics)
        ]
        
    def build_search_query(self, days_back: int = 1) -> str:
        """Build search query for AI papers from the last N days"""
        # Create category search (papers in any of the AI categories)
        category_query = " OR ".join([f"cat:{cat}" for cat in self.ai_categories])
        
        # You can also add keyword search for broader coverage
        keyword_query = "all:artificial+intelligence OR all:machine+learning OR all:deep+learning OR all:neural+network"
        
        # Combine queries
        full_query = f"({category_query}) OR ({keyword_query})"
        return full_query
    
    def fetch_papers_xml(self, max_results: int = 100, days_back: int = 1) -> Optional[str]:
        """Fetch AI papers from arXiv API"""
        query = self.build_search_query(days_back)
        
        params = {
            'search_query': query,
            'start': 0,
            'max_results': max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching data from arXiv: {e}")
            return None
    
    def parse_xml_response(self, xml_content: str) -> List[Dict]:
        """Parse XML response from arXiv API"""
        try:
            root = ET.fromstring(xml_content)
            # Define namespace
            ns = {'atom': 'http://www.w3.org/2005/Atom',
                  'arxiv': 'http://arxiv.org/schemas/atom'}
            
            papers = []
            entries = root.findall('atom:entry', ns)
            
            for entry in entries:
                paper = {}
                
                # Title
                title_elem = entry.find('atom:title', ns)
                paper['title'] = title_elem.text.strip().replace('\n', ' ') if title_elem is not None else "N/A"
                
                # Authors
                authors = []
                author_elems = entry.findall('atom:author', ns)
                for author in author_elems:
                    name_elem = author.find('atom:name', ns)
                    if name_elem is not None:
                        authors.append(name_elem.text.strip())
                paper['authors'] = authors
                
                # Abstract
                summary_elem = entry.find('atom:summary', ns)
                paper['abstract'] = summary_elem.text.strip().replace('\n', ' ') if summary_elem is not None else "N/A"
                
                # Published date
                published_elem = entry.find('atom:published', ns)
                if published_elem is not None:
                    # Parse date string like "2024-01-15T18:00:01Z"
                    date_str = published_elem.text.strip()
                    try:
                        parsed_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                        paper['published_date'] = parsed_date
                        paper['published_date_str'] = parsed_date.strftime("%Y-%m-%d %H:%M:%S UTC")
                    except ValueError:
                        paper['published_date'] = None
                        paper['published_date_str'] = date_str
                else:
                    paper['published_date'] = None
                    paper['published_date_str'] = "N/A"
                
                # arXiv ID and link
                id_elem = entry.find('atom:id', ns)
                paper['arxiv_id'] = id_elem.text.strip() if id_elem is not None else "N/A"
                
                # Categories
                categories = []
                category_elems = entry.findall('atom:category', ns)
                for cat in category_elems:
                    term = cat.get('term')
                    if term:
                        categories.append(term)
                paper['categories'] = categories
                
                papers.append(paper)
            
            return papers
            
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")
            return []
    
    def filter_by_date(self, papers: List[Dict], days_back: int = 1) -> List[Dict]:
        """Filter papers by publication date"""
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_back)
        
        filtered_papers = []
        for paper in papers:
            if paper['published_date'] and paper['published_date'] >= cutoff_date:
                filtered_papers.append(paper)
        
        return filtered_papers
    
    def get_daily_ai_papers(self, days_back: int = 1, max_results: int = 100) -> List[Dict]:
        """Main function to get daily AI papers"""
        print(f"Fetching AI papers from the last {days_back} day(s)...")
        
        # Fetch papers
        xml_content = self.fetch_papers_xml(max_results, days_back)
        if not xml_content:
            return []
        
        # Parse papers
        papers = self.parse_xml_response(xml_content)
        if not papers:
            print("No papers found or error parsing response")
            return []
        
        # Filter by date
        recent_papers = self.filter_by_date(papers, days_back)
        
        print(f"Found {len(recent_papers)} AI papers from the last {days_back} day(s)")
        return recent_papers
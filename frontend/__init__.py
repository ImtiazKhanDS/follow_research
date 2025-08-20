"""
Frontend package for Daily AI Research Feed
"""
from .components import *
from .styles import get_app_styles

__all__ = [
    'create_paper_card', 
    'create_stats_section', 
    'create_empty_stats_section',
    'create_filter_section', 
    'create_empty_papers_message',
    'get_category_display_name',
    'get_app_styles'
]
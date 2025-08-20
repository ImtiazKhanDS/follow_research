"""
Daily AI Research Feed - Main Application
A beautiful web application for browsing the latest AI research papers from arXiv
"""
from fasthtml.common import *
from backend import PaperService
from frontend import (
    create_paper_card, create_stats_section, create_empty_stats_section,
    create_filter_section, create_empty_papers_message, get_app_styles
)

# Initialize FastHTML app with custom styles
app, rt = fast_app(hdrs=[get_app_styles()])

# Initialize services
paper_service = PaperService(cache_duration_minutes=30)


@rt("/")
def home(category: str = None):
    """Main page - display papers with optional category filtering"""
    # Get papers from service
    papers = paper_service.get_papers()
    
    # Filter papers by category if specified
    if category and category != 'all':
        papers = paper_service.filter_papers_by_category(papers, category)
    
    # Get stats
    total_papers = len(papers)
    all_papers = paper_service.get_papers()  # Get all papers for stats
    all_papers_count = len(all_papers)
    categories = paper_service.get_all_categories(all_papers)
    cache_info = paper_service.get_cache_info()
    
    # Handle empty state
    if not all_papers:
        return Titled("Daily AI Research Feed",
            create_empty_stats_section()
        )
    
    # Create main page
    return Titled("Daily AI Research Feed",
        # Stats section with glittery header
        create_stats_section(
            total_papers=total_papers,
            all_papers_count=all_papers_count,
            categories_count=len(categories),
            cache_age_minutes=cache_info['age_minutes'],
            category=category
        ),
        
        # Filter section
        create_filter_section(categories, category),
        
        # Papers list (single column)
        Div(
            *[create_paper_card(paper) for paper in papers] if papers else [
                create_empty_papers_message()
            ],
            cls="grid-container"
        )
    )


@rt("/refresh")
def refresh():
    """Force refresh papers from API"""
    paper_service.get_papers(force_refresh=True)
    return RedirectResponse("/", status_code=303)


@rt("/debug")
def debug():
    """Debug endpoint to check cache status"""
    cache_info = paper_service.get_cache_info()
    papers = paper_service.get_papers()
    
    debug_info = f"""
Cache Status:
- Papers in cache: {len(papers)}
- Cache date: {cache_info['cache_date']}
- Cache age: {cache_info['age_minutes']} minutes
- Cache valid: {cache_info['is_valid']}
- Papers count: {cache_info['papers_count']}
"""
    
    return Pre(debug_info)


if __name__ == "__main__":
    serve()
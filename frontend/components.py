"""
Frontend Components - UI components for the Daily AI Research Feed
"""
from fasthtml.common import *


# Category mapping for better display names
CATEGORY_NAMES = {
    'cs.AI': 'Artificial Intelligence',
    'cs.LG': 'Machine Learning',
    'cs.CV': 'Computer Vision',
    'cs.CL': 'Natural Language Processing',
    'cs.NE': 'Neural Networks',
    'stat.ML': 'Statistical ML',
    'cs.RO': 'Robotics',
    'cs.IR': 'Information Retrieval',
    'cs.HC': 'Human-Computer Interaction',
    'cs.CR': 'Cryptography',
    'cs.DC': 'Distributed Computing',
    'cs.DS': 'Data Structures',
    'cs.GT': 'Game Theory',
    'cs.IT': 'Information Theory',
    'cs.MA': 'Multiagent Systems',
    'cs.MM': 'Multimedia',
    'cs.NI': 'Networking',
    'cs.PL': 'Programming Languages',
    'cs.SE': 'Software Engineering',
    'cs.SY': 'Systems and Control'
}


def get_category_display_name(category_code: str) -> str:
    """Convert category code to readable name"""
    return CATEGORY_NAMES.get(category_code, category_code)


def get_category_css_class(category_code: str) -> str:
    """Get CSS class for category styling"""
    category_map = {
        'cs.AI': 'category-ai',
        'cs.LG': 'category-ml', 
        'cs.CV': 'category-cv',
        'cs.CL': 'category-cl',
        'cs.NE': 'category-ne',
        'stat.ML': 'category-stat'
    }
    return category_map.get(category_code, 'category-default')


def create_paper_card(paper: dict) -> Article:
    """Create a card component for a single paper"""
    # Truncate authors list if too long
    authors = paper.get('authors', [])
    if len(authors) > 3:
        author_text = f"{', '.join(authors[:3])} et al."
    else:
        author_text = ', '.join(authors)
    
    # Create category badges with proper names and colors
    categories = paper.get('categories', [])
    category_badges = []
    for cat in categories[:3]:  # Limit to 3 categories
        display_name = get_category_display_name(cat)
        css_class = f"category-badge {get_category_css_class(cat)}"
        category_badges.append(Span(display_name, cls=css_class))
    
    # Extract arXiv ID for link
    arxiv_url = paper.get('arxiv_id', '')
    if 'arxiv.org' in arxiv_url:
        arxiv_link = arxiv_url
    else:
        arxiv_link = f"https://arxiv.org/abs/{arxiv_url}"
    
    return Article(
        H3(paper.get('title', 'Untitled'), cls="paper-title"),
        P(author_text, cls="paper-authors"),
        P(paper.get('abstract', 'No abstract available'), cls="paper-abstract"),
        Div(
            *category_badges,
            style="margin-bottom: 1rem;"
        ),
        Div(
            Span(paper.get('published_date_str', 'Unknown date'), cls="paper-date"),
            A("View on arXiv", href=arxiv_link, target="_blank", cls="arxiv-btn"),
            cls="paper-meta"
        ),
        cls="paper-card"
    )


def create_stats_section(total_papers: int, all_papers_count: int, categories_count: int, 
                        cache_age_minutes: int, category: str = None) -> Section:
    """Create the stats section with glittery header"""
    return Section(
        Div(
            Div("🤖", cls="header-icon"),
            H2(
                Span("Daily AI Research Feed", cls="glitter-text")
            ),
            Div(
                Span("✨", cls="sparkle"),
                Span("💫", cls="sparkle"), 
                Span("⭐", cls="sparkle"),
                Span("✨", cls="sparkle"),
                Span("🌟", cls="sparkle"),
                Span("💫", cls="sparkle"),
                cls="floating-sparkles"
            ),
            Div(
                Div(
                    Span(str(total_papers), cls="stat-number"),
                    Div("📄 Papers", cls="stat-label"),
                    cls="stat-item"
                ),
                Div(
                    Span(str(categories_count), cls="stat-number"),
                    Div("🏷️ Categories", cls="stat-label"),
                    cls="stat-item"
                ) if categories_count > 1 else None,
                Div(
                    Span(f"{cache_age_minutes}m", cls="stat-number"),
                    Div("🕒 Cache Age", cls="stat-label"),
                    cls="stat-item"
                ) if cache_age_minutes >= 0 else None,
                cls="stats-grid"
            ),
            P(f"{'🔍 ' + get_category_display_name(category) if category and category != 'all' else '🌟 Latest from arXiv'}"),
            A("🔄 Refresh", href="/refresh", role="button", cls="refresh-btn"),
            cls="stats-content"
        ),
        cls="stats-section"
    )


def create_empty_stats_section() -> Section:
    """Create stats section for empty state"""
    return Section(
        Div(
            Div("🤖", cls="header-icon"),
            H2(
                Span("Daily AI Research Feed", cls="glitter-text")
            ),
            Div(
                Span("✨", cls="sparkle"),
                Span("💫", cls="sparkle"), 
                Span("⭐", cls="sparkle"),
                Span("✨", cls="sparkle"),
                Span("🌟", cls="sparkle"),
                Span("💫", cls="sparkle"),
                cls="floating-sparkles"
            ),
            Div(
                Div(
                    Span("0", cls="stat-number"),
                    Div("📄 Papers", cls="stat-label"),
                    cls="stat-item"
                ),
                cls="stats-grid"
            ),
            P("🚀 Initialize your collection"),
            A("🔄 Fetch Papers", href="/refresh", role="button", cls="refresh-btn"),
            cls="stats-content"
        ),
        cls="stats-section"
    )


def create_filter_section(categories: set, current_category: str = None) -> Section:
    """Create the category filter section"""
    # Create filter badges - limit to main categories only
    main_categories = ['cs.CL', 'cs.CV', 'cs.AI']  # NLP, Computer Vision, AI
    
    filter_badges = [
        A("All Categories", href="/", 
          cls=f"filter-badge {'active' if not current_category or current_category == 'all' else ''}")
    ]
    
    # Add only the main categories that exist in our papers
    for cat in main_categories:
        if cat in categories:  # Only show if we have papers in this category
            display_name = get_category_display_name(cat)
            is_active = current_category == cat
            filter_badges.append(
                A(display_name, href=f"/?category={cat}", 
                  cls=f"filter-badge {'active' if is_active else ''}")
            )
    
    return Section(
        Div("Research Categories", cls="filter-title"),
        Div(*filter_badges, cls="filter-badges"),
        cls="filter-section"
    )


def create_empty_papers_message() -> Div:
    """Create message for when no papers are found in category"""
    return Div(
        H3("No Research Papers Available"),
        P("No papers found in the selected category. Try a different filter or refresh the collection."),
        style="text-align: center; padding: 2rem; color: var(--text-muted);"
    )
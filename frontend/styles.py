"""
Frontend Styles - CSS styling for the Daily AI Research Feed
"""
from fasthtml.common import Style


def get_app_styles() -> Style:
    """Get all CSS styles for the application"""
    return Style("""
    :root {
        --card-bg: #ffffff;
        --card-border: #e5e7eb;
        --text-primary: #1f2937;
        --text-secondary: #6b7280;
        --text-muted: #9ca3af;
        --accent-blue: #3b82f6;
        --accent-blue-hover: #2563eb;
        --accent-green: #10b981;
        --accent-purple: #8b5cf6;
        --accent-orange: #f59e0b;
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }
    
    [data-theme="dark"] {
        --card-bg: #1f2937;
        --card-border: #374151;
        --text-primary: #f9fafb;
        --text-secondary: #d1d5db;
        --text-muted: #9ca3af;
    }
    
    .paper-card {
        transition: all 0.2s ease-in-out;
        border: 1px solid var(--card-border);
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        background: var(--card-bg);
        box-shadow: var(--shadow-sm);
    }
    .paper-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent-blue);
    }
    .paper-title {
        font-size: 1.125rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        line-height: 1.4;
        color: var(--text-primary);
    }
    .paper-authors {
        font-size: 0.875rem;
        color: var(--text-secondary);
        margin-bottom: 0.75rem;
        font-weight: 500;
    }
    .paper-abstract {
        font-size: 0.9rem;
        line-height: 1.6;
        margin-bottom: 1.25rem;
        color: var(--text-secondary);
        text-align: justify;
    }
    .category-badge {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 500;
        padding: 0.25rem 0.75rem;
        margin: 0.125rem 0.5rem 0.125rem 0;
        border-radius: 9999px;
        color: white;
    }
    .category-ai { background-color: var(--accent-blue); }
    .category-ml { background-color: var(--accent-green); }
    .category-cv { background-color: var(--accent-purple); }
    .category-cl { background-color: var(--accent-orange); }
    .category-ne { background-color: #ef4444; }
    .category-stat { background-color: #8b5cf6; }
    .category-default { background-color: var(--text-muted); }
    
    .paper-meta {
        border-top: 1px solid var(--card-border);
        padding-top: 1rem;
        margin-top: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.75rem;
    }
    .paper-date {
        font-size: 0.8rem;
        color: var(--text-muted);
        font-weight: 500;
    }
    .arxiv-btn {
        font-size: 0.875rem;
        padding: 0.5rem 1rem;
        background-color: var(--accent-blue);
        color: white;
        text-decoration: none;
        border-radius: 0.5rem;
        font-weight: 500;
        transition: background-color 0.2s;
        border: none;
    }
    .arxiv-btn:hover {
        background-color: var(--accent-blue-hover);
        color: white;
        text-decoration: none;
    }
    .stats-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 0.75rem;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: var(--shadow-lg);
        color: white;
        position: relative;
        overflow: hidden;
    }
    .stats-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a" cx="50%" cy="50%"><stop offset="0%" stop-color="%23ffffff" stop-opacity="0.1"/><stop offset="100%" stop-color="%23ffffff" stop-opacity="0"/></radialGradient></defs><circle cx="200" cy="200" r="100" fill="url(%23a)"/><circle cx="800" cy="300" r="150" fill="url(%23a)"/><circle cx="400" cy="700" r="120" fill="url(%23a)"/><circle cx="700" cy="800" r="80" fill="url(%23a)"/></svg>');
        background-size: cover;
        opacity: 0.3;
    }
    .stats-content {
        position: relative;
        z-index: 1;
    }
    .header-icon {
        width: 80px;
        height: 80px;
        margin: 0 auto 1.5rem;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        backdrop-filter: blur(10px);
    }
    .stats-section h2 {
        color: white;
        margin-bottom: 0.75rem;
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(45deg, #fff, #f0f8ff, #fff, #e6f3ff, #fff);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: shimmer 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.5);
        position: relative;
    }
    
    @keyframes shimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .glitter-text {
        position: relative;
        display: inline-block;
    }
    
    .glitter-text::before {
        content: '✨';
        position: absolute;
        top: -10px;
        left: -20px;
        font-size: 1.2rem;
        animation: sparkle1 2s ease-in-out infinite;
    }
    
    .glitter-text::after {
        content: '⭐';
        position: absolute;
        top: -15px;
        right: -25px;
        font-size: 1rem;
        animation: sparkle2 2.5s ease-in-out infinite;
    }
    
    @keyframes sparkle1 {
        0%, 100% { 
            opacity: 0;
            transform: scale(0.5) rotate(0deg);
        }
        50% { 
            opacity: 1;
            transform: scale(1) rotate(180deg);
        }
    }
    
    @keyframes sparkle2 {
        0%, 100% { 
            opacity: 0;
            transform: scale(0.3) rotate(0deg);
        }
        60% { 
            opacity: 1;
            transform: scale(1.2) rotate(-180deg);
        }
    }
    
    .floating-sparkles {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        overflow: hidden;
    }
    
    .sparkle {
        position: absolute;
        color: rgba(255, 255, 255, 0.8);
        font-size: 1rem;
        animation: float 4s ease-in-out infinite;
    }
    
    .sparkle:nth-child(1) { left: 10%; animation-delay: 0s; }
    .sparkle:nth-child(2) { left: 20%; animation-delay: 0.5s; }
    .sparkle:nth-child(3) { left: 30%; animation-delay: 1s; }
    .sparkle:nth-child(4) { left: 70%; animation-delay: 1.5s; }
    .sparkle:nth-child(5) { left: 80%; animation-delay: 2s; }
    .sparkle:nth-child(6) { left: 90%; animation-delay: 2.5s; }
    
    @keyframes float {
        0%, 100% { 
            transform: translateY(100px) scale(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        50% { 
            transform: translateY(-20px) scale(1);
            opacity: 1;
        }
    }
    
    /* Style the main H1 title */
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #667eea 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: titleShimmer 4s ease-in-out infinite;
        text-align: center;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 2rem;
        text-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
        position: relative;
    }
    
    h1::before {
        content: '🚀';
        position: absolute;
        left: -50px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.5rem;
        animation: rocketBounce 3s ease-in-out infinite;
    }
    
    h1::after {
        content: '⚡';
        position: absolute;
        right: -50px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.5rem;
        animation: lightningFlash 2s ease-in-out infinite;
    }
    
    @keyframes titleShimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes rocketBounce {
        0%, 100% { transform: translateY(-50%) scale(1); }
        50% { transform: translateY(-70%) scale(1.1); }
    }
    
    @keyframes lightningFlash {
        0%, 100% { opacity: 0.7; transform: translateY(-50%) rotate(0deg); }
        50% { opacity: 1; transform: translateY(-50%) rotate(10deg); }
    }
    
    .stats-section p {
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }
    .refresh-btn {
        background-color: rgba(255, 255, 255, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.3);
        color: white;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border-radius: 50px;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    .refresh-btn:hover {
        background-color: rgba(255, 255, 255, 0.3);
        border-color: rgba(255, 255, 255, 0.5);
        color: white;
        transform: translateY(-2px);
    }
    .grid-container {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        margin-top: 2rem;
    }
    .filter-section {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--shadow-sm);
    }
    .filter-title {
        font-size: 1rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    .filter-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    .filter-badge {
        display: inline-block;
        font-size: 0.875rem;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: 9999px;
        text-decoration: none;
        transition: all 0.2s;
        border: 2px solid var(--card-border);
        background: var(--card-bg);
        color: var(--text-secondary);
    }
    .filter-badge:hover {
        border-color: var(--accent-blue);
        color: var(--accent-blue);
        text-decoration: none;
    }
    .filter-badge.active {
        background-color: var(--accent-blue);
        border-color: var(--accent-blue);
        color: white;
    }
    .filter-badge.active:hover {
        background-color: var(--accent-blue-hover);
        border-color: var(--accent-blue-hover);
        color: white;
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    .stat-item {
        text-align: center;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        display: block;
        line-height: 1;
    }
    .stat-label {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.8);
        margin-top: 0.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.25rem;
    }
    @media (max-width: 768px) {
        .paper-meta {
            flex-direction: column;
            align-items: flex-start;
        }
        h1 {
            font-size: 2rem;
        }
        h1::before,
        h1::after {
            display: none;
        }
    }
""")
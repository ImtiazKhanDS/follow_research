# Use the official uv image that includes Python
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    UV_SYSTEM_PYTHON=1

# Create non-root user first
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app

# Switch to non-root user
USER app

# Copy uv project files first for better caching
COPY --chown=app:app pyproject.toml uv.lock ./

# Install dependencies using uv with system Python
RUN uv sync --frozen --no-dev

# Copy application code
COPY --chown=app:app . .

# Expose port
EXPOSE 5001

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD uv run python -c "import requests; requests.get('http://localhost:5001/debug', timeout=10)"

# Run the application
CMD ["uv", "run", "python", "app.py"]
#!/usr/bin/env python3
import yaml
import os
from pathlib import Path
import requests
import json

def fetch_sefaria_text(ref):
    """Fetch text from Sefaria API"""
    try:
        url = f"https://www.sefaria.org/api/texts/{ref}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch {ref}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching {ref}: {e}")
        return None

def generate_ai_content(text, title):
    """Generate enhanced content using AI"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return f"Basic summary for {title}: This text explores fundamental concepts in Jewish tradition."

    try:
        import openai
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant specializing in Jewish texts and traditions. Provide concise, accurate summaries."},
                {"role": "user", "content": f"Provide a brief summary of the content from {title}. Here's a sample text: {text[:1000] if text else 'No text available'}"}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI generation failed: {e}")
        return f"AI summary for {title} (error occurred)"

def generate_content():
    # Load data
    with open('_data/books.yml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # Create _pages directory if it doesn't exist
    pages_dir = Path('_pages')
    pages_dir.mkdir(exist_ok=True)

    # Generate Torah pages
    for book in data['torah_books']:
        filename = f"{book['name'].lower()}.md"

        # Fetch from Sefaria
        sefaria_data = fetch_sefaria_text(f"{book['name']}.1")
        fetched_text = ""
        if sefaria_data and 'text' in sefaria_data:
            # Get first few verses
            text_content = sefaria_data['text']
            if isinstance(text_content, list):
                fetched_text = ' '.join(text_content[:3])  # First 3 verses
            else:
                fetched_text = str(text_content)[:500]

        # Generate AI content
        ai_summary = generate_ai_content(fetched_text, book['name'])

        content = f"""---
layout: page
title: {book['name']}
---

# {book['name']} ({book['hebrew']})

{book['description']}

## AI-Generated Summary

{ai_summary}

## Sample Text from Sefaria

{fetched_text}

## Overview

This page contains information about the book of {book['name']}.

## Chapters

- Chapter 1
- Chapter 2
- Chapter 3
- (And so on...)

## Key Themes

- Theme 1
- Theme 2
- Theme 3

## Study Resources

- [Commentary](commentary/)
- [Audio Lectures](audio/)
- [Discussion Questions](questions/)
"""
        with open(pages_dir / filename, 'w', encoding='utf-8') as f:
            f.write(content)

    # Generate Talmud pages
    for tractate in data['talmud_tractates']:
        filename = f"{tractate['name'].lower()}.md"

        # Fetch from Sefaria (try first daf)
        sefaria_data = fetch_sefaria_text(f"{tractate['name']}.2a")
        fetched_text = ""
        if sefaria_data and 'text' in sefaria_data:
            text_content = sefaria_data['text']
            if isinstance(text_content, str):
                fetched_text = text_content[:500]
            elif isinstance(text_content, list):
                fetched_text = ' '.join(str(t) for t in text_content[:2])[:500]

        # Generate AI content
        ai_summary = generate_ai_content(fetched_text, tractate['name'])

        content = f"""---
layout: page
title: {tractate['name']}
---

# Tractate {tractate['name']}

{tractate['description']}

## AI-Generated Summary

{ai_summary}

## Sample Text from Sefaria

{fetched_text}

## Overview

This page contains information about Tractate {tractate['name']}.

## Dafim (Pages)

- Daf 1
- Daf 2
- Daf 3
- (And so on...)

## Key Topics

- Topic 1
- Topic 2
- Topic 3

## Study Resources

- [Commentary](commentary/)
- [Audio Lectures](audio/)
- [Discussion Questions](questions/)
"""
        with open(pages_dir / filename, 'w', encoding='utf-8') as f:
            f.write(content)

    print("Content generation completed!")

if __name__ == "__main__":
    generate_content()
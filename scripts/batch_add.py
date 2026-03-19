#!/usr/bin/env python3
"""
Bulk import design ideas from a JSON file or stdin.
Useful after research sessions to add multiple ideas at once.
"""

import argparse
import json
import sys
from pathlib import Path
from _shared import get_supabase_client, print_idea


def batch_add(file_path: str = None):
    """Load design ideas from JSON file and add them to the database."""
    supabase = get_supabase_client()
    
    try:
        # Read JSON from file or stdin
        if file_path:
            if not Path(file_path).exists():
                print(f"❌ File not found: {file_path}")
                return False
            with open(file_path) as f:
                ideas = json.load(f)
        else:
            # Read from stdin
            print("Reading JSON from stdin (or pipe your file)...")
            ideas = json.load(sys.stdin)
        
        if not isinstance(ideas, list):
            print("❌ JSON must be a list of design ideas")
            return False
        
        print(f"\n📥 Importing {len(ideas)} design idea(s)...")
        
        added = 0
        for i, idea in enumerate(ideas, 1):
            # Validate required fields
            if not all(k in idea for k in ["title", "niche", "description", "audience"]):
                print(f"⚠️  Skipping idea {i}: missing required fields (title, niche, description, audience)")
                continue
            
            try:
                response = supabase.table("design_ideas").insert(idea).execute()
                if response.data:
                    print(f"✅ [{i}/{len(ideas)}] Added: {idea['title']}")
                    added += 1
            except Exception as e:
                print(f"❌ [{i}/{len(ideas)}] Failed to add {idea.get('title', 'Unknown')}: {str(e)}")
        
        print(f"\n📊 Summary: {added}/{len(ideas)} ideas imported successfully")
        return True
    except json.JSONDecodeError:
        print("❌ Invalid JSON format")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def print_example():
    """Print example JSON format."""
    example = [
        {
            "title": "No Shelf Control",
            "niche": "Bookish Humor",
            "description": "Clever pun on self-control for readers who can't stop buying books",
            "audience": "book lovers, introverts, TBR hoarders",
            "research": "Wordplay designs sell well. Puns increase recall. Redbubble searches: high volume",
            "text_to_image_prompt": "Minimalist text design in bold sans-serif: 'No Shelf Control' with stacked books in subtle background",
            "products": ["t-shirt", "sticker"],
            "notes": "Consider pastel colors for broader appeal"
        },
        {
            "title": "This Anxiety is Chronic But This Book is Iconic",
            "niche": "Mental Health + Books",
            "description": "Mental health reference combined with book pun using rhyming text",
            "audience": "anxious readers, BookTok community, mental health advocates",
            "research": "Mental health merch underserved. Rhyming increases memorability.",
            "text_to_image_prompt": "Modern sans-serif design: text in contrasting colors on light background",
            "products": ["t-shirt", "sticker", "mug"],
            "notes": "Pink or teal color scheme resonates with target audience"
        }
    ]
    print("\n📋 Example JSON format:\n")
    print(json.dumps(example, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Bulk import design ideas from JSON file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # From file
  python3 batch_add.py designs.json
  
  # From stdin
  cat designs.json | python3 batch_add.py
  
  # Print example format
  python3 batch_add.py --example
        """
    )
    parser.add_argument("file", nargs="?", help="JSON file with design ideas")
    parser.add_argument("--example", action="store_true", help="Print example JSON format")
    
    args = parser.parse_args()
    
    if args.example:
        print_example()
        sys.exit(0)
    
    success = batch_add(args.file)
    
    sys.exit(0 if success else 1)

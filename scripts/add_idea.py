#!/usr/bin/env python3
"""
Add a single design idea to the database.
"""

import argparse
import json
import sys
from _shared import get_supabase_client, print_idea


def add_idea(
    title: str,
    niche: str,
    audience: str,
    description: str,
    research: str = None,
    prompt: str = None,
    products: list = None,
    notes: str = None,
):
    """Add a new design idea to the database."""
    supabase = get_supabase_client()
    
    idea = {
        "title": title,
        "niche": niche,
        "description": description,
        "audience": audience,
    }
    
    if research:
        idea["research"] = research
    if prompt:
        idea["text_to_image_prompt"] = prompt
    if products:
        idea["products"] = products if isinstance(products, list) else [p.strip() for p in products.split(",")]
    if notes:
        idea["notes"] = notes
    
    try:
        response = supabase.table("design_ideas").insert(idea).execute()
        if response.data:
            print("✅ Design idea added!")
            print_idea(response.data[0])
            return True
        else:
            print("❌ Failed to add design idea")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a design idea")
    parser.add_argument("--title", required=True, help="Design title")
    parser.add_argument("--niche", required=True, help="Niche/category")
    parser.add_argument("--audience", required=True, help="Target audience")
    parser.add_argument("--description", required=True, help="Short description")
    parser.add_argument("--research", help="Market research notes")
    parser.add_argument("--prompt", help="Text-to-image generator prompt")
    parser.add_argument("--products", help="Comma-separated products (t-shirt, sticker, mug)")
    parser.add_argument("--notes", help="Additional notes")
    
    args = parser.parse_args()
    
    products = None
    if args.products:
        products = [p.strip() for p in args.products.split(",")]
    
    success = add_idea(
        title=args.title,
        niche=args.niche,
        audience=args.audience,
        description=args.description,
        research=args.research,
        prompt=args.prompt,
        products=products,
        notes=args.notes,
    )
    
    sys.exit(0 if success else 1)

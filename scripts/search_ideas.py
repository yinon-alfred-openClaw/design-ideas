#!/usr/bin/env python3
"""
Search design ideas by niche, audience, or keywords.
"""

import argparse
import sys
from _shared import get_supabase_client, format_table, print_idea


def search_ideas(niche: str = None, audience: str = None, keyword: str = None, verbose: bool = False):
    """Search design ideas by various criteria."""
    supabase = get_supabase_client()
    
    try:
        query = supabase.table("design_ideas").select("*").order("created_at", desc=True)
        
        if niche:
            query = query.eq("niche", niche)
        
        response = query.execute()
        ideas = response.data
        
        # Client-side filtering for audience and keyword
        if audience:
            ideas = [i for i in ideas if audience.lower() in i.get("audience", "").lower()]
        
        if keyword:
            keyword_lower = keyword.lower()
            ideas = [
                i for i in ideas
                if keyword_lower in i.get("title", "").lower()
                or keyword_lower in i.get("description", "").lower()
                or keyword_lower in i.get("research", "").lower()
            ]
        
        if not ideas:
            criteria = []
            if niche:
                criteria.append(f"niche: {niche}")
            if audience:
                criteria.append(f"audience: {audience}")
            if keyword:
                criteria.append(f"keyword: {keyword}")
            
            print(f"No design ideas found matching: {', '.join(criteria)}")
            return
        
        print(f"\n🔍 Found {len(ideas)} matching design idea(s)")
        if niche:
            print(f"   Niche: {niche}")
        if audience:
            print(f"   Audience: {audience}")
        if keyword:
            print(f"   Keyword: {keyword}")
        
        if verbose:
            for idea in ideas:
                print_idea(idea)
        else:
            format_table(ideas)
        
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search design ideas")
    parser.add_argument("--niche", help="Filter by niche")
    parser.add_argument("--audience", help="Filter by audience keywords")
    parser.add_argument("--keyword", help="Search by keyword in title/description")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    success = search_ideas(
        niche=args.niche,
        audience=args.audience,
        keyword=args.keyword,
        verbose=args.verbose,
    )
    
    sys.exit(0 if success else 1)

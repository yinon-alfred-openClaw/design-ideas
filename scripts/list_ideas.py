#!/usr/bin/env python3
"""
List all design ideas or filter by niche.
"""

import argparse
import sys
from _shared import get_supabase_client, format_table, print_idea


def list_ideas(niche: str = None, limit: int = None, verbose: bool = False):
    """List design ideas from the database."""
    supabase = get_supabase_client()
    
    try:
        query = supabase.table("design_ideas").select("*").order("created_at", desc=True)
        
        if niche:
            query = query.eq("niche", niche)
        
        if limit:
            query = query.limit(limit)
        
        response = query.execute()
        ideas = response.data
        
        if not ideas:
            print(f"No design ideas found{f' for niche: {niche}' if niche else ''}.")
            return
        
        print(f"\n📚 Found {len(ideas)} design idea(s){f' in niche: {niche}' if niche else ''}")
        
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
    parser = argparse.ArgumentParser(description="List design ideas")
    parser.add_argument("--niche", help="Filter by niche")
    parser.add_argument("--limit", type=int, help="Limit number of results")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    success = list_ideas(
        niche=args.niche,
        limit=args.limit,
        verbose=args.verbose,
    )
    
    sys.exit(0 if success else 1)

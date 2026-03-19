#!/usr/bin/env python3
"""
Get a random design idea from the database.
Useful for inspiration when you need ideas!
"""

import argparse
import random
import sys
from _shared import get_supabase_client, print_idea


def get_random_idea(niche: str = None):
    """Get a random design idea, optionally filtered by niche."""
    supabase = get_supabase_client()
    
    try:
        query = supabase.table("design_ideas").select("*")
        
        if niche:
            query = query.eq("niche", niche)
        
        response = query.execute()
        ideas = response.data
        
        if not ideas:
            print(f"No ideas found{f' for niche: {niche}' if niche else ''}.")
            return False
        
        idea = random.choice(ideas)
        
        print("\n🎲 Random design idea:")
        print_idea(idea)
        
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get a random design idea")
    parser.add_argument("--niche", help="Filter by niche")
    
    args = parser.parse_args()
    
    success = get_random_idea(niche=args.niche)
    
    sys.exit(0 if success else 1)

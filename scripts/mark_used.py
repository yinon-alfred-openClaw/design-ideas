#!/usr/bin/env python3
"""
Mark a design idea as used by deleting it from the database.
Use this after you've created and uploaded a design.
"""

import argparse
import sys
from _shared import get_supabase_client


def mark_used(idea_id: str):
    """Mark a design idea as used (delete it)."""
    supabase = get_supabase_client()
    
    try:
        # First, fetch the idea to display it before deletion
        fetch_response = supabase.table("design_ideas").select("*").eq("id", idea_id).execute()
        
        if not fetch_response.data:
            print(f"❌ Design idea with ID {idea_id} not found.")
            return False
        
        idea = fetch_response.data[0]
        print(f"📌 Marking as used: {idea['title']}")
        
        # Delete the idea
        delete_response = supabase.table("design_ideas").delete().eq("id", idea_id).execute()
        
        print(f"✅ Design idea '{idea['title']}' has been removed from your pool.")
        print(f"   (It was in the '{idea['niche']}' niche)")
        
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mark a design idea as used (delete it)")
    parser.add_argument("--id", required=True, help="UUID of the design idea to delete")
    
    args = parser.parse_args()
    
    success = mark_used(args.id)
    
    sys.exit(0 if success else 1)

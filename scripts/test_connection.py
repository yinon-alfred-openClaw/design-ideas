#!/usr/bin/env python3
"""
Test the Supabase connection and verify the design_ideas table exists.
"""

import sys
from _shared import get_supabase_client, table_exists


def test_connection():
    """Test Supabase connection and table setup."""
    print("🧪 Testing Supabase connection...\n")
    
    try:
        supabase = get_supabase_client()
        print("✅ Connected to Supabase")
        
        # Check if design_ideas table exists
        if table_exists(supabase, "design_ideas"):
            print("✅ 'design_ideas' table exists")
            
            # Count rows
            response = supabase.table("design_ideas").select("id").execute()
            count = len(response.data) if response.data else 0
            print(f"✅ Table has {count} design idea(s)")
            
            return True
        else:
            print("❌ 'design_ideas' table not found")
            print("\nTo create the table, run:")
            print("  python3 scripts/init_db.py")
            print("\nOr run the migration via Supabase CLI:")
            print("  npx supabase db push")
            
            return False
    
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        print("\nMake sure:")
        print("  1. Supabase credentials are in ~/.openclaw/workspace/memory/supabase-creds.json")
        print("  2. File contains: {\"url\": \"...\", \"key\": \"...\"}")
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)

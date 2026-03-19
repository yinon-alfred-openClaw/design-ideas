#!/usr/bin/env python3
"""
Shared utilities for design-ideas skill.
Handles Supabase connection and common operations.
"""

import json
import os
import sys
from pathlib import Path

try:
    from supabase import create_client
    from supabase.client import Client
except ImportError:
    print("ERROR: supabase-py not installed. Install with: pip3 install supabase")
    sys.exit(1)


def get_supabase_client() -> Client:
    """Initialize Supabase client from credentials file."""
    creds_path = Path.home() / ".openclaw/workspace/memory/supabase-creds.json"
    
    if not creds_path.exists():
        print(f"ERROR: Supabase credentials file not found at {creds_path}")
        print("Expected format: {\"url\": \"...\", \"key\": \"...\"}")
        sys.exit(1)
    
    with open(creds_path) as f:
        creds = json.load(f)
    
    url = creds.get("url")
    key = creds.get("key")
    
    if not url or not key:
        print("ERROR: Missing 'url' or 'key' in Supabase credentials file")
        sys.exit(1)
    
    return create_client(url, key)


def table_exists(supabase: Client, table_name: str) -> bool:
    """Check if a table exists in the database."""
    try:
        supabase.table(table_name).select("id").limit(1).execute()
        return True
    except Exception:
        return False


def print_idea(idea: dict):
    """Pretty-print a design idea."""
    print(f"\n📌 {idea['title']}")
    print(f"   Niche: {idea['niche']}")
    print(f"   Audience: {idea['audience']}")
    print(f"   Description: {idea['description']}")
    if idea.get('research'):
        print(f"   Research: {idea['research']}")
    if idea.get('products'):
        print(f"   Products: {', '.join(idea['products'])}")
    if idea.get('notes'):
        print(f"   Notes: {idea['notes']}")
    print(f"   Created: {idea['created_at']}")
    print(f"   ID: {idea['id']}")


def format_table(ideas: list):
    """Format ideas as a simple table."""
    if not ideas:
        print("No ideas found.")
        return
    
    print("\n" + "=" * 120)
    print(f"{'Title':<30} {'Niche':<20} {'Audience':<30} {'Products':<20}")
    print("=" * 120)
    for idea in ideas:
        products = ", ".join(idea.get('products', [])[:2]) if idea.get('products') else "-"
        print(f"{idea['title']:<30} {idea['niche']:<20} {idea['audience']:<30} {products:<20}")
    print("=" * 120)

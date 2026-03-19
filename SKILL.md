---
name: design-ideas
description: Manage design ideas for merchandise with Supabase backend. Use when: (1) need design inspiration for merch (t-shirt, sticker, mug), (2) organizing design research by niche (Dark Romance, Mental Health, Bookish Humor, etc.), (3) bulk-importing ideas from research sessions, (4) tracking which designs have been created and removing them from the pool, (5) searching design ideas by niche, audience, or keyword
---

# Design Ideas Skill

Your personal **design idea repository** for merch design workflows. Store research, audience data, and text-to-image prompts in Supabase. Get inspired, create designs, mark them as used.

## Quick Start

### 1. Initial Setup (First Time)

See `references/setup.md` for:
- Creating the database table
- Testing the connection
- Loading 14 pre-researched initial ideas

### 2. Get Design Ideas

```bash
# Random idea for inspiration
python3 scripts/random_idea.py

# From specific niche
python3 scripts/random_idea.py --niche "Dark Romance"

# List all ideas
python3 scripts/list_ideas.py

# Search by keyword
python3 scripts/search_ideas.py --keyword "anxiety"
```

### 3. Add New Ideas

```bash
# Single idea
python3 scripts/add_idea.py \
  --title "No Shelf Control" \
  --niche "Bookish Humor" \
  --audience "book lovers, introverts" \
  --description "Clever pun on self-control"

# Bulk import from JSON
python3 scripts/batch_add.py research_findings.json
```

### 4. Track Progress

```bash
# When you've created a design, mark it as used
python3 scripts/mark_used.py --id <uuid>
```

---

## Database Schema

**Table: `design_ideas`**

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| title | TEXT | Design name |
| niche | TEXT | Category (e.g., "Dark Romance", "Bookish Humor") |
| description | TEXT | 1-2 sentence description |
| audience | TEXT | Target audience |
| research | TEXT | Market research notes |
| text_to_image_prompt | TEXT | Prompt for DALL-E/Midjourney |
| products | TEXT[] | Suitable products (t-shirt, sticker, mug) |
| notes | TEXT | Additional context |
| created_at | TIMESTAMPTZ | Timestamp |
| updated_at | TIMESTAMPTZ | Timestamp |

---

## All Commands

### Explore Ideas

```bash
# List all
python3 scripts/list_ideas.py

# Verbose output (full details)
python3 scripts/list_ideas.py --verbose

# Filter by niche
python3 scripts/list_ideas.py --niche "Mental Health"

# Limit results
python3 scripts/list_ideas.py --limit 10
```

### Search & Discover

```bash
# Random idea (any niche)
python3 scripts/random_idea.py

# Random from specific niche
python3 scripts/random_idea.py --niche "Dark Romance"

# Search by niche
python3 scripts/search_ideas.py --niche "Fandom In-Jokes"

# Search by audience
python3 scripts/search_ideas.py --audience "BookTok"

# Search by keyword
python3 scripts/search_ideas.py --keyword "spicy" --verbose
```

### Add & Manage Ideas

```bash
# Add single idea
python3 scripts/add_idea.py \
  --title "Title" \
  --niche "Niche" \
  --audience "Audience" \
  --description "Description" \
  --research "Why this works" \
  --prompt "Text-to-image prompt" \
  --products "t-shirt,sticker"

# Bulk import
python3 scripts/batch_add.py ideas.json

# Print example format
python3 scripts/batch_add.py --example

# Mark design as used (delete from pool)
python3 scripts/mark_used.py --id <uuid>
```

---

## Pre-Researched Ideas

**14 initial ideas** included covering:
- Bookish Humor (wordplay, puns)
- Mental Health + Books (anxiety, coping)
- Dark Humor (nihilism, sarcasm)
- Dark Romance (spicy books, morally grey)
- Fandom In-Jokes (trope references)
- Relatable Problems (TBR piles, book guilt)

Each includes:
- Description and target audience
- Market research notes
- Text-to-image prompts
- Recommended products

---

## Bulk Import Format

Add multiple ideas from JSON file. See `references/json-format.md` for complete format guide.

**Example:**
```json
[
  {
    "title": "No Shelf Control",
    "niche": "Bookish Humor",
    "description": "Pun on self-control for readers",
    "audience": "book lovers, introverts",
    "research": "Wordplay designs sell well",
    "text_to_image_prompt": "Minimalist text design...",
    "products": ["t-shirt", "sticker"]
  }
]
```

---

## Workflow

1. **Inspiration:** `python3 scripts/random_idea.py --niche "Dark Romance"`
2. **Copy prompt:** Take `text_to_image_prompt` field
3. **Generate:** Paste into DALL-E or Midjourney
4. **Design:** Create, refine, upload to Redbubble
5. **Cleanup:** `python3 scripts/mark_used.py --id <uuid>`
6. **Repeat:** Get next idea

---

## For More Details

- **Setup & usage guide**: See `references/setup.md`
- **JSON bulk import format**: See `references/json-format.md`
- **Database definition**: See `assets/schema.sql`
- **Initial 14 ideas**: See `assets/initial_ideas.json`

---

## Tips

1. **Be specific with prompts** — Text-to-image prompts should be detailed enough to paste directly into generators
2. **Track research** — Document why designs work and who buys them
3. **Group by niche** — Organize ideas by category for easy discovery
4. **Refresh regularly** — Add new ideas after research sessions
5. **Mark as used** — Remove designs you've already created to keep the pool fresh

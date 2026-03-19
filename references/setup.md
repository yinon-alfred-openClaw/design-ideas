# Setup & Usage Guide

## Initial Setup (First Time)

### 1. Create the Database Table

Create the `design_ideas` table in your Supabase database. Choose one method:

**Option A: Supabase Dashboard (Easiest)**
1. Go to https://app.supabase.com/
2. Open your project
3. Click **SQL Editor**
4. Create new query and paste the SQL from `assets/schema.sql`
5. Click **Run**

**Option B: Supabase CLI**
1. Copy schema to migrations: `cp assets/schema.sql supabase/migrations/20260319_design_ideas.sql`
2. Push: `npx supabase db push`

### 2. Test Connection

```bash
cd skills/design-ideas
python3 scripts/test_connection.py
```

Expected output:
```
✅ Connected to Supabase
✅ 'design_ideas' table exists
✅ Table has 0 design idea(s)
```

### 3. Load Initial Ideas

```bash
python3 scripts/batch_add.py assets/initial_ideas.json
```

Expected: 14 design ideas imported successfully.

---

## Daily Usage

### Get Design Inspiration

```bash
# Random idea from any niche
python3 scripts/random_idea.py

# Random idea from specific niche
python3 scripts/random_idea.py --niche "Dark Romance"

# Get 5 random ideas
for i in {1..5}; do python3 scripts/random_idea.py --niche "Dark Romance"; done
```

### List & Search

```bash
# List all ideas
python3 scripts/list_ideas.py

# Filter by niche
python3 scripts/list_ideas.py --niche "Mental Health"

# Verbose output (full details)
python3 scripts/list_ideas.py --verbose

# Search by keyword
python3 scripts/search_ideas.py --keyword "anxiety"

# Search by audience
python3 scripts/search_ideas.py --audience "BookTok"
```

### Add New Ideas

```bash
# Single idea
python3 scripts/add_idea.py \
  --title "No Shelf Control" \
  --niche "Bookish Humor" \
  --audience "book lovers, introverts" \
  --description "Clever pun on self-control for readers"

# Bulk import from file
python3 scripts/batch_add.py my_ideas.json
```

### Mark Idea as Used

After you create and upload a design:

```bash
python3 scripts/mark_used.py --id <uuid>
```

Get the UUID from `python3 scripts/list_ideas.py`

---

## Workflow Example

1. **Get inspiration:** `python3 scripts/random_idea.py --niche "Dark Romance"`
2. **Copy prompt:** Take the `text_to_image_prompt` field
3. **Generate:** Paste into DALL-E/Midjourney
4. **Design:** Create, refine, upload to Redbubble
5. **Cleanup:** `python3 scripts/mark_used.py --id <uuid>`
6. **Repeat:** Get next idea

---

## Bulk Import (Research Sessions)

After research, add multiple ideas at once:

```bash
python3 scripts/batch_add.py research_findings.json
```

JSON format: See `references/json-format.md`

---

## Niches in Database

Track your design ideas by these niches:

- **Bookish Humor** — wordplay, puns, funny book references
- **Mental Health + Books** — anxiety, depression, coping through reading
- **Dark Romance** — spicy books, morally grey characters, trope references
- **Fandom In-Jokes** — series-specific quotes and references
- **Relatable Problems** — TBR piles, book buying guilt, late-night reading
- **Dark Humor** — morbid jokes, nihilism, sarcasm

Or create your own niches as you research.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Table does not exist" | Run Step 1 (Create Database Table) above |
| "Credentials not found" | Ensure `~/.openclaw/workspace/memory/supabase-creds.json` exists with `url` and `key` |
| "supabase-py not installed" | `pip3 install supabase` |
| Scripts fail to run | Make sure you're in `skills/design-ideas/` directory |

---

## File Structure

```
design-ideas/
├── SKILL.md                  # Skill definition
├── scripts/                  # Python CLI tools
│   ├── list_ideas.py
│   ├── random_idea.py
│   ├── search_ideas.py
│   ├── add_idea.py
│   ├── batch_add.py
│   ├── mark_used.py
│   ├── test_connection.py
│   └── _shared.py (helper)
├── references/
│   ├── setup.md              # This file
│   └── json-format.md        # Bulk import format
└── assets/
    ├── initial_ideas.json    # 14 pre-researched ideas
    └── schema.sql            # Database table definition
```

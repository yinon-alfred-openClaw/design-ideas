# JSON Format for Bulk Import

Use this format when bulk-importing design ideas with `batch_add.py`.

## Basic Structure

```json
[
  {
    "title": "Design Title",
    "niche": "Niche Category",
    "description": "Short 1-2 sentence description",
    "audience": "Target audience description",
    "research": "Market research notes",
    "text_to_image_prompt": "Full prompt for DALL-E/Midjourney",
    "products": ["t-shirt", "sticker"],
    "notes": "Optional additional context"
  }
]
```

## Field Descriptions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Design name/title |
| `niche` | string | Yes | Category (e.g., "Dark Romance", "Bookish Humor") |
| `description` | string | Yes | 1-2 sentence overview of the design |
| `audience` | string | No | Target audience ("book lovers, introverts, BookTok") |
| `research` | string | No | Why this design works, competitor notes, market info |
| `text_to_image_prompt` | string | No | Complete prompt for AI image generators |
| `products` | array | No | Suitable products: ["t-shirt", "sticker", "mug", "hoodie", "tote bag"] |
| `notes` | string | No | Any additional context or design notes |

## Complete Example

```json
[
  {
    "title": "No Shelf Control",
    "niche": "Bookish Humor",
    "description": "Clever pun on self-control for readers who can't stop buying books",
    "audience": "book lovers, introverts, TBR hoarders",
    "research": "Wordplay designs sell consistently on Redbubble. Puns increase recall and shareability. High search volume for 'book humor'",
    "text_to_image_prompt": "Minimalist text design: 'No Shelf Control' in bold sans-serif font. Stacked colorful books subtly in background. Light cream background. Clean, readable.",
    "products": ["t-shirt", "sticker", "mug"],
    "notes": "Consider pastel t-shirt colors for broader appeal"
  },
  {
    "title": "This Anxiety is Chronic But This Book is Iconic",
    "niche": "Mental Health + Books",
    "description": "Mental health + book pun using rhyming text",
    "audience": "anxious readers, BookTok, mental health advocates, Gen Z",
    "research": "Underserved niche. Rhyming text increases memorability and social sharing.",
    "text_to_image_prompt": "Modern sans-serif typography: 'This Anxiety is Chronic But This Book is Iconic' in contrasting colors (pink on light background). Subtle spiral or book motifs in corners.",
    "products": ["t-shirt", "sticker"],
    "notes": "High viral potential on TikTok"
  },
  {
    "title": "Reading Because Murder is Wrong",
    "niche": "Dark Humor + Books",
    "description": "Dark humor implying books are escape from darker impulses",
    "audience": "dark humor enthusiasts, true crime fans, readers with twisted wit",
    "research": "Dark humor merch has strong niche following. Book + dark humor combo is underserved.",
    "text_to_image_prompt": "Minimalist text: 'Reading Because Murder is Wrong' in clean sans-serif. Optional: subtle silhouette of reading figure. White/light text on dark shirt.",
    "products": ["t-shirt", "sticker"],
    "notes": "Edgy audience segment"
  }
]
```

## Minimal Example

You can provide just required fields:

```json
[
  {
    "title": "Quick Idea",
    "niche": "Bookish Humor",
    "description": "A design idea",
    "audience": "book lovers"
  }
]
```

## Usage

### From File

```bash
python3 scripts/batch_add.py designs.json
```

### From stdin

```bash
cat designs.json | python3 scripts/batch_add.py
```

### Print Example Format

```bash
python3 scripts/batch_add.py --example
```

## Tips

1. **Be specific with prompts** — The text-to-image prompt should be detailed enough to paste directly into DALL-E or Midjourney
2. **Research context matters** — Why does this design work? Who buys it? What makes it different?
3. **Mark products early** — Not all designs work on all products
4. **Keep titles concise** — But memorable
5. **Validate before import** — Make sure JSON is valid (use a JSON validator)

## Common Niches

- **Bookish Humor** — Wordplay, puns, funny book references
- **Mental Health + Books** — Anxiety, depression, coping through reading
- **Dark Romance** — Spicy books, morally grey characters, trope references
- **Fandom In-Jokes** — Series-specific quotes and inside references
- **Relatable Problems** — TBR piles, book buying guilt, late-night reading
- **Dark Humor** — Morbid jokes, nihilism, dark sarcasm
- **BookTok** — Trending topics and TikTok-specific references

Create new niches as needed for your research.

## Common Products

- `t-shirt` — Classic apparel
- `sticker` — Vinyl stickers, phone/laptop
- `mug` — Coffee/tea mugs
- `hoodie` — Hooded sweatshirt
- `tote bag` — Canvas bags
- `poster` — Print art
- `sweatshirt` — Crew neck sweatshirt
- `bookmark` — Paper/cardstock bookmarks

## Validation

Before importing, ensure:

- JSON is valid (no trailing commas, proper quotes)
- Each idea has required fields: `title`, `niche`, `description`, `audience`
- At least one of `research`, `text_to_image_prompt`, `products` is provided (recommended)
- No duplicate titles in the same batch

-- Migration: Create design_ideas table
-- Description: Table to store merch design ideas with research, audience, and prompts

CREATE TABLE IF NOT EXISTS public.design_ideas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    niche TEXT NOT NULL,
    description TEXT NOT NULL,
    audience TEXT,
    research TEXT,
    text_to_image_prompt TEXT,
    products TEXT[],
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

-- Enable RLS
ALTER TABLE public.design_ideas ENABLE ROW LEVEL SECURITY;

-- Policy: User can select all (personal ideas)
CREATE POLICY "user_select_design_ideas" 
    ON public.design_ideas 
    FOR SELECT 
    USING (true);

-- Policy: User can insert
CREATE POLICY "user_insert_design_ideas" 
    ON public.design_ideas 
    FOR INSERT 
    WITH CHECK (true);

-- Policy: User can update
CREATE POLICY "user_update_design_ideas" 
    ON public.design_ideas 
    FOR UPDATE 
    USING (true)
    WITH CHECK (true);

-- Policy: User can delete
CREATE POLICY "user_delete_design_ideas" 
    ON public.design_ideas 
    FOR DELETE 
    USING (true);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_design_ideas_niche ON public.design_ideas(niche);
CREATE INDEX IF NOT EXISTS idx_design_ideas_created_at ON public.design_ideas(created_at DESC);

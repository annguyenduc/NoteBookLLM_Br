-- wiki_brain.db Schema
-- Single Source of Truth for NoteBookLLM_Br Wiki 2.0

-- 1. Table for Wiki Atoms (Markdown files)
CREATE TABLE IF NOT EXISTS atoms (
    file_id TEXT PRIMARY KEY,           -- e.g., 'concepts/CONCEPT_PY_Pandas_Basics.md'
    title TEXT NOT NULL,
    type TEXT NOT NULL,                -- concept, entity, source, comparison, synthesis
    status TEXT DEFAULT 'stub',        -- stub, verified, synthesized (Human Only)
    agent_id TEXT,                     -- agent who created/last modified
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    file_hash TEXT,                    -- for change detection
    metadata JSON                      -- extensible metadata (tags, aliases, etc.)
);

-- 2. Table for Raw Sources
CREATE TABLE IF NOT EXISTS sources (
    source_id TEXT PRIMARY KEY,        -- e.g., 'raw/sources/book_llm.pdf'
    name TEXT NOT NULL,
    path TEXT NOT NULL,
    source_type TEXT,                  -- pdf, md, url, office
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSON
);

-- 3. Table for Links (Graph)
CREATE TABLE IF NOT EXISTS links (
    source_id TEXT NOT NULL,           -- atom or source
    target_id TEXT NOT NULL,           -- atom
    link_type TEXT NOT NULL,           -- 'wikilink', 'source_tracing'
    PRIMARY KEY (source_id, target_id, link_type),
    FOREIGN KEY (target_id) REFERENCES atoms(file_id)
);

-- 4. Table for Agent Logs/Tasks
CREATE TABLE IF NOT EXISTS task_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id TEXT NOT NULL,
    action TEXT NOT NULL,              -- ingest, absorb, query, breakdown, cleanup, rebuild
    target_file TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT,                       -- success, failure, pending
    details TEXT
);

-- 5. Table for Session Insights
CREATE TABLE IF NOT EXISTS session_insights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tags TEXT
);

-- 6. Full Text Search (FTS5) for fast discovery
CREATE VIRTUAL TABLE IF NOT EXISTS atom_search USING fts5(
    file_id UNINDEXED,
    title,
    content,
    tokenize='porter unicode61'
);

-- Triggers for FTS sync (optional, usually handled by scripts)
-- Trigger for automatic updated_at
CREATE TRIGGER IF NOT EXISTS update_atom_timestamp 
AFTER UPDATE ON atoms
BEGIN
    UPDATE atoms SET updated_at = CURRENT_TIMESTAMP WHERE file_id = OLD.file_id;
END;

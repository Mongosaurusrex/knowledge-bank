CREATE TABLE knowledge_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    embedding VECTOR(1536), 
    source_file TEXT,
    title TEXT,
    section TEXT,
    chunk_index INT
);
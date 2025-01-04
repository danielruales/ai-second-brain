SELECT 
    m.id,
    m.url,
    m.media_type,
    m.status,
    m.created_at,
    wp.title,
    wp.description,
    wp.summary,
    wp.author,
    wp.published_at
FROM media m
LEFT JOIN web_pages wp ON wp.media_id = m.id
WHERE m.media_type = 'web-page'
ORDER BY m.created_at DESC
LIMIT 100
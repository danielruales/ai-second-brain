def create_content_from_df(df):
    """Convert dataframe rows into formatted content string."""
    all_content = '<articles>\n'
    all_content_list=[]
    all_content_dict = {}
    
    for idx, row in df.iterrows():
        # Format each article with consistent structure
        content = f"""
Title: {row['title']}
URL: {row['url']}
Summary: {row['summary']}
Description: {row['description']}
Created: {row['created_at'].strftime('%Y-%m-%d')}
Type: {row['media_type']}
"""
        # print('HERE***********', all_content_list)
        all_content += content
        all_content_list.append(content)
        all_content_dict[idx+1] = {
            "title": row['title'],
            "url": row['url'],
            "summary": row['summary'],
            "description": row['description'],
            "created_at": row['created_at'].strftime('%Y-%m-%d'),
            "media_type": row['media_type'],
            "content": content
        }
    all_content += '\n</articles>\n--------------------\n'
    
    return all_content, all_content_list, all_content_dict

def create_chunked_content(df, chunk_character_max_length=1000):
    """Create a chunked content string from a dataframe."""
    all_content = '<articles>\n'
    all_content_list=[]
    all_content_dict = {}

    for idx, row in df.iterrows():
        for chunk in (row['content'], chunk_character_max_length):
            pass
    
    return all_content, all_content_list, all_content_dict
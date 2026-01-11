def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if document_id == target_document_id:
            return level
        else:
            found_level = count_nested_levels(
                nested_documents[document_id], target_document_id, level + 1
            )
            if found_level != -1:
                return found_level
    return -1

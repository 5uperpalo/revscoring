import re

from ..datasources import previous_revision_metadata, revision_metadata
from ..util.dependencies import depends


@depends(on=[previous_revision_metadata, revision_metadata])
def is_same_author(previous_revision_metadata, revision_metadata):
    
    return previous_revision_metadata.user_text == revision_metadata.user_text

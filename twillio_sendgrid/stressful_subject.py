import re

def is_stressful(subj):
    return (subj.isupper() or
            subj.endswith('!!!') or
            any(re.search('+[.!-]*'.join(c for c in word), subj.lower())
                for word in ['help', 'asap', 'urgent']))
def simplify_path(path):
    is_abs, out = path.startswith('/'), []
    for subdir in path.split('/'):  
        is_up = (is_abs or (out and out[-1] != '..')) and subdir == '..'            
        out = out[:-1] if is_up else out+[subdir]*(subdir not in '.')
    return '/'*is_abs+'/'.join(out) or '.'
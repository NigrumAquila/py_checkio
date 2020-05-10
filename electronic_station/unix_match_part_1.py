import re
unix_match=lambda x,y: re.fullmatch(''.join(['.' if i=='?' else i for i in ''.join(['.*' if i=='*' else i for i in ''.join(['\.' if i=='.' else i for i in y])])]),x)!=None
'''
'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
'''

def is_merge(s, part1, part2):
    if not s:
        return part1 + part2 == ''
    if not part1:
        return s == part2
    if not part2:
        return s == part1
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
        return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False
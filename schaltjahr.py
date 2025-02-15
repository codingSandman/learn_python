"""
Ein Schaltjahr ist ein Kalenderjahr, das einen zusätzlichen Schalttag enthält.
Der zusätzliche Tag (29.02.) tritt in jedem Jahr auf das ein Vielfaches von 4 ist, außer den Jahren, welche Vielfache
von 100 sind, es sei denn sie sind auch durch 400 teilbar.
"""

jahr = 2025

if jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0):
    print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")
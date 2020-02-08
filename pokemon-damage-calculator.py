def calculate_damage(your_type, opponent_type, attack, defense):
    eff = {'fire': {'water': 0.5, 'grass': 2, 'electric': 1},
           'water': {'fire': 2, 'grass': 0.5, 'electric': 0.5},
           'grass': {'fire': 0.5, 'water': 2, 'electric': 1},
           'electric': {'fire': 1, 'water': 2, 'grass': 1}}
    
    if your_type == opponent_type:
        effectiveness = 0.5
    else:
        effectiveness = eff[your_type][opponent_type]
        
    return int(50 * (attack / defense) * effectiveness)

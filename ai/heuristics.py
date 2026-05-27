from game.game_state import GameState
from game.constants import PlayerId
from ai.pathfinding import get_shortest_path_length

def evaluate_state(state: GameState, maximizing_player: PlayerId) -> float:
    """
    Evaluates the board state.
    Positive score is good for maximizing_player, negative is bad.
    """
    if state.is_game_over():
        if state.winner == maximizing_player:
            return 10000.0
        else:
            return -10000.0
            
    p1 = state.p1
    p2 = state.p2
    
    p1_dist = get_shortest_path_length(state.board, p1.x, p1.y, p1.goal_y)
    p2_dist = get_shortest_path_length(state.board, p2.x, p2.y, p2.goal_y)
    
    # A smaller distance is better.
    # Score is difference in distances.
    # If maximizing_player is P1, we want P2 dist to be high, P1 dist to be low.
    if maximizing_player == PlayerId.PLAYER_1:
        score = p2_dist - p1_dist
        # Add slight bonus for keeping walls
        score += (p1.walls_left - p2.walls_left) * 0.5
    else:
        score = p1_dist - p2_dist
        score += (p2.walls_left - p1.walls_left) * 0.5
        
    return float(score)

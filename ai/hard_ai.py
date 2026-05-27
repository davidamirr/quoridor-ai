from game.game_state import GameState, Move
from .minimax import minimax

def get_hard_ai_move(state: GameState) -> Move:
    """Uses Minimax with Alpha-Beta pruning to find the best move."""
    # Depth 2 ensures responsiveness while providing decent strategy
    DEPTH = 2
    _, best_move = minimax(state, depth=DEPTH, alpha=float('-inf'), beta=float('inf'), maximizing_player=state.current_turn)
    
    if best_move is None:
        # Fallback to medium AI if something goes wrong
        from .medium_ai import get_medium_ai_move
        return get_medium_ai_move(state)
        
    return best_move

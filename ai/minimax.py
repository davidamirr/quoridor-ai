from typing import Tuple, List, Optional
from game.game_state import GameState, Move, PawnMove, WallMove
from game.constants import PlayerId, BOARD_SIZE, WallOrientation
from game.rules import get_valid_pawn_moves, is_wall_placement_valid
from game.wall import Wall
from .heuristics import evaluate_state
import random

def get_all_possible_moves(state: GameState) -> List[Move]:
    moves: List[Move] = []
    player = state.get_current_player()
    opponent = state.get_opponent()
    
    # Pawn moves
    valid_pawn_moves = get_valid_pawn_moves(state.board, player, opponent)
    for mx, my in valid_pawn_moves:
        moves.append(PawnMove(player.id, mx, my))
        
    # Wall moves
    if player.walls_left > 0:
        # Heuristic: only consider walls near the opponent to block their shortest path
        # This drastically reduces branching factor
        wall_candidates = []
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0, 1, 2]:
                x = opponent.x + dx
                y = opponent.y + dy
                if 0 <= x < BOARD_SIZE - 1 and 0 <= y < BOARD_SIZE - 1:
                    wall_candidates.append(Wall(x, y, WallOrientation.HORIZONTAL))
                    wall_candidates.append(Wall(x, y, WallOrientation.VERTICAL))
        
        valid_walls = []
        for w in set(wall_candidates):
            if is_wall_placement_valid(state.board, w, state.p1, state.p2):
                valid_walls.append(w)
                
        # Limit to 8 randomly selected valid walls around the opponent to keep search fast
        random.shuffle(valid_walls)
        for w in valid_walls[:8]:
            moves.append(WallMove(player.id, w))
            
    return moves

def minimax(state: GameState, depth: int, alpha: float, beta: float, maximizing_player: PlayerId) -> Tuple[float, Optional[Move]]:
    if depth == 0 or state.is_game_over():
        return evaluate_state(state, maximizing_player), None
        
    is_maximizing = state.current_turn == maximizing_player
    best_move = None
    
    moves = get_all_possible_moves(state)
    if not moves:
        return evaluate_state(state, maximizing_player), None
        
    if is_maximizing:
        max_eval = float('-inf')
        for move in moves:
            next_state = state.copy()
            next_state.execute_move(move)
            
            eval_score, _ = minimax(next_state, depth - 1, alpha, beta, maximizing_player)
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
                
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            next_state = state.copy()
            next_state.execute_move(move)
            
            eval_score, _ = minimax(next_state, depth - 1, alpha, beta, maximizing_player)
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
                
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

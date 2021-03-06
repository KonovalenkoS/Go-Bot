from dlgo.gotypes import Point

def is_point_an_eye(board, point, color):
	#Eyes should be empty points
	if board.get(point) is not None:
		return False
	#Adjacent points must be friendly stones
	for neighbor in point.neighbors():
		neighbor_color = board.get(neighbor)
		if neighbor_color != color:
			return False

	#Check that the proper spaces are controlled for an eye
	friendly_corners = 0
	off_board_corners = 0
	corners = [
		Point(point.row - 1, point.col - 1),
		Point(point.row - 1, point.col + 1),
		Point(point.row + 1, point.col - 1),
		Point(point.row + 1, point.col + 1)
	]
	for corner in corners:
		if board.is_on_grid(corner):
			corner_color = board.get(corner)
			if corner_color == color:
				friendly_corners += 1
		else:
			off_board_corners += 1
	if off_board_corners > 0:
		#point is on the edge or corner
		return off_board_corners + friendly_corners == 4
	#Point is in the middle
	return friendly_corners >= 3
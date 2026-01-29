package main

func createMatrix(rows, cols int) (matrix [][]int) {
	for row := range rows {
		currentRow := []int{}
		for col := range cols {
			currentRow = append(currentRow, row*col)
		}
		matrix = append(matrix, currentRow)
	}

	return
}

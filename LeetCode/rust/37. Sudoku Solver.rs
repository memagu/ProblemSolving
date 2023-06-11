struct Solution;

impl Solution {
    fn is_valid(board: &[Vec<char>], num: char, row: usize, col: usize) -> bool {
        if (0..9).any(|i| num == board[row][i] && i != col || num == board[i][col] && i != row) {
            return false;
        }

        let box_row_start: usize = row / 3usize * 3usize;
        let box_col_start: usize = col / 3usize * 3usize;

        !(box_row_start..box_row_start + 3).any(|i| {
            (box_col_start..box_col_start + 3).any(|j| {
                (i, j) != (row, col) && board[i][j] == num
            })
        })
    }

    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        let possible: Vec<([usize; 2], Vec<char>)> = (0..9)
            .flat_map(|row| (0..9).map(move |col| (row, col)))
            .filter(|&(row, col)| board[row][col] == '.')
            .map(|(row, col)| {
                (
                    [row, col],
                    ('1'..='9')
                        .filter(|&num| Self::is_valid(board, num, row, col))
                        .collect::<Vec<char>>()
                )
            })
            .collect::<Vec<([usize; 2], Vec<char>)>>();

        let mut stack: Vec<[usize; 2]> = vec![[0, 0]];

        while !stack.is_empty() {
            let [index, num_index] = *stack.last().unwrap();

            if index == possible.len() {
                break;
            }

            let ([row, col], nums) = (possible[index].0, &possible[index].1);

            if num_index >= nums.len() {
                board[row][col] = '.';
                stack.pop();
                continue;
            }

            stack.last_mut().unwrap()[1] += 1;

            if Self::is_valid(board, nums[num_index], row, col) {
                board[row][col] = nums[num_index];
                stack.push([index + 1usize, 0usize]);
            }
        }
    }
}

fn main() {
    let mut board: Vec<Vec<char>> = vec![
        vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ];

    Solution::solve_sudoku(&mut board);
    println!("{:?}", board)
}
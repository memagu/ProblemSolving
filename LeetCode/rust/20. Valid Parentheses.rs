enum Bracket {
    Open(char),
    Close(char),
}

impl Bracket {
    pub fn from_char(c: char) -> Option<Bracket> {
        match c {
            '{' | '[' | '(' => Some(Bracket::Open(c)),
            '}' => Some(Bracket::Close('{')),
            ']' => Some(Bracket::Close('[')),
            ')' => Some(Bracket::Close('(')),
            _ => None,
        }
    }
}

struct Solution {}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        if s.len() % 2 == 1 {
            return false;
        }

        let mut bracket_stack: Vec<char> = Vec::new();
        for c in s.chars() {
            match Bracket::from_char(c) {
                Some(Bracket::Open(char_bracket)) => {
                    bracket_stack.push(char_bracket);
                }
                Some(Bracket::Close(char_close_bracket)) => {
                    if bracket_stack.pop() != Some(char_close_bracket) {
                        return false;
                    };
                }
                _ => (),
            };
        };
        bracket_stack.is_empty()
    }
}

fn main() {
    println!("{}", Solution::is_valid("()".to_string()));
    println!("{}", Solution::is_valid("()[]{}".to_string()));
    println!("{}", Solution::is_valid("(]".to_string()));
}
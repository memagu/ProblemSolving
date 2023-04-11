struct Solution;

impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        sentences.into_iter().map(|sentence| sentence.split_whitespace().count()).max().unwrap_or(0usize) as i32
    }
}

fn main() {
    println!("{}", Solution::most_words_found(vec!("alice and bob love leetcode".to_string(),
                                                   "i think so too".to_string(),
                                                   "this is great thanks very much".to_string())));
    println!("{}", Solution::most_words_found(vec!("please wait".to_string(),
                                                   "continue to fight".to_string(),
                                                   "continue to win".to_string())));
}
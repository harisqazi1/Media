// Reading argument values from env
use std::{env};
// Bring functions from lib.rs file
use label_it::{wordlist_gen, wordlist_output};

fn main() {
    // Collecting the environmental variables into a String Vector
    let args: Vec<String> = env::args().collect();
    // Check to make sure user put in expected arguments
    let _input_check = std::env::args().nth(1).expect("\nERROR: No Input File Provided!\nFormat: disk_namer wordlist amount_of_output output_file (optional)\n\n");
    let _amount_check = std::env::args().nth(2).expect("\nERROR: No Amount Provided!\nFormat: disk_namer wordlist amount_of_output output_file (optional)\n\n");
    // Proceed based on input arguments
    if args.len() == 3 {
        for strings in wordlist_gen(args[1].clone(), args[2].parse::<u8>().unwrap()) {
            print!("{strings}");
        }
    } else if args.len() == 4 {
        wordlist_output(wordlist_gen(args[1].clone(), args[2].parse::<u8>().unwrap()), args[3].clone());
    } else {
        panic!("\nERROR: Too Many Args\n");
    }
}
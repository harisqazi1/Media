use std::{fs, fs::read_to_string, fs::OpenOptions, fs::File, path::Path};
use rand::Rng;
use titlecase::titlecase;
use std::io::{Seek, SeekFrom, Write};

// Creates the wordlist for output
pub fn wordlist_gen(input_file: String, amount: u8) -> Vec<String> {
    // String Vector to hold all of the values in comma format
    let mut result: Vec<String> = Vec::new();
    // Output vector
    let mut output: Vec<String> = Vec::new();       
    // char array to use in password
    //let ch: [char; 11] = [')','(','*','&','^','%','$','#','@','!','~'];
    // Push each line to the Vector
    for line in read_to_string(input_file).unwrap().lines() {
        // Add a Titlecased version of the string to the string Vector
        result.push(titlecase(line));
    }
    // Header
    output.push("# Drives -----------".to_string());
    // From 0 to the users input 
    for _integers in 0..amount {
        // Output all the strings to the Vector to output
        output.push("\nCodename: ".to_string());
        output.push(result[random_gen(result.len()-1)].clone());
        output.push(result[random_gen(result.len()-1)].clone());
        output.push("\n".to_string());
        output.push("Make & Model: \n".to_string());
        output.push("Serial Number: \n".to_string());
        output.push("Size: \n".to_string());
        output.push("Date Purchased: \n".to_string());
        output.push("Encryption Type: \n".to_string());
        // Remove from 36-46 if you want to remove password field
        // output.push("Password: ".to_string());
        // output.push(result[random_gen(result.len()-1)].clone());
        // output.push(ch[random_gen(ch.len()-1)].to_string().clone());
        // output.push(result[random_gen(result.len()-1)].clone());
        // output.push(ch[random_gen(ch.len()-1)].to_string().clone());
        // output.push(result[random_gen(result.len()-1)].clone());
        // output.push(ch[random_gen(ch.len()-1)].to_string().clone());
        // output.push(result[random_gen(result.len()-1)].clone());
        // output.push(ch[random_gen(ch.len()-1)].to_string().clone());
        // output.push(result[random_gen(result.len()-1)].clone());
        // output.push("\n".to_string());
    }

    output

}

// Function to generate a random usize variable to use instead of having to copy and paste the same line over and over again
pub fn random_gen(maximum: usize) -> usize {
    let output: usize = rand::rng().random_range(0..=maximum);
    output
}

// Function to update a file if you use it to keep track of Drive names
// Check codenames to make sure output doesn't include reused codeword
pub fn wordlist_output(input: Vec<String>, filepath: String){
    // Cloning the filepath so we can use it later to output our data
    let file_path_clone: String = filepath.clone();
    // Vector String to hold the output file into
    let mut file_to_vec: Vec<String> = Vec::new();
    // Adding the input Vector to the following string var
    let mut input_to_str: String = String::new();
    // Checking if the file exists, if not creating one:
    if !Path::new(&file_path_clone).exists() {
        // create the file
        let mut _file = File::create(file_path_clone.clone()).unwrap();
        // Add the first line
        let mut first_line = OpenOptions::new().write(true).append(true).open(&file_path_clone).unwrap();
        writeln!(first_line, "# Drives -----------").expect("Failed to write to output file");
    } 
    // Read the file from the filepath string input parameter
    let contents = fs::read_to_string(&filepath)
    .expect("Should have been able to read the file");
    //Add the file to the aforementioned Vector
    for line in contents.split("\n") {
        file_to_vec.push(line.to_string());
    }
    // Adding the input to the other Vector
    for line in input {
        input_to_str.push_str(line.as_str());
    }
    // Sending the input_to_str to a Vector
    let mut input_to_vec: Vec<String> = Vec::new();
    // Function to add the input_to_string to send it to the aforementioned vector
    for words in input_to_str.split("\n") {
        input_to_vec.push(words.to_string());
    }
    //new vector to hold the final output
    let mut output_final: Vec<String> = Vec::new();
    // Check if any of the Codename used is already in the file2vec, if so replace input with backup
    // starting from #1 to not account for the #Drives ---- line
    for each_item in 1..input_to_vec.len() {
        //println!("ITEM {}: {}", each_item, input_to_vec[each_item]);
        if input_to_vec[each_item].starts_with("Codename"){
            if file_to_vec.contains(&input_to_vec[each_item]) {
                // push final output from backup_plan function.
                output_final.push(backup_plan());
            } else {
                output_final.push(input_to_vec[each_item].clone());
            }
        } else {
            output_final.push(input_to_vec[each_item].clone());
        }
    }
    // New File variable, so we can append to the already created file
    let mut file = OpenOptions::new().write(true).append(true).open(file_path_clone).unwrap();
    // Not sure if this line is needed or not specifically
    file.seek(SeekFrom::End(0)).unwrap();
    // For loop to output to file
    for items in output_final {
        // write the output to the file
        writeln!(file, "{items}").expect("Failed to write to output file");
    }
    
}

//When a codeword is matching use this function to replace with a new one from /usr/share/dict/words
pub fn backup_plan() -> String {
    // Output string
    let mut output: String = String::new();
    // Adding Codename to fill that part out
    output.push_str("Codename: ");
    // Read from the backup file
    let contents = fs::read_to_string("/usr/share/dict/words")
    .expect("Should have been able to read the file");
    // Add these to a vector
    let mut cont_vec: Vec<String> = Vec::new();
    for value in contents.split("\n") {
        cont_vec.push(value.to_string());
    }
    //Remove \n from last line which got added to vector
    cont_vec.pop();
    // Output 2 words from the backup file to then replace the duplicate codeword
    output.push_str(&titlecase(&cont_vec[random_gen(cont_vec.len()-1)].clone()));
    output.push_str(&titlecase(&cont_vec[random_gen(cont_vec.len()-1)].clone()));

    output
}